from odoo import fields, models, api

class PatientStatus(models.Model):
    _name = 'bi.patient.status'
    _description = 'bi_clinic.patient_status'

    name = fields.Char("Status")