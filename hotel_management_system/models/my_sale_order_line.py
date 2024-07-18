from odoo import models, fields, api


# add image task start here
class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_image = fields.Binary(string="Product Image", related="product_template_id.image_1920")


class SaleOrderLine1(models.Model):
    _inherit = 'stock.move'

    product_image = fields.Binary(string="Product Image", related="product_id.image_1920")


class AccountMove(models.Model):
    _inherit = 'account.move.line'

    product_image = fields.Binary(string="Product Image", related="product_id.image_1920")


# add image task end here


class StockPicking(models.Model):
    _inherit = "sale.order"

    # ORM _get_view method
    @api.model
    def _get_view(self, view_id=None, view_type='form', **options):
        arch, view = super(StockPicking, self)._get_view(view_id, view_type, **options)
        current_user = self.env.user
        user_group = current_user.has_group('hotel_management_system.group_manager_record_access')
        if view_type == 'form' and not (user_group):
            for node in arch.xpath("//field"):
                node.set('readonly', '1')

        return arch, view
