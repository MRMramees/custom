from odoo import models, fields, api
import xlsxwriter

class PartnerXlsx(models.AbstractModel):
    _name = 'report.bi_test.studreport'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        if not data['form']["student_id"]:
            bistudents = self.env['bi.student'].search([])
            bold = workbook.add_format({'bold': True})
            italic = workbook.add_format({'italic':True})
            sheet = workbook.add_worksheet("student_report")
            sheet.write(0, 0, "Name", bold)
            sheet.write(0, 1, "English Mark", bold)
            sheet.write(0, 2, "Maths Mark", bold)
            sheet.write(0, 3, "Science Mark", bold)
            sheet.write(0, 4, "Total",bold)
            i = 1
            eng_mark=0
            math_mark=0
            sci_mark=0
            for obj in bistudents:
                # One sheet by partner
                sheet.write(i, 0, obj.name, bold)
                sheet.write(i, 1, obj.english_mark,italic)
                eng_mark += obj.english_mark
                sheet.write(i, 2, obj.maths_mark,italic)
                math_mark += obj.maths_mark
                sheet.write(i, 3, obj.science_mark,italic)
                sci_mark += obj.science_mark
                i+=1
            sheet.write(i, 0, "Total", bold)
            sheet.write(i, 1, eng_mark, bold)
            sheet.write(i, 2, math_mark, bold)
            sheet.write(i, 3, sci_mark,bold)
            
        else:
            for obj in partners:
            # One sheet by partner
                sheet = workbook.add_worksheet("student_report")
                bold = workbook.add_format({'bold': True})
                italic = workbook.add_format({'italic':True})
                sheet.write(0, 0, obj.student_id.name, bold)
                sheet.write(0, 1, obj.student_id.english_mark,italic)
                sheet.write(0, 2, obj.student_id.maths_mark,italic)
                sheet.write(0, 3, obj.student_id.science_mark,italic)
                tot_mark = obj.student_id.english_mark + obj.student_id.maths_mark + obj.student_id.science_mark
                sheet.write(0,4,tot_mark, bold)
    