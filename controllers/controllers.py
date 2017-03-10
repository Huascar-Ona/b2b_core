# -*- coding: utf-8 -*-
from odoo import http
from odoo import models
import json
import base64
import requests
from StringIO import StringIO
import os

TOKEN = "322027161:AAHeLdME3aTbzJByCBSBfgPyCACzW6QVKL4"

class VentaTiempoAire(http.Controller):
     @http.route('/api/telegram/', auth='user', type='json', methods=['POST'], csrf=False)
     def index(self, file, filename, telegram_id, reply_markup=False):
        token = TOKEN
        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_id)])

        if partner:
            api_url = "https://api.telegram.org/bot" + token

            url = api_url + "/sendDocument"
            params = {'chat_id':int(telegram_id)}

            file_content = base64.b64decode(file)
            tempf = "/tmp/tmp%s"%http.request.env.uid
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
            record = http.request.env['log.log']
            record.create({'partner': partner.id, "nombre_archivo": filename})

            return {"response": "OK"}
        else:
            return {"telegram_id": "ERROR"}

#     @http.route('/telegram/telegram/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('telegram.listing', {
#             'root': '/telegram/telegram',
#             'objects': http.request.env['telegram.telegram'].search([]),
#         })

#     @http.route('/telegram/telegram/objects/<model("telegram.telegram"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('telegram.object', {
#             'object': obj
#         })
