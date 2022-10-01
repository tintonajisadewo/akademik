#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class dosen(models.Model):

    _name = "hr.employee"
    _description = "hr.employee"

    _inherit = "hr.employee"
    kode_dosen = fields.Char( string="Kode dosen",  help="")
    nidn = fields.Char( string="Nidn",  help="")
    status_ikatan_kerja = fields.Char( string="Status ikatan kerja",  help="")
    status_aktivitas = fields.Char( string="Status aktivitas",  help="")
    is_dosen = fields.Boolean( string="Is dosen",  help="")


    perguruan_tinggi_id = fields.Many2one(comodel_name="res.partner",  string="Perguruan tinggi",  help="")
    fakultas_id = fields.Many2one(comodel_name="res.partner",  string="Fakultas",  help="")
    prodi_id = fields.Many2one(comodel_name="res.partner",  string="Prodi",  help="")
    jabatan_fungsional_id = fields.Many2one(comodel_name="vit.jabatan_fungsional",  string="Jabatan fungsional",  help="")
    pendidikan_tertinggi_id = fields.Many2one(comodel_name="vit.jenjang",  string="Pendidikan tertinggi",  help="")
    riwayat_mengajar_ids = fields.One2many(comodel_name="vit.riwayat_mengajar",  inverse_name="dosen_id",  string="Riwayat mengajar",  help="")
    riwayat_pendidikan_ids = fields.One2many(comodel_name="vit.riwayat_pendidikan",  inverse_name="dosen_id",  string="Riwayat pendidikan",  help="")
