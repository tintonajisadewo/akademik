#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class mahasiswa(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"

    # NIM
    @api.onchange('prodi_id')
    def _onchange_prodi_id(self):
        urutan = "____"
        self.nim = "{}.{}".format( self.prodi_id.kode_prodi, urutan )