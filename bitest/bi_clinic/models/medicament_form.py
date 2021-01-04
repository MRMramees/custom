#-*- coding: utf-8 -*-

from odoo import models, fields, api

class MedicamentForm(models.Model):
    _name = 'bi.medicament.form'
    _description = 'bi_clinic.medicament.form'

    code = fields.Char(string="Code")
    name = fields.Char(string="Form", required=True)
