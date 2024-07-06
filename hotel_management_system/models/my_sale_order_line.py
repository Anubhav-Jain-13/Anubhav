from odoo import models, fields, api

# add image task start here
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Binary(string="Product Image",related="product_template_id.image_1920")


class SaleOrderLine(models.Model):
    _inherit = 'stock.move'

    product_image = fields.Binary(string="Product Image",related="product_id.image_1920")


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    product_image = fields.Binary(string="Product Image",related="product_id.image_1920")
# add image task end here
