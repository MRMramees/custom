#this file created for building report. but not used so kept reduntant

from odoo import api, fields, models

# _logger = logging.getLogger(__name__)


class LabTestReport(models.Model):
    _inherit = 'bi.lab.test.requests'

    def lab_test_result_report(self):
        # print(self.request_no)
        doc = []
        for line in self.env['bi.lab.test.request.type'].search([('test_request_id','=',self.request_no)]):
            vals = {
                'test_name':line.test_type_id.name,
                'test_type': line.test_request_type_line_id.name,
                'upper_limit':line.test_request_type_line_id.upper_limit,
                'lower_limit':line.test_request_type_line_id.lower_limit,
                'test_result':line.test_result
            }
            doc.append(vals)    


        return {
           'lines': doc
        }
    # for line in self.env['bi.lab.test.requests']


