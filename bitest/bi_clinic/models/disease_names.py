#-*- coding: utf-8 -*-

from odoo import models, fields, api

class DiseaseNames(models.Model):
    _name = 'bi.disease.names'
    _description = 'bi_clinic.Disease.Names'

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    disease_sub_category = fields.Many2one('bi.disease.sub.category',
        ondelete='set null',string="Disease Sub Category")

