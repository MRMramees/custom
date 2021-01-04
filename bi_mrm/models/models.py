# -*- coding: utf-8 -*-
from odoo import models, fields, api



class bi_mrm(models.Model):
        _name = 'bi.mrm'
        _description = 'bi_mrm.bi_mrm'

        name = fields.Char(string='name')
        age = fields.Integer(string='age')
        value2 = fields.Float(compute="_value_pc", store=True)
        description = fields.Text()
        abc= fields.Many2one('bi.mrm1')
        percent = fields.Selection([('key','value'),('k1','value1')], string='')
        vard = fields.Selection([('key','value2'),('k3','value4')], string='')
        salary1 = fields.Float(string='')
        age1 = fields.Integer(string='') 
       

#button
        state = fields.Selection([('draft', 'Draft'), ('done', 'Done'),
   ('cancel', 'Cancelled'), ], required=True, default='draft')

        def button_done(self):
            for rec in self:
                rec.write({'state': 'done'})
                
        def button_reset(self):
            for rec in self:
                rec.state= 'draft'

        def button_cancel(self):
            for rec in self:
                rec.write({'state': 'cancel'})

#method

        def createa(self):
            for rec in self:
                vals={"salary2":self.salary1,"age2":self.age1}
                self.env['bi.mrm1'].create(vals)

#write fun


        def writeb(self):
            record_ids = self.env['bi.mrm'].search([('name','=','ram')])
            for record in record_ids:
                record.write({
                    'salary1' : 100,
                    'age1' : 30,
                })



#many to one
class bi_mrm1(models.Model):
        _name = 'bi.mrm1'
        _description = 'bi_mrm.bi_mrm'

        new = fields.Many2one('bi.mrm')
        fresh = fields.One2many('bi.mrm', 'abc',)
        

        deg = fields.Many2many('bi.mrm',string="")
        salary2 = fields.Float(string='')
        age2 = fields.Integer(string='') 
       

