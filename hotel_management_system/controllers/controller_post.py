from odoo import http
from odoo.http import request
import json


# define a custom controller using post method to create a new record of sale.order start here
class SaleOrderController(http.Controller):
    @http.route('/create_sale_order', type='json', auth='public', methods=['POST'], csrf=False)
    def create_sale_order(self, **kwargs):
        try:
            # Extract data from the request
            data = json.loads(request.httprequest.data)

            # Define sale order values
            order_vals = {
                'partner_id': data.get('partner_id'),
                'order_line': [(0, 0, {
                    'product_id': line.get('product_id'),
                    'product_uom_qty': line.get('quantity'),
                    'price_unit': line.get('price_unit'),
                }) for line in data.get('order_lines', [])]
            }

            # Create the sale order
            sale_order = request.env['sale.order'].sudo().create(order_vals)

            return {'status': 'success', 'sale_order_id': sale_order.id}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}
# define a custom controller using post method to create a new record of sale.order end here

# below code is for json in postman
# {
#     "partner_id": 1,
#     "order_lines": [
#         {
#             "product_id": 1,
#             "quantity": 2,
#             "price_unit": 100
#         },
#         {
#             "product_id": 2,
#             "quantity": 1,
#             "price_unit": 200
#         }
#     ]
# }
