from odoo import fields, models, api

class MedicamentDoseUnits(models.Model):
    _name = 'bi.medicament.dose.units'
    _description = 'bi_clinic.medicament.dose.units'

    name = fields.Char(string='Unit')
    description = fields.Char(string='Description', required=True)