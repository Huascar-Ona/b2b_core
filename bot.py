# -*- coding: utf-8 -*-
from openerp import fields,api,models

class bot(models.Model):
    _name = "b2b.bot"

    name = fields.Char("Nombre")
    token = fields.Char("Token")
