#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class jenjang(models.Model):

    _name = "vit.jenjang"
    _description = "vit.jenjang"
    name = fields.Char( required=True, string="Name",  help="")


