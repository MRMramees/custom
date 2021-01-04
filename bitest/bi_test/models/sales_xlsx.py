#-*- coding: utf-8 -*-

from odoo import models, fields, api
import xlsxwriter

class SalesSummaryXlsx(models.AbstractModel):
    _name = 'report.bi_test.salessummary'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        print(data)
        # '|',('date_order'