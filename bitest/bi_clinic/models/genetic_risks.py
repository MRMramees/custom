import string
from odoo import models, fields, api

class GeneticRisks(models.Model):
    _name = 'bi.genetic.risks'
    _description = 'bi_clinic.genetic.risks'

    official_symbol = fields.Char(string='Official Symbol')
    name = fields.Char(string='Official Long Name')
    affected_chromosome = fields.Integer(string='Affected Chromosome')
    dominance = fields.Char(string='Dominance')