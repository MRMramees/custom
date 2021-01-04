

from odoo import models, fields, api
from odoo.tools.misc import xlwt
from odoo.exceptions import UserError, AccessError
import io
import base64
from PIL import Image
import itertools
import time
from datetime import datetime,timedelta,date
import xlsxwriter


class REPORT5Xlsx(models.AbstractModel):
    _name = 'report.bi_pdf1.report_sale_docs'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        worksheet = workbook.add_worksheet("INVOICE REPORT 1")
        format1 = workbook.add_format({'font_size': 14, 'bottom': True, 'right': True, 'left': True, 'top': True,
                                       'align': 'center', 'bold': True})
        format12 = workbook.add_format(
            {'font_size': 16, 'align': 'center', 'right': True, 'left': True, 'bottom': False,
             'top': True, 'bold': True,})
        format3 = workbook.add_format({'bold':True,'bottom': True, 'top': True, 'font_size': 12,'align': 'center'})
        font_size_8 = workbook.add_format({'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 8})
        justify = workbook.add_format({'bottom': True, 'top': True, 'right': True, 'left': True, 'font_size': 12,'bold':True,'align':'center'})
        format3.set_align('center')
        font_size_8.set_align('center')
        justify.set_align('justify')
        format1.set_align('center')
        boldc = workbook.add_format({'bold':True,'align':'center'})
        center = workbook.add_format({'align':'center'})

        # filter_row = 3
        # filter_row1 = 5
        # if data['form']['date_from']:
        #     date_from = datetime.strptime(data['form']['date_from'], '%Y-%m-%d').date()
        #     worksheet.write('A%s' % filter_row, 'Date From', boldc)
        #     worksheet.write('B%s' % filter_row, str(date_from.strftime("%d-%m-%Y")), boldc)
        # if data['form']['date_to']:
        #     date_to = datetime.strptime(data['form']['date_to'], '%Y-%m-%d').date()
        #     worksheet.write('D%s' % filter_row, 'Date To', boldc)
        #     worksheet.write('E%s' % filter_row, str(date_to.strftime("%d-%m-%Y")), boldc)
            
        row = 6
        new_row = row + 1
        worksheet.set_column('A:A', 20)
        worksheet.set_column('B:B', 25)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 25)
        worksheet.set_column('F:F', 20)
        worksheet.set_column('G:G', 25)
        worksheet.set_column('H:H', 25)
        worksheet.set_column('I:I', 25)
        worksheet.set_column('J:J', 25)
        worksheet.set_column('K:K', 25)
       

        worksheet.merge_range('A1:E1', 'INVOICING REPORT', format3)
        worksheet.write('A%s' % row, 'SL NO', format3)
        worksheet.write('B%s' % row, 'NUMBER', format3)
        worksheet.write('C%s' % row, 'CUSTOMER', format3)
        worksheet.write('D%s' % row, 'INVOICE DATE', format3)
        # worksheet.write('E%s' % row, 'SOURCE DOCUMENT', format3)
        # worksheet.write('F%s' % row, 'SALES PERSON', format3)
        worksheet.write('E%s' % row, 'DUE DATE', format3)
        worksheet.write('F%s' % row, 'TAX EXCLUDED', format3)
        worksheet.write('G%s' % row, 'TOTAL', format3)
        worksheet.write('H%s' % row, 'AMOUNT DUE', format3)
        worksheet.write('I%s' % row, 'STATUS', format3)
        worksheet.write('J%s' % row, 'PAYMENT', format3)
        domain =[]
       
        # if data['form']['date_from']:
        #     domain.append(('invoice_date', '>=', data['form']['date_from']))
        # if data['form']['date_to']:
        #     domain.append(('invoice_date', '<=', data['form']['date_to']))

        # date_from = data['form']['date_from']
        # date_to = data['form']['date_to']


        date_from = '11/01/2020'
        date_to = date.today()

        self.env.cr.execute("""select * from account_move 
                                                 where invoice_date 
                                                 between  '"""+str(date_from)+ """' 
                                                 AND '"""+str(date_to)+"""' """)
        values = self.env.cr.dictfetchall()
         
               
        sl_no = 1
        record = self.env['account.move'].search(domain)
        # val = []
    
        for each in values :
           
            worksheet.write('A%s' % new_row, sl_no, center)
            worksheet.write('B%s' % new_row, each['name'])
            worksheet.write('C%s' % new_row, each['invoice_partner_display_name'])
            worksheet.write('D%s' % new_row, each['invoice_date'], center)
            # worksheet.write('E%s' % new_row, each.invoice_origin)
            # worksheet.write('F%s' % new_row, each.invoice_user_id.name)
            worksheet.write('E%s' % new_row, each['invoice_date_due'], center)
            worksheet.write('F%s' % new_row, each['amount_untaxed_signed'])
            worksheet.write('G%s' % new_row, each['amount_total_signed'])
            worksheet.write('H%s' % new_row, each['amount_residual_signed'])
            worksheet.write('I%s' % new_row, each['state'])
            worksheet.write('J%s' % new_row, each['invoice_payment_state'])



            # new_row = new_row + 1
            # worksheet.write('B%s' % new_row, 'quantity',center)
            # worksheet.write('C%s' % new_row, 'product',center)
            # worksheet.write('D%s' % new_row, 'price',center)
            # for k in each.invoice_line_ids:
            #     new_row = new_row + 1
            #     worksheet.write('B%s' % new_row, k.quantity)
            #     # new_row+=1
            #     worksheet.write('C%s' % new_row, k.name)
            #     worksheet.write('D%s' % new_row, k.price_unit)   
            
                   
            new_row+=1
            sl_no+=1