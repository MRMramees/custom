#-*- coding: utf-8 -*-

from odoo import models, fields, api

class DiseaseMainCategory(models.Model):
    _name = 'bi.disease.main.category'
    _description = 'bi_clinic.Disease.Main.Category'

    name = fields.Char(string="Name")
