#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class kelas(models.Model):

    _name = "vit.kelas"
    _description = "vit.kelas"
    name = fields.Char( required=True, string="Name",  help="")
    kode_kelas = fields.Char( string="Kode kelas",  help="")


