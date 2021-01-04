from odoo import fields, models, api

class MedicamentAdminRoutes(models.Model):
    _name = 'bi.medicament.admin.routes'
    _description = 'bi_clinic.medicament.admin.routes'

    code = fields.Char(string='Code')
    name = fields.Char(string='Route', required=True)