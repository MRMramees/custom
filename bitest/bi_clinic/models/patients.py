#-*- coding: utf-8 -*-

from copy import copy
from datetime import datetime, timedelta
from email.policy import default
import string
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api

class Patients(models.Model):
    # _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'bi_clinic.res.partner.inherit'

    is_doctor = fields.Boolean(string='Is Doctor')
    