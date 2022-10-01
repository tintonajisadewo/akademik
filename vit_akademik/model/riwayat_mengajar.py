#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class riwayat_mengajar(models.Model):

    _name = "vit.riwayat_mengajar"
    _description = "vit.riwayat_mengajar"
    name = fields.Char( required=True, string="Name",  help="")
    kode_mata_kuliah = fields.Char( string="Kode mata kuliah",  help="")


    dosen_id = fields.Many2one(comodel_name="hr.employee",  string="Dosen",  help="")
    semester_id = fields.Many2one(comodel_name="vit.semester",  string="Semester",  help="")
    mata_kuliah_id = fields.Many2one(comodel_name="vit.mata_kuliah",  string="Mata kuliah",  help="")
    kelas_id = fields.Many2one(comodel_name="vit.kelas",  string="Kelas",  help="")
