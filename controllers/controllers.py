# -*- coding: utf-8 -*-
from odoo import http
from odoo import models

class VentaTiempoAire(http.Controller):
     @http.route('/api/telegram/', auth='user', type='json', methods=['POST'], csrf=False)
     def index(self, file, filename, telegram_id, reply_markup=False):
        partners = http.request.env['res.partner']
        partner = partners.search([('telegram_chat_id','=', telegram_id)])

        if not partner:
            partner = partners.search([('identifier','=', telegram_id)])

        if partner:
            partner.send_file(file, filename)
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
