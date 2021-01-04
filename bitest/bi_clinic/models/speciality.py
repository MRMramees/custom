from odoo import fields, models, api

class PatientMedicament(models.Model):
    _name = 'bi.speciality'
    _description = 'bi_clinic.speciality'

    name=fields.Char(string="Speciality")
