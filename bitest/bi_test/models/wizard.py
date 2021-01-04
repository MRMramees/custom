from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'school.wizard'
    _description = "Wizard: Registration"


    student_id = fields.Many2one('bi.student', string='Student Name')


    def print(self):
        context = self._context
        datas = {'ids': context.get('active_ids', [])}
        datas['model'] = 'school.wizard'
        datas['form'] = self.read()[0]
        # if datas.
        return self.env.ref('bi_test.studreport').report_action(self, data=datas, config=False)
        
        # report = self.env['ir.actions.report']._get_report_from_name('report.bi_test.studreport')
        # report.sudo().report_file= str('STUDENT REPORT')
        # return self.env.ref('report.bi_test.studreport').report_action(self,data=datas,config=False)