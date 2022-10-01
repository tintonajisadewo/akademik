#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class perguruan_tinggi(models.Model):

    _name = "res.partner"
    _description = "res.partner"

    _inherit = "res.partner"
    kode_pt = fields.Char( string="Kode pt",  help="")
    akreditasi_pt = fields.Char( string="Akreditasi pt",  help="")
    tanggal_berdiri = fields.Date( string="Tanggal berdiri",  help="")
    nomor_sk_pt = fields.Char( string="Nomor sk pt",  help="")
    tanggal_sk_pt = fields.Date( string="Tanggal sk pt",  help="")


    rektor_id = fields.Many2one(comodel_name="hr.employee",  string="Rektor",  help="")
    wakil_rektor_1_id = fields.Many2one(comodel_name="hr.employee",  string="Wakil rektor 1",  help="")
    wakil_rektor_2_id = fields.Many2one(comodel_name="hr.employee",  string="Wakil rektor 2",  help="")
