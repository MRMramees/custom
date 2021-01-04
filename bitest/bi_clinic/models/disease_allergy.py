from odoo import fields, models, api

class AllergyType(models.Model):
    _name = 'bi.allergy.type'
    _description = 'bi_clinic.allergy.type'

    name = fields.Char("Allergy Type")