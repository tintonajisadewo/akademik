#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class mata_kuliah(models.Model):

    _name = "vit.mata_kuliah"
    _description = "vit.mata_kuliah"
    name = fields.Char( required=True, string="Name",  help="")
    sks = fields.Integer( string="Sks",  help="")
    kode_mata_kuliah = fields.Char( string="Kode mata kuliah",  help="")


