# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.tools.float_utils import float_compare, float_is_zero, float_round
from odoo.exceptions import UserError
import datetime



class bi_stock_tracking(models.Model):
    _name = 'bi.stock.tracking'
    _description = "Picking Type"
    _rec_name = 'sequence_no'

# -----Location----
    picking_from_id = fields.Many2one('stock.warehouse',string='Request To')
    transit_id = fields.Many2one('stock.location',string='Transit', default=18)
    company_id = fields.Many2one('res.company', 'Company', required=True, readonly=True,default=lambda s: s.env.company.id, index=True)
# -----Other---
    name = fields.Char(string='Reference')
    operation_type_id = fields.Many2one('stock.picking.type',string='Operation Type', default=5)
    scheduled_date = fields.Datetime(string="Date",default=datetime.datetime.now())
    move_type = fields.Selection([('direct', 'As soon as possible'), ('one', 'When all products are ready')], 'Shipping Policy', default='direct')
    description_picking = fields.Text('Description of Picking',default="Internal Transfer")
    move_line_ids = fields.Many2many('stock.move.line') 
    state = fields.Selection([
            ('draft', 'Draft'),
            ('request','To Approve'),
            ('reserved', 'Reserved'),
            ('transfered', 'Transfered'),
            ],default='draft')
    user_id = fields.Many2one(
        'res.users', 'Responsible', tracking=True,
        domain=lambda self: [('groups_id', 'in', self.env.ref('stock.group_stock_user').id)],
        states={'transfered': [('readonly', True)]},
        default=lambda self: self.env.user)
    rounding = fields.Float(
        'Rounding Precision', default=0.01, digits=0, required=True)
# -----sequence_no--------
    sequence_no = fields.Char('sequence_no', readonly=True,default='New')

    @api.model
    def create(self, vals):
        if vals.get('sequence_no', 'New') == 'New':
            vals['sequence_no'] = self.env['ir.sequence'].next_by_code('bi.stock.tracking') or '/'
        return super(bi_stock_tracking, self).create(vals)
# -----Products

    order_line_ids = fields.One2many('bi.orderline1','order1_id')

    def request(self):
        self.ensure_one()
        if not self.order_line_ids:
            raise UserError(_('Please add some items to move.'))
    
        self.write({
        'state': 'request',})

    def reserve(self):
        location_id = self.env['stock.warehouse'].search([('id','=',self.picking_from_id.id)])
        # record = self.env['stock.picking']

        for data in self.order_line_ids:
            available = data.product_id.with_context({'location': location_id.lot_stock_id.id}).sudo().qty_available
            if available == 0 :
                raise UserError(_('No quantity available.'))

            if available < data.product_uom_id._compute_quantity(data.qty_demand, data.product_id.uom_id):
                # raise UserError(_('Not enough quantity available.'))
                return self.action_generate_backorder_wizard()
            else:
                return self.do_reserve()

    def action_generate_backorder_wizard(self):
            view = self.env.ref('stock.view_backorder_confirmation')
            wiz = self.env['stock.backorder.confirmation1']
            return {
                'name': _('Create Backorder?'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'stock.backorder.confirmation1',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': wiz.id,
                'context': self.env.context,
            }
    def process_cancel_backorder(self):
        bi_stock_tracking_id = self.env[self.env.context.get['active_model']].browse(self.env.context['active_ids'])
        location_id = self.env['stock.location'].search([('user_id','=',self.user_id.id)])
        record = self.env['stock.picking']
        new_lines =[]
        for data in bi_stock_tracking_id :
            
            new_lines.append((0, 0, {
                'product_id'            :data.product_id.id,
                'product_uom_qty'       :data.qty_demand,
                'description_picking'   :self.description_picking,
                'name'                  :data.product_id.name,            
                'product_uom'           :data.product_uom_id,
                }))
        # qty_demand= self.env['stock.location'].search([('user_id','=',self.user_id.id)])

    def do_reserve(self):
        record = self.env['stock.picking']
        new_lines =[]
        for data in self.order_line_ids:
            
            new_lines.append((0, 0, {
                'product_id'            :data.product_id.id,
                'product_uom_qty'       :data.qty_demand,
                'description_picking'   :self.description_picking,
                'name'                  :data.product_id.name,            
                'product_uom'           :data.product_uom_id,
                }))

        location_id = self.env['stock.warehouse'].search([('id','=',self.picking_from_id.id)])

        pick = {}
        pick = {
            'picking_type_id'           :self.operation_type_id.id,
            'name'                      :record.product_id.display_name,
            'location_dest_id'          :self.transit_id.id,
            'location_id'               :location_id.lot_stock_id.id,
            'move_ids_without_package'  :new_lines,
            'move_type'                 :self.move_type,
            'company_id'                :self.company_id.id,
            'scheduled_date'            :self.scheduled_date,  
            'origin'                    :self.sequence_no,
        }
        
        picking = record.create(pick)            
        picking.action_confirm()
        picking.action_assign()
        picking.button_validate() 

        for data in self.order_line_ids:

            move = self.env['stock.move'].create({
            'name'              :self.sequence_no,
            'location_id'       :location_id.lot_stock_id.id,
            'location_dest_id'  :self.transit_id.id,
            'product_id'        :data.product_id.id,
            'product_uom'       :data.product_uom_id.id,
            'product_uom_qty'   :data.qty_demand,
             })

            move._action_confirm()
            move._action_assign()
            move.move_line_ids.write({'qty_done':data.qty_demand}) 
            move._action_done()

        self.write({
        'state': 'reserved',})

    def validate(self):
        record = self.env['stock.picking']
        location = self.env['stock.location'].search([('user_id','=',self.user_id.id)])
        new_lines =[]

        for data in self.order_line_ids:
            new_lines.append((0, 0, {
                'product_id'            :data.product_id.id,
                'product_uom_qty'       :data.qty_demand,
                'description_picking'   :self.description_picking,
                'name'                  :data.product_id.name,
                'product_uom'           :data.product_uom_id,
                }))

        pick = {}  
        pick = {
        'picking_type_id'           :self.operation_type_id.id,
        'name'                      :record.product_id.display_name,
        'location_dest_id'          :location.id,
        'location_id'               :self.transit_id.id,
        'move_ids_without_package'  :new_lines,
        'move_type'                 :self.move_type,
        'company_id'                :self.company_id.id,
        'scheduled_date'            :self.scheduled_date,
        'origin'                    :self.sequence_no,
        }

        picking =record.create(pick)
        
        for data in self.order_line_ids:
            move = self.env['stock.move'].create({
                'name'              :self.sequence_no,
                'location_id'       :self.transit_id.id,
                'location_dest_id'  :location.id,
                'product_id'        :data.product_id.id,
                'product_uom'       :data.product_uom_id.id,
                'product_uom_qty'   :data.qty_demand,
            })

            move._action_confirm()
            move._action_assign()
            move.move_line_ids.write({'qty_done':data.qty_demand}) 
            move._action_done()

        picking.action_confirm()
        picking.action_assign()
        picking.button_validate()

        self.write({
        'state': 'transfered',})

class UserId(models.Model):
    _inherit = 'stock.location'

    user_id = fields.Many2one('res.users')

class LocationId(models.Model):
    _inherit = 'res.users'

    location_ids = fields.Many2many('stock.location', 'user_id')

class OrderLine(models.Model):
    _name = 'bi.orderline1'
    _description = "Order Line"

    order1_id = fields.Many2one('bi.stock.tracking', string='')


    product_id = fields.Many2one('product.product',string='Product')
    qty_demand = fields.Float(string='Quantity', digits='Product Unit of Measure', default=1.0)
    product_uom_id = fields.Many2one('uom.uom', 'Unit of Measure', required=True, domain="[('category_id', '=', product_uom_category_id)]")
    product_uom_category_id = fields.Many2one(related='product_id.uom_id.category_id')

    @api.onchange('product_id')
    def onchange_product_id(self):
        product = self.product_id.with_context(lang=self.env.user.lang)
        self.product_uom_id = product.uom_id.id


class StockBackorderConfirmation1(models.TransientModel):
    _name = 'stock.backorder.confirmation1'
    _description = 'Backorder Confirmation1'


    # pick_ids = fields.Many2many('stock.picking', 'stock_picking_backorder_rel')

    def _process(self, cancel_backorder=False):
        for confirmation in self:
            if cancel_backorder:
                for pick_id in confirmation.pick_ids:
                    moves_to_log = {}
                    for move in pick_id.move_lines:
                        if float_compare(move.product_uom_qty,
                                         move.quantity_done,
                                         precision_rounding=move.product_uom.rounding) > 0:
                            moves_to_log[move] = (move.quantity_done, move.product_uom_qty)
                    pick_id._log_less_quantities_than_expected(moves_to_log)
            confirmation.pick_ids.with_context(cancel_backorder=cancel_backorder).action_done()

    def process1(self):
        self._process()

    def process_cancel_backorder(self):
        self._process(cancel_backorder=True)