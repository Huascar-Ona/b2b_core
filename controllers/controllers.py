# -*- coding: utf-8 -*-
from odoo import http
from odoo import models
import json
import base64

class Telegram(http.Controller):
     @http.route('/api/telegram/', auth='user', type='json', methods=['POST'], csrf=False)
     def index(self, file, telegram_id):
        encode_file = base64.b64encode(file)
        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_id)])

        if partner:
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
