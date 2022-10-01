#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class prodi(models.Model):

    _name = "res.partner"
    _description = "res.partner"

    _inherit = "res.partner"
    kode_prodi = fields.Char( string="Kode prodi",  help="")
    status = fields.Boolean( string="Status",  help="")
    jenjang = fields.Char( string="Jenjang",  help="")
    akreditasi_prodi = fields.Char( string="Akreditasi prodi",  help="")
    tanggal_berdiri = fields.Date( string="Tanggal berdiri",  help="")
    sk_penyelenggaraan = fields.Char( string="Sk penyelenggaraan",  help="")
    tanggal_sk = fields.Date( string="Tanggal sk",  help="")
    visi_prodi = fields.Text( string="Visi prodi",  help="")
    misi_prodi = fields.Text( string="Misi prodi",  help="")
    deskripsi_prodi = fields.Text( string="Deskripsi prodi",  help="")


    mahasiswa_ids = fields.One2many(comodel_name="res.partner",  inverse_name="prodi_id",  string="Mahasiswa",  help="")
    fakultas_id = fields.Many2one(comodel_name="res.partner",  string="Fakultas",  help="")
    jenjang_id = fields.Many2one(comodel_name="vit.jenjang",  string="Jenjang",  help="")
    kepala_prodi_id = fields.Many2one(comodel_name="hr.employee",  string="Kepala prodi",  help="")
    dosen_home_base_ids = fields.One2many(comodel_name="hr.employee",  inverse_name="prodi_id",  string="Dosen home base",  help="")
