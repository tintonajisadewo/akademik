#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class riwayat_pendidikan(models.Model):

    _name = "vit.riwayat_pendidikan"
    _description = "vit.riwayat_pendidikan"
    name = fields.Char( required=True, string="Name",  help="")
    gelar_akademik = fields.Char( string="Gelar akademik",  help="")
    tanggal_ijasah = fields.Date( string="Tanggal ijasah",  help="")


    perguruan_tinggi_id = fields.Many2one(comodel_name="res.partner",  string="Perguruan tinggi",  help="")
    jenjang_id = fields.Many2one(comodel_name="vit.jenjang",  string="Jenjang",  help="")
    dosen_id = fields.Many2one(comodel_name="hr.employee",  string="Dosen",  help="")
