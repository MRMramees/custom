# -*- coding: utf-8 -*-
# from odoo import http


# class BiTest(http.Controller):
#     @http.route('/bi_test/bi_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bi_test/bi_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bi_test.listing', {
#             'root': '/bi_test/bi_test',
#             'objects': http.request.env['bi_test.bi_test'].search([]),
#         })

#     @http.route('/bi_test/bi_test/objects/<model("bi_test.bi_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bi_test.object', {
#             'object': obj
#         })
