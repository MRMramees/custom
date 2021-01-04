#-*- coding: utf-8 -*-

from odoo import models, fields, api

class SalesXlsxWizard(models.TransientModel):
    _name = 'salesxlsx.wizard'
    _description = 'Sales Summary Excel Generation'
    
    fromdate = fields.Datetime(string='From Date')
    tilldate = fields.Datetime(string='To Date')

    def show(self):
        context = self._context
        datas = {'ids':context.get('active_ids',[])}
        datas['model'] = 'salesxlsx.wizard'
        datas['form'] = self.read()[0]
        return self.env.ref('bi_test.salessummary').report_action(self, data=datas, config=False)