from odoo import models, fields, api
from datetime import datetime,timedelta,date
import base64

class bi_emailtest1(models.Model):
    _name = 'bi.emailtest1'
    _inherit = 'report.bi_pdf1.report_template'
    _description = 'bi_emailtest1'

#------------report attachment method email date filter invoice module -------------------------------------

    sender = fields.Char(string='From', default='ramees@bassaminfotech.com')
    recipients_id = fields.Char(string='', default='rameesmrm1@gmail.com')
    message_body = fields.Text(string='')
    current_date = fields.Date(string='', default=fields.Date.today)
    attach_file = fields.Binary(string='')

#-------------------------------------------------------------------------------
    date_to = date.today()
    date_from = date_to - timedelta(days=60)
#-------------------------------------------------------------------------------

    def action_send_email(self):
        dataa = {
            'form' :{      
                        'date_from': self.date_from,
                        'date_to': self.date_to,
                    },
                }


        # obj=self.env['invoice.report.wizard']
        pdf =self.env.ref('bi_pdf1.print_report_pdf').render_qweb_pdf(self, data=dataa)
        # b64=base64.b64encode(pdf[0])
        # obj._get_r eport_values(docids, data).with_context({'date_from': self.date_from, 'date_to':self.date_to()})
        pdfa=base64.b64encode(pdf[0])

        mail_template = self.env.ref('bi_emailtest1.email_template')

        attachment={
            'name': 'new',
            # 'datas': self.attach_file,
            'datas': pdfa,
            'res_model': 'bi.emailtest1',
            'type': 'binary'
        }

        id1 = self.env['ir.attachment'].create(attachment)
        mail_template.attachment_ids = [(6,0,[id1.id])]
        mail_template.send_mail(self.id, force_send=True)