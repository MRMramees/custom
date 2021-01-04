#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class bi_test(models.Model):
    _name = 'bi.student'
    _description = 'bi_test.bi_test'

    name = fields.Char(string="Student Name")
    age = fields.Integer()
    english_mark = fields.Integer()
    maths_mark = fields.Integer()
    science_mark = fields.Integer()
    start_date = fields.Date(string="Start Date", store=True, )
    desc = fields.Text()
    total_marks = fields.Float(compute="calc_total", store=True)
    avg_mark = fields.Float(compute="calc_total", store=True)
    instructor_id = fields.Many2one('bi.instructor', string='Instructor')
    test_boolean = fields.Boolean(string='Test', default=False)
 
    _sql_constraints = [
        ('english_maths_notsame','CHECK(english_mark != maths_mark)',
        "Maths and Science Marks should not same"),

        ('name_unique','UNIQUE(name)',
        "Name should be unique")
    ]

    @api.depends('english_mark','maths_mark','science_mark')
    def calc_total(self):
        for record in self:
            record.total_marks = float(record.english_mark) + float(record.maths_mark) + float(record.science_mark)
            record.avg_mark = (float(record.english_mark) + float(record.maths_mark) + float(record.science_mark))

    @api.onchange('english_mark')
    def onchange_marks(self):
        if self.english_mark > 100 or self.maths_mark > 100 or self.science_mark > 100:
            return {
                'warning': {
                    'title': "Incorrect Marks",
                    'message': "Marks can't be more than 100",
                },
            }

    @api.constrains('english_mark','maths_mark','science_mark')
    def check_maths_above_100(self):
        for record in self:
            if record.maths_mark > 100 or record.english_mark > 100 or record.science_mark > 100:
                raise ValidationError("Marks should be less than 100")
