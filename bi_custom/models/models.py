# -*- coding: utf-8 -*-

from odoo import _, api, fields, models

class BiCustom(models.Model):
    _name = 'bi.custom'
    _description = 'description'

    name = fields.Char(string='Name')
    roll_no = fields.Integer(string='Roll No')
    

