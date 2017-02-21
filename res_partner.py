from odoo import models, fields

class res_partner(models.Model):
  _name = "res.partner"
  _inherit = "res.partner"

  telegram_chat_id = fields.Char("Telegram Chat ID")
  identifier = fields.Char("Identificador")
