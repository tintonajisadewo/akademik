#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class tahun_ajaran(models.Model):

    _name = "vit.tahun_ajaran"
    _description = "vit.tahun_ajaran"
    name = fields.Char( required=True, string="Name",  help="")


