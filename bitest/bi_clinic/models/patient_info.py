#-*- coding: utf-8 -*-

from datetime import datetime

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class PatientInfo(models.Model):
    _name = 'bi.patient.info'
    _description = 'bi_clinic.patient.information'
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('res.partner',string="Name")
    patient_no = fields.Char(string="Patient ID", required=True, readonly=True,
                        index=True,copy=False, default='New')
    date_of_birth = fields.Date(string="Date Of Birth")
    age = fields.Char(compute='calc_age', string="Age")
    blood_group = fields.Many2one('bi.blood.groups', on_delete='set null', string="Blood Group")
    # blood_group = fields.Char(string="Blood Group")
    gender = fields.Selection([('male','Male'),('female','Female')],string='Gender')
    disease_lines = fields.One2many('bi.patient.disease','patient_info_id', string="Patient")
    medicament_lines = fields.One2many('bi.patient.medicament','patient_info_id',string='Medicaments')
    appointment_lines = fields.One2many('bi.appointments','patient_info_id',string='Appointments')

    @api.depends('date_of_birth')
    def calc_age(self):
        for rec in self:
            date_diff = relativedelta(datetime.today(),rec.date_of_birth)
            rec.age = str(date_diff.years) + 'y ' + str(date_diff.months) + 'm ' + str(date_diff.days) + 'd'
    
    @api.model
    def create(self, vals):
        if vals.get('patient_no', 'New') == 'New':
            vals['patient_no'] = self.env['ir.sequence'].next_by_code('bi.clinic.patient.sequence') or 'New'
            result = super(PatientInfo,self).create(vals)
            return result