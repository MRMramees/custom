from odoo import fields, models, api

class PatientMedicament(models.Model):
    _name = 'bi.patient.medicament'
    _description = 'bi_clinic.patient.medicament'

    patient_info_id = fields.Many2one('bi.patient.info',string="Patient")
    medicament_id = fields.Many2one('product.template',string="Medicament")
    physician_info_id = fields.Many2one('bi.physician.info',string="Physician")
    active = fields.Boolean(string="Active")
    indication_id = fields.Many2one('bi.patient.medicament.indication',string="Indication") #..need to clarify the purpose / function
    treatment_start_date = fields.Date(string="Treatment Start Date")
    treatment_end_date = fields.Date(string="Treatment End Date")
    course_completed = fields.Boolean(string="Course Completed")
    discontinued = fields.Boolean(string="Discontinued")
    medicament_form_id = fields.Many2one('bi.medicament.form',string="Form")
    admin_route_id = fields.Many2one('bi.medicament.admin.routes',string="Administration Route")
    dose = fields.Float(string="Dose")
    dose_unit_id = fields.Many2one('bi.medicament.dose.units',string="Dose Unit")
    treatment_duration = fields.Integer(string="Treatment Duration")
    treatment_period = fields.Selection(selection=[('hours','Hours'),('days','Days'),('months','Months'),('years','Years')],string="Treatment Period")
    common_dosage_frequency_id = fields.Many2one('bi.medicament.dosage.frequency',string="Common Dosage Frequency") # need to clarify the purpose / function
    admin_hours = fields.Char(string="Admin hours")
    specific_dosage_frequency_id = fields.Many2one('bi.medicament.dosage.frequency',string="Specific Dosage Frequency") # need to clarify the purpose / function
    unit = fields.Char(string="Unit")
    notes = fields.Text(string="Notes")