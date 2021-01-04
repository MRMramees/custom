

from odoo import models, fields, api
from odoo.exceptions import UserError, AccessError
import datetime

class SaleReportWizard(models.TransientModel):
        _name = 'invoice.report.wizard'
        
        date_from = fields.Date(string='Start Date',required=True)
        date_to = fields.Date(string='End Date',default=fields.Date.today)
        
        def print_report_xl(self):
            
            record_ids = self.env['account.move'].search([('invoice_date', '>=', self.date_from),('invoice_date', '<=', self.date_to)])
            if len(record_ids)== 0:
                raise UserError("No Data Found") 
            else:
                context = self._context
                datas = {'ids': context.get('active_ids', [])}
                datas['form'] = self.read()[0]
                for field in datas['form'].keys():
                    if isinstance(datas['form'][field], tuple):
                        datas['form'][field] = datas['form'][field][0]
                return self.env.ref('bi_excelpdf.report_sale_docs').report_action(self, data=datas)

        def print_report_pdf(self):
            # date_from = datetime.datetime.strptime(str(self.date_from), '%Y-%m-%d').strftime('%Y-%m-%d')
            # date_to = datetime.datetime.strptime(str(self.date_to), '%Y-%m-%d').strftime('%Y-%m-%d')

            data = {
            'ids': self.ids,
            'model': self._name,
            'form': {
                'date_from': self.date_from,
                'date_to': self.date_to,
            },
        }

            return self.env.ref('bi_excelpdf.print_report_pdf').report_action(self,data=data)

class BiPdfReport(models.AbstractModel):

    _name = 'report.bi_excelpdf.report_template'

    # @api.model
    def _get_report_values(self,docids, data):

        date_from = data['form']['date_from']
        date_to = data['form']['date_to']

        self.env.cr.execute("""select am.name as id, am.invoice_partner_display_name, rp.name as name, am.invoice_date, am.invoice_date_due, am.amount_untaxed_signed, am.amount_total_signed, am.amount_residual_signed, am.state, am.invoice_payment_state
                                                from account_move am
                                                INNER JOIN res_users ru ON am.invoice_user_id = ru.id
                                                join res_partner rp on rp.id = ru.partner_id
                                                where invoice_date 
                                                between  '"""+str(date_from)+ """' 
                                                AND '"""+str(date_to)+"""' """)
        values = self.env.cr.dictfetchall()
        return {
                'values' : values,
                }