#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class krs_detail(models.Model):

    _name = "vit.krs_detail"
    _description = "vit.krs_detail"
    name = fields.Char( required=True, string="Name",  help="")
    sks = fields.Float( string="Sks",  help="")
    nilai_huruf = fields.Char( string="Nilai huruf",  help="")
    nilai_bobot = fields.Float( string="Nilai bobot",  help="")
    nilai_total = fields.Float( string="Nilai total",  help="")


    mata_kuliah_id = fields.Many2one(comodel_name="vit.mata_kuliah",  string="Mata kuliah",  help="")
    dosen_id = fields.Many2one(comodel_name="hr.employee",  string="Dosen",  help="")
    krs_id = fields.Many2one(comodel_name="vit.krs",  string="Krs",  help="")
