#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','Aktiv'),('done','Selesai')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning
import time

class krs(models.Model):
    _name = "vit.krs"
    _inherit = "vit.krs"

    @api.model
    def create(self, vals):
        return super(krs, self).create(vals)

    def action_confirm(self):
        self.state = STATES[1][0]

    def action_done(self):
        self.state = STATES[2][0]

    def action_draft(self):
        self.state = STATES[0][0]

    def unlink(self):
        for me_id in self :
            if me_id.state != STATES[0][0]:
                raise UserError("Cannot delete non draft record!")
        return super(krs, self).unlink()

    def hitung_jumlah_sks(self, ):
        pass


    def hitung_ip_semester(self, ):
        pass


    def hitung_max_sks_semester_depan(self, ):
        pass



    def create_tagihan_spp(self, ):
        price_unit = 10000000
        inv = self.env['account.move'].create({
            'partner_id': self.mahasiswa_id.id,
            'invoice_date': time.strftime('%Y-%m-%d'),
            'payment_reference': self.name,
            'move_type':'out_invoice',
            'invoice_line_ids': [
                (0,0,{
                    'name':'Tagihan SPP {}/{}'.format(self.semester_id.name, self.semester_id.tahun_ajaran_id.name),
                    'quantity':1,
                    'price_unit': price_unit,
                })
            ]
        })

        self.invoice_id = inv.id
