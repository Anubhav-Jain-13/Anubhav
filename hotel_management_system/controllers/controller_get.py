from odoo import http
from odoo.http import request


# define a custom controller using get method to fetch data from sale.order start here
class anubhav(http.Controller):
    @http.route('/hotel_management/anubhav/', type='http', auth="public", website=True)
    def patient_app_data(self, **kwargs):
        # return http.request.render("hotel_management_system.tmp_practice", {})
        sale_order = request.env['sale.order'].sudo().search([])
        details = {
            'records': sale_order,
        }
        return http.request.render("hotel_management_system.tmp_practice", details)
# define a custom controller using get method to fetch data from sale.order end here
