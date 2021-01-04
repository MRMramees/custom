from odoo import fields, models, api

class PatientUrgencyLevel(models.Model):
    _name = 'bi.patient.urgency.level'
    _description = 'bi_clinic.patient_urgency_level'

    name = fields.Char("Urgency")