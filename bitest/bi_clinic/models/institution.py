from odoo import fields, models, api

class PatientMedicament(models.Model):
    _name = 'bi.institution'
    _description = 'bi_clinic.institution'

    name = fields.Char(string="Institution")
