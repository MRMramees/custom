#-*- coding: utf-8 -*-

from odoo import models, fields, api

class LabTestType(models.Model):
    _name = 'bi.lab.test.type'
    _description = 'bi_clinic.Lab.test.type'

    name = fields.Char(string="Test")
    code = fields.Char(string="Code")
    account_id = fields.Many2one('account.account',string='Account')
    # service_id = fields.Many2one('product.product', domain="[('type','=','service')]",string="Service")
    lab_test_type_line = fields.One2many('bi.lab.test.type.line','lab_test_type_id',string='Test Lines')

class LabTestTypeLines(models.Model):
    _name = 'bi.lab.test.type.line'
    _description = 'bi_clinic.Lab.Test.Type.Line'
    # sl_no = fields.Integer(string="Sl#") - to be done

    lab_test_type_id = fields.Many2one('bi.lab.test.type')
    # warning = fields.Boolean(string="Warning")
    # excluded = fields.Boolean(string="Excluded")
    name = fields.Char(string="Test")
    lower_limit = fields.Float(string="Lower Limit")
    upper_limit = fields.Float(string="Upper Limit")
    units = fields.Many2one('bi.lab.test.units',string="Units")
    test_rate = fields.Float(string="Rate")
    # remarks = fields.Char(string="Remarks")

    # @api.model
    # def create(self, values):
    #     res = super(LabTestTypeLines, self).create(values)
    #     return res

    # @api.multi
    # def write(self, values):
    #     res = super(LabTestTypeLines, self).write(values)
    #     return res



