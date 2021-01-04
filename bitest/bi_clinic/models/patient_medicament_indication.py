from odoo import fields, models, api

class PatientMedicament(models.Model):
    _name = 'bi.patient.medicament.indication'
    _description = 'bi_clinic.patient.medicament.indication'

    name= fields.Char(string='Indication')