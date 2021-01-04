#-*- coding: utf-8 -*-

from odoo import models, fields, api

class DiseaseSubCategory(models.Model):
    _name = 'bi.disease.sub.category'
    _description = 'bi_clinic.Disease.Sub.Category'

    name = fields.Char(string="Name")
    disease_main_category = fields.Many2one('bi.disease.main.category',
        ondelete='set null',string="Disease Main Category")
