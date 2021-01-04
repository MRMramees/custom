from odoo import fields, models, api

class LabTestRequests(models.Model):
    _name = 'bi.prescription'
    _description = 'bi_clinic.prescription'
    _rec_name = 'prescription_no'

    prescription_no = fields.Char(string="Prescription No:",readonly=True, index=True,copy=False, default='New')
    date_prescription = fields.Date(string = "Prescription Date")
    patient_info_id = fields.Many2one('bi.patient.info',string="Patient")
    physician_info_id = fields.Many2one('bi.physician.info',string="Doctor")
    medicament_lines = fields.One2many('bi.patient.medicament','patient_info_id',string='Medicaments')

    @api.model
    def create(self, vals):
        if vals.get('prescription_no', 'New') == 'New':
            vals['prescription_no'] = self.env['ir.sequence'].next_by_code('bi.clinic.appointment.sequence') or 'New'
            result = super(LabTestRequests,self).create(vals)
            return result
    