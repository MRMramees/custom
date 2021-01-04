# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bi_asd(models.Model):
     _name = 'bi.asd'
     _description = 'bi_asd.bi_asd'

     name = fields.Char()
     age = fields.Integer()
     a = fields.Binary()
     a1 = fields.Integer()
     a3 = fields.Html()
     description = fields.Text()
     a4 = fields.Integer()
     a7 = fields.Many2one('bi.asd1')
     a8 = fields.Many2many('comodel_name', string='')
     
class bi_asd1(models.Model):
     _name = 'bi.asd1'
     _description = 'bi_asd1.bi_asd1'
          
     a5 = fields.Many2one('bi.asd')
     a6 = fields.One2many('bi.asd', 'a7')
