#-*- coding: utf-8 -*-

from odoo import models, fields, api

class LabTestUnits(models.Model):
    _name = 'bi.lab.test.units'
    _description = 'bi_clinic.Lab.test.units'
    _rec_name = 'code'

    unit = fields.Char(string="Unit")
    code = fields.Char(string="Code")

