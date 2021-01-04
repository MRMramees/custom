from odoo import fields, models, api

class AppointmentStatus(models.Model):
    _name = 'bi.appointment.status'
    _description = 'bi_clinic.appointment_status'

    name = fields.Char("Appointment Status")