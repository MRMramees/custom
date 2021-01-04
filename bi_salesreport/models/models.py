# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class bi_salesreport(models.Model):
#     _inherit = 'sale.order'


class TestReport(models.TransientModel):
    _name='test.order'

    # date_from = fields.Date(string='From date')
    # date_to = fields.Date(string='To date')


    def test_report(self):
        record_ids = self.env['sale.order'].search([
            ('state', '=','confirm'),
        ])
        for each in record:
            order.order_line.invoice_lines.move_id.filtered(lambda r: r.type in ('out_invoice', 'out_refund'))

        return self.env.ref('bi_salesreport.print_report_pdf').report_action(record_ids)

