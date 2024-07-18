from odoo import http
from odoo.http import request
import json


class CustomEmailController(http.Controller):

    @http.route('/website/form/mail.mail', type='json', auth='public', methods=['POST'], website=True)
    def create_email(self, **kwargs):
        values = json.loads(request.httprequest.data)
        print(values)
        if values:
            request.env['mail.mail'].sudo().create(values.get('data_value'))
            return {'status': 'success', 'message': 'Email created successfully'}
        return {'status': 'error', 'message': 'Missing values'}

# below code is for json in postman
# {
#     "model": "mail.mail",
#     "data_value": {
#         "email_from": "anubhav@gmail.com.com",
#         "email_to": "jay@gmail.com.com",
#         "subject": "Anubhav",
#         "body_html": "<p>Your email content here</p>"
#     }
# }
