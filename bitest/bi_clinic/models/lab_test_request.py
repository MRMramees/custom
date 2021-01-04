from odoo import fields, models, api

class LabTestRequests(models.Model):
    _name = 'bi.lab.test.requests'
    _description = 'bi_clinic.lab.test.requests'
    _rec_name = 'request_no'

    request_no = fields.Char(string="Request ID", required=True, readonly=True, index=True,copy=False, default='New')
    patient_info_id = fields.Many2one('bi.patient.info',string="Patient")
    physician_info_id = fields.Many2one('bi.physician.info',string="Doctor")
    state = fields.Selection([('draft', 'Draft'), ('result', 'Result')],readonly=True, string='Status', default='draft')
    urgent = fields.Boolean(string="Urgent")
    lab_test_request_line = fields.One2many('bi.lab.test.request.type','test_request_id',string="Test requests")
    # test_type_line = fields.One2many('bi.lab.test.request.type.line','request_type_line_id',string="Requests")

    @api.model
    def create(self, vals):
        if vals.get('request_no','New') == 'New':
            vals['request_no']= self.env['ir.sequence'].next_by_code('bi.clinic.lab.test.request.sequence') or 'New'
            result= super(LabTestRequests,self).create(vals)
            return result
    
    # below code created for onchange event. later plan changed. Inorder to activate this code.
    # uncomment lab_invoice from init, and views/account_invoice_view_inherit.xml from manifext.
    # def action_create_invoice(self):    
    #     action = self.env.ref('account.action_move_out_invoice_type')
    #     result = action.read()[0]
    #     result['context'] = {
    #         'default_type': 'in_invoice',
    #         'default_lab_request_id': self.id
    #         }

    #      # choose the view_mode accordingly
    #     res = self.env.ref('account.view_move_form', False)
    #     form_view = [(res and res.id or False, 'form')] 
    #     if 'views' in result:
    #             result['views'] = form_view + [(state,view) for state,view in action['views'] if view != 'form']
    #     else:
    #         result['views'] = form_view
    #     return result
    

    def action_create_invoice(self):
        rec_list = []
        for rec in self.lab_test_request_line:
            rec_list.append((0,0, {
                'name': rec.test_type_id.name + ":" + rec.test_request_type_line_id.name,
                'price_unit': rec.test_request_type_line_id.test_rate,
                'account_id': rec.test_type_id.account_id
                })),

        vals = {
                'ref': self.request_no,
                'type':'out_invoice',
                'partner_id': self.patient_info_id.patient_id.id,
                'invoice_partner_display_name': self.patient_info_id.patient_id.name,
                'type': 'out_invoice',
                'invoice_line_ids': rec_list,
        }
        invoice_id = self.env['account.move'].create(vals)

        if invoice_id:
            return {
                'name': 'Create invoice/bill',
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'account.move',
                'view_id': self.env.ref('account.view_move_form').id,
                'res_id': invoice_id.id
            }


class LabTestRequestType(models.Model):
    _name = 'bi.lab.test.request.type'
    _description = 'bi_clinic.lab.test.request.type'
    _rec_name = 'test_request_id'

    test_request_id = fields.Many2one('bi.lab.test.requests')
    test_type_id= fields.Many2one('bi.lab.test.type',string="Test Type")
    test_request_type_line_id= fields.Many2one('bi.lab.test.type.line',string="Type Line")
    test_result = fields.Float("Result")



    #     below commented code taken from purchase.py. to activate this way uncomment lab_invoice, 
    # def _prepare_account_move_line(self, move):
    #     self.ensure_one()
    #     vals = {
    #         'name': '%s: %s' % (self.test_type_id.name, self.test_request_type_line_id.name),
    #         'move_id': move.id,
    #         'price_unit': self.test_request_type_line_id.test_rate,
    #     }
    #     return vals
