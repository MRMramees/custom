# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date, timedelta


class bi_duplicate(models.Model):
    _name = 'bi.duplicate'
    _description = 'bi_duplicate'


    source_document = fields.Reference(selection='_select_target_model', string="Source Document")
    count = fields.Integer(string='')
    intervel = fields.Selection([('daily', 'Daily'), ('weekly', 'Weekly'), ('monthly', 'Monthly')],  default='daily')
    i = fields.Integer(string='', default = 0)
    now = fields.Date(string='', default=0)

    @api.model
    def _select_target_model(self):   
        models = self.env['ir.model'].search([])
        return [(model.model, model.name) for model in models]

    def goo(self):
        rec = self.env['bi.duplicate'].search([],order='id desc')[0]
        record = rec.source_document._name
        if rec.i < rec.count:
            if rec.intervel == 'daily':
                self.env[record].browse(rec.source_document.id).copy(default={'id':rec.source_document.id})
                rec.i+=1
                rec.now+=timedelta(days=1)

            if rec.intervel == 'weekly':
                self.env[record].browse(rec.source_document.id).copy(default={'id':rec.source_document.id})
                rec.i+=1
                rec.now+=timedelta(days=7)
            
            if rec.intervel == 'monthly':
                self.env[record].browse(rec.source_document.id).copy(default={'id':rec.source_document.id})
                rec.i+=1
                rec.now+=timedelta(days=30)

