from odoo import fields, models, api

class MedicamentCategory(models.Model):
    _name = 'bi.medicament.category'
    _description = 'bi_clinic.medicament.category'

    name = fields.Char(string='Category Name', required=True)