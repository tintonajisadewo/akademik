#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class prodi(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"


    #ngisi kode prodi
    @api.onchange('fakultas_id')
    def _onchange_fakultas_id(self):
        if self.fakultas_id:
            self.kode_prodi = "{}.__".format( self.fakultas_id.kode_fakultas )

    #unik kode prodi
    #_sql_contraints