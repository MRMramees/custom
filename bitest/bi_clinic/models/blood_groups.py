import string
from unicodedata import name
from odoo import models, fields, api

class Patients(models.Model):
    _name = 'bi.blood.groups'
    _description = 'bi_clinic.blood.groups'
    
    name = fields.Char(required=True, string='Blood Group')