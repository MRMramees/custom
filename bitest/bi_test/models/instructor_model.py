#-*- coding: utf-8 -*-

from odoo import models, fields, api
        
class Instructor(models.Model):
    _name = 'bi.instructor'
    _description = 'bi_test.Instructor'

    name = fields.Char(string="Instructor")
    age = fields.Integer()
    place = fields.Char(string="Place")

    