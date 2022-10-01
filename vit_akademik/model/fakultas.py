#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class fakultas(models.Model):

    _name = "res.partner"
    _description = "res.partner"
    kode_fakultas = fields.Char( string="Kode fakultas",  help="")

    _inherit = "res.partner"


    perguruan_tinggi_id = fields.Many2one(comodel_name="res.partner",  string="Perguruan tinggi",  help="")
    dekan_id = fields.Many2one(comodel_name="hr.employee",  string="Dekan",  help="")
    prodi_ids = fields.One2many(comodel_name="res.partner",  inverse_name="fakultas_id",  string="Prodi",  help="")
