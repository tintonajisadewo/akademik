#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class dosen(models.Model):
    _name = "hr.employee"
    _inherit = "hr.employee"
