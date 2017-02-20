# -*- coding: utf-8 -*-
from odoo import http
from odoo import models
import json
# import base64
import requests

class VentaTiempoAire(http.Controller):
     @http.route('/api/telegram/', auth='user', type='json', methods=['POST'], csrf=False)
     def index(self, file, telegram_id, token, reply_markup=False):
        # encode_file = base64.b64encode(file)
        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_id)])

        api_url = "https://api.telegram.org/bot" + token

        url = api_url + "/sendDocument"
        params = {'chat_id':int(telegram_id)}
        files = {'document': open(file, 'rb')}

        if partner:
            if reply_markup:
                params["reply_markup"] = json.dumps(reply_markup)
            r = requests.post(url, params=params, files=files)
            return {"response": "OK", "telegram_url": api_url}
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
