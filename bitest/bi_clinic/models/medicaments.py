from odoo import fields, models, api

class Medicaments(models.Model):
    _inherit = 'product.template'


    active_component = fields.Char(string="Active Component")
    category = fields.Many2one('bi.medicament.category',string="Category")
    # qty_available = fields.Integer(string="Available Quantity")
    therapeutic_effect = fields.Char(string="Therapeutic effect")
    pregnancy_warning = fields.Boolean(string="Pregnancy Warning")