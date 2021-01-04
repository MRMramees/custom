from odoo import fields, models, api

class PatientDisease(models.Model):
    _name = 'bi.patient.disease'
    _description = 'bi_clinic.patient.disease'

    patient_info_id = fields.Many2one('bi.patient.info',string="Patient")
    disease_id = fields.Many2one('bi.disease.names', string='Disease', required=True)
    severity_id = fields.Many2one('bi.disease.severity', string='Severity')
    disease_status_id = fields.Many2one('bi.disease.status',string='Status')
    infectious_disease = fields.Boolean(string='Infectious')
    active_disease = fields.Boolean(string='Active disease', default=True)
    remarks = fields.Char(string='Remarks')
    diagnosis_date = fields.Date(string='Diagnosis Date')
    healed_date = fields.Date(string='Healed Date')
    diagnosed_age = fields.Integer(string='Age when Diagnoses')
    physician_info_id = fields.Many2one('bi.physician.info',string='Physician')
    allergic_disease=fields.Boolean(string='Allergic Disease')
    allergic_type_id =fields.Many2one('bi.allergy.type',string='Allergy Type')
    pregnancy_warning = fields.Boolean(string='Pregnancy warning')
    contract_pregnancy_week = fields.Integer(string='Contracted in pregnancy week#')
    on_treatment = fields.Boolean(string='On Treatement')
    treatment_desc = fields.Char(string='Treatment Description')
    treatment_start_date = fields.Date(string='Start of treatment')
    treatment_end_date = fields.Date(string='End of treatment')
    extra_info = fields.Text(string="Extra Info")
    # 'code' need to understand the purpose and complete.



