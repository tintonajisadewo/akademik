#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class mahasiswa(models.Model):

    _name = "res.partner"
    _description = "res.partner"

    _inherit = "res.partner"
    nim = fields.Char( string="Nim",  help="")


    prodi_id = fields.Many2one(comodel_name="res.partner",  string="Prodi",  help="")
