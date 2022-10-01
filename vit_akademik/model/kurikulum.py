#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class kurikulum(models.Model):

    _name = "vit.kurikulum"
    _description = "vit.kurikulum"
    name = fields.Char( required=True, string="Name",  help="")


    tahun_ajaran_id = fields.Many2one(comodel_name="vit.tahun_ajaran",  string="Tahun ajaran",  help="")
