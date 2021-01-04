from email.policy import default
from odoo import models, fields, api

class Patients(models.Model):
    _name = 'bi.occupation'
    _description = 'bi_clinic.occupation'

    code = fields.Integer(string='Code', required=True, readonly=True)
    name = fields.Char(string='Occupation', required=True)