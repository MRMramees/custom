# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMoveLab(models.Model):
    _inherit = 'account.move'

    lab_request_id = fields.Many2one('bi.lab.test.requests',store=False, string='Lab Request No:')

    @api.onchange('lab_request_id')
    def _onchange_lab_request_id(self):

        if not self.lab_request_id:
            return
        
        req_lines = self.lab_request_id.lab_test_request_line
        new_lines = self.env['account.move.line']
        for line in req_lines:
            new_line = new_lines.new(line._prepare_account_move_line(self)) 
            new_line.account_id = new_line._get_computed_account()
            new_line._onchange_price_subtotal()
            new_lines += new_line
        new_lines._onchange_mark_recompute_taxes()