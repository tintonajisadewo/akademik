#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class jabatan_fungsional(models.Model):

    _name = "vit.jabatan_fungsional"
    _description = "vit.jabatan_fungsional"
    name = fields.Char( required=True, string="Name",  help="")


