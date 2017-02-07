# -*- coding: utf-8 -*-
from odoo import http

# class VentaTiempoAire(http.Controller):
#     @http.route('/venta_tiempo_aire/venta_tiempo_aire/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/venta_tiempo_aire/venta_tiempo_aire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('venta_tiempo_aire.listing', {
#             'root': '/venta_tiempo_aire/venta_tiempo_aire',
#             'objects': http.request.env['venta_tiempo_aire.venta_tiempo_aire'].search([]),
#         })

#     @http.route('/venta_tiempo_aire/venta_tiempo_aire/objects/<model("venta_tiempo_aire.venta_tiempo_aire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('venta_tiempo_aire.object', {
#             'object': obj
#         })