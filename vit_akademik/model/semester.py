#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class semester(models.Model):

    _name = "vit.semester"
    _description = "vit.semester"
    name = fields.Char( required=True, string="Name",  help="")


    tahun_ajaran_id = fields.Many2one(comodel_name="vit.tahun_ajaran",  string="Tahun ajaran",  help="")
