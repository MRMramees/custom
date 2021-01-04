from odoo import fields, models, api

class DiseaseSeverity(models.Model):
    _name = 'bi.disease.severity'
    _description = 'bi_clinic.disease.severity'

    name = fields.Char("Severity")