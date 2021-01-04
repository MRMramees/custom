from odoo import models, fields, api

class ProductBatch(models.Model):
    _name = "product.batch"
    _description = "Product batches and expiry"

    product_id = fields.Many2one('product.product', string='Product')
    batch_no = fields.Char('Batch No')
    expiry_date = fields.Date('Expiry Date')

class ProductProduct(models.Model):
    _inherit = "product.product"

    batch_ids = fields.One2many('product.batch', 'product_id', string='Batch')

