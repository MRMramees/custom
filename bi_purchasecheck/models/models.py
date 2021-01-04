 

# -*- coding: utf-8 -*-

from odoo import models, fields, api
import time
from datetime import datetime
import odoo.addons.decimal_precision as dp
from odoo.exceptions import UserError


class bi_purchasebutton(models.Model):
	_inherit = 'crm.lead'


	purchase_order_ids = fields.Many2many('purchase.order','crm_id')

	
	


	#smartbutton
	
	purchase_order_count = fields.Integer(compute='compute_count')
	
	def purchase_order(self):
		purchase_order_ids=self.mapped('purchase_order_ids')
		
		if len(purchase_order_ids) > 1:
					return {
						'name': ('Attachments'),
						'type': 'ir.actions.act_window',
						'res_model':'purchase.order',
						'view_mode':'tree,form',
						'domain': [('id', 'in', self.purchase_order_ids.ids)],
						'target':'current',
					}
		
		elif len(purchase_order_ids) == 1:
					return {
						'name': ('Attachments'),
						'type': 'ir.actions.act_window',
						'res_model':'purchase.order',
						'view_mode':'form',
						'res_id': self.purchase_order_ids.id,
						'target':'current',
				}

#count-----
	
	def compute_count(self):
		self.purchase_order_ids = self.mapped('purchase_order_ids')
		for record in self:
			record.purchase_order_count = len(record.purchase_order_ids)

class crm_button(models.Model):
	_inherit = 'purchase.order'

	crm_id=fields.Many2many('crm.lead')

class createpurchaseorder(models.TransientModel):
	
	_name = 'create.purchaseorder'
	_description = "Create Purchase Order"

	new_order_line_ids = fields.One2many( 'getsale.orderdata', 'new_order_line_id',String="Order Line")
	partner_id = fields.Many2one('res.partner', string='Vendor', required = True)
	date_order = fields.Datetime(string='Order Date', required=True, copy=False, default=fields.Datetime.now)
	

	def action_create_purchase_order(self):
	
		res = self.env['purchase.order']
		value = []
		
		for data in self.new_order_line_ids:

			final_price = data.product_id.standard_price
			 	
			value.append([0,0,{
								'product_id' : data.product_id.id,
								'name' : data.name,
								'product_qty' : data.product_qty,
								'order_id':data.order_id.id,
								'product_uom' : data.product_uom.id,
								'taxes_id' : data.product_id.supplier_taxes_id.ids,
								'date_planned' : data.date_planned,
								'price_unit' : final_price,
								}])
		purchase = res.create({
						'partner_id' : self.partner_id.id,
						'date_order' : str(self.date_order),
						'order_line':value,
						
				})
		
		crm_order_id = self.env['crm.lead'].browse(self.env.context['active_id'])
		crm_order_id.purchase_order_ids = [(4,purchase.id)]
	

#auotomatic form 
		return {
        #'name': self.order_id,
        'res_model': 'purchase.order',
        'type': 'ir.actions.act_window',
        'context': {},
        'view_mode': 'form',
        'view_type': 'form',
		'res_id': purchase.id,
        'view_id': self.env.ref("purchase.purchase_order_form").id,
        'target': 'self'
    }



class Getsaleorderdata(models.TransientModel):
	_name = 'getsale.orderdata'
	_description = "Get Sale Order Data"

	new_order_line_id = fields.Many2one('create.purchaseorder')
		
	product_id = fields.Many2one('product.product', string="Product", required=True)
	name = fields.Char(string="Description")
	product_qty = fields.Float(string='Quantity', required=True)
	date_planned = fields.Datetime(string='Scheduled Date', default = datetime.today())
	product_uom = fields.Many2one('uom.uom', string='Product Unit of Measure')
	order_id = fields.Many2one('sale.order', string='Order Reference', required=True, ondelete='cascade', index=True, copy=False)
	price_unit = fields.Float(string='Unit Price', required=True, digits=dp.get_precision('Product Price'))
	product_subtotal = fields.Float(string="Sub Total", compute='_compute_total')
#-------

     
                            



#------	
	@api.depends('product_qty', 'price_unit')
	def _compute_total(self):
		for record in self:
			record.product_subtotal = record.product_qty * record.price_unit



			