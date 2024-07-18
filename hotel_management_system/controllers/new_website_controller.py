from odoo import http, _
from odoo.http import request
class anubhav(http.Controller):
    @http.route('/hotel_management/form_create', type='http', auth="public", website=True,csrf=False)
    def formCreation(self, **kwargs):
        return http.request.render("hotel_management_system.website_form_create", {})

    @http.route('/hotel_management/submit_button', type='http', auth="public", website=True,csrf=False)
    def submitButton(self, **post):
        print(request.env.user.name)
        if request.env.user.name == "Public user":
            request.env['public.info'].sudo().create({
                'name': post['name'],
                'email':post['email'],
                'message':post['message'],
            })
        else:
            request.env['private.info'].sudo().create({
                'name': post['name'],
                'email': post['email'],
                'message': post['message'],
            })
        return http.request.render("hotel_management_system.thank_you_page", {})



