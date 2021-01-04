from odoo import fields, models, api

class Appointment(models.Model):
    _name = 'bi.appointments'
    _description = 'bi_clinic.appointments'
    _rec_name = 'appointment_no'

    appointment_no = fields.Char(string="Appointment ID", required=True, readonly=True,
                        index=True,copy=False, default='New')
    patient_info_id = fields.Many2one('bi.patient.info',"Patient")
    patient_status_id = fields.Many2one('bi.patient.status',string="Patient Status")
    urgency_level_id = fields.Many2one('bi.patient.urgency.level',string="Urgency Level")
    appointment_start_date = fields.Date(string="Appointment Start") 
    appointment_end_date = fields.Date(string="Appointment End")
    physician_info_id = fields.Many2one('bi.physician.info',string="Physician")
    speciality_id = fields.Many2one('bi.speciality',string="Speciality")
    status_id = fields.Many2one('bi.appointment.status',string="Status")
    invoice_excempt = fields.Boolean(string="Invoice Excempt")
    validity_date = fields.Date(string="Validity Date")
    consultation_service_id = fields.Many2one('bi.speciality',string="Consultation Service")

    @api.model
    def create(self, vals):
        if vals.get('appointment_no', 'New') == 'New':
            vals['appointment_no'] = self.env['ir.sequence'].next_by_code('bi.clinic.prescription.sequence') or 'New'
            result = super(Appointment,self).create(vals)
            return result
    