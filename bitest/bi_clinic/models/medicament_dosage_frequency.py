from odoo import fields, models, api

class MedicamentAdminRoutes(models.Model):
    _name = 'bi.medicament.dosage.frequency'
    _description = 'bi_clinic.medicament.dosage.frequency'

    code = fields.Char(string='Code')
    name = fields.Char(string='Frequency', required=True)
    abbreviation = fields.Char(string='Abbreviation')