#!/usr/bin/python
#-*- coding: utf-8 -*-

STATES = [('draft','Draft'),('open','Aktiv'),('done','Selesai')]
from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning

class krs(models.Model):
    """ini class"""

    _name = "vit.krs"
    _description = "vit.krs"
    name = fields.Char( required=True, default="New", readonly=True,  string="Name",  help="")
    state = fields.Selection(selection=STATES,  readonly=True, default=STATES[0][0],  string="State",  help="")
    jumlah_sks = fields.Float( string="Jumlah sks",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    ip_semester = fields.Float( string="Ip semester",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    max_sks_semester_depan = fields.Float( string="Max sks semester depan",  readonly=True, states={"draft" : [("readonly",False)]},  help="")


    def hitung_jumlah_sks(self, ):
        """ini fungsi itung SKS"""
        pass


    def hitung_ip_semester(self, ):
        pass


    def hitung_max_sks_semester_depan(self, ):
        pass


    def create_tagihan_spp(self, ):
        pass


    @api.model
    def create(self, vals):
        if not vals.get("name", False) or vals["name"] == "New":
            vals["name"] = self.env["ir.sequence"].next_by_code("vit.krs") or "Error Number!!!"
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

    mahasiswa_id = fields.Many2one(comodel_name="res.partner",  string="Mahasiswa",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    semester_id = fields.Many2one(comodel_name="vit.semester",  string="Semester",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    prodi_id = fields.Many2one(comodel_name="res.partner",  string="Prodi",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    jenjang_id = fields.Many2one(comodel_name="vit.jenjang",  string="Jenjang",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    penasehat_akademik_id = fields.Many2one(comodel_name="hr.employee",  string="Penasehat akademik",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    perguruan_tinggi_id = fields.Many2one(comodel_name="res.partner",  string="Perguruan tinggi",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    krs_detail_ids = fields.One2many(comodel_name="vit.krs_detail",  inverse_name="krs_id",  string="Krs detail",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    fakultas_id = fields.Many2one(comodel_name="res.partner",  string="Fakultas",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
    invoice_id = fields.Many2one(comodel_name="account.move",  string="Invoice",  readonly=True, states={"draft" : [("readonly",False)]},  help="")
