#!/usr/bin/python
#-*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class fakultas(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"


    # ngisi kode fak
    @api.onchange('perguruan_tinggi_id')
    def _onchange_perguruan_tinggi_id(self):
        if self.perguruan_tinggi_id:
            # urut = self.env['res.partner'].search_count([('perguruan_tinggi_id','=',self.perguruan_tinggi_id.id)]) + 1
            # self.kode_fakultas = "{}.{}".format(self.perguruan_tinggi_id.kode_pt, urut)
            self.kode_fakultas = "{}.___".format(self.perguruan_tinggi_id.kode_pt)