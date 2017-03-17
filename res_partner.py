# -*- coding: utf-8 -*-
from odoo import models, fields, api
import base64
import os
import json
import requests

class res_partner(models.Model):
  _inherit = "res.partner"

  telegram_chat_id = fields.Char("Telegram Chat ID")
  identifier = fields.Char("Identificador alterno")
  bot_token = fields.Char("Token del bot")  

  @api.model
  def send_file(self, file, filename, reply_markup=False):  
    api_url = "https://api.telegram.org/bot" + self.bot_token

    url = api_url + "/sendDocument"
    params = {'chat_id':int(self.telegram_chat_id)}

    file_content = base64.b64decode(file)
    tempf = "/tmp/tmp%s"%self.env.uid
    if not os.path.exists(tempf):
        os.makedirs(tempf)
    file_path = os.path.join(tempf, filename)
    with open(file_path, "wb") as f:
        f.write(file_content)
    files = {'document': open(file_path, 'rb')}

    if reply_markup:
        params["reply_markup"] = json.dumps(reply_markup)

    r = requests.post(url, params=params, files=files)

    os.unlink(os.path.join(tempf, filename))
    os.rmdir(tempf)

    # creación de logs
    record = self.env['log.log']
    record.create({'partner': self.id, "nombre_archivo": filename})
    
    return True

class wizard_send_file(models.TransientModel):
    _name = "venta_aire.wizard_send_file"

    file = fields.Binary("Archivo")
    filename = fields.Char("Nombre del archivo")

    @api.one
    def action_send(self):
        partner = self.env["res.partner"].browse(self.env.context.get("active_id"))
        partner.send_file(self.file, self.filename)
        return True
