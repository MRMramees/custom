from odoo import fields, models, api

class DiseaseStatus(models.Model):
    _name = 'bi.disease.status'
    _description = 'bi_clinic.disease.status'

    name = fields.Char("Status")