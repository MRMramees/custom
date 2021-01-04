from odoo import models, fields, api

class GenericRisks(models.Model):
    _name = 'bi.medical.specialities'
    _description = 'bi_clinic.medical.specialities'

    code = fields.Char(string='Code')
    name = fields.Char(string='Description')