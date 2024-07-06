from odoo import models, fields, api
from odoo.exceptions import ValidationError


class StockMoveNew(models.Model):
    _inherit = 'sale.order'
    custom_name = fields.Char(string="Custom Name")
    total_quantity = fields.Float(string="Total Qantity", compute="_compute_total_quantity")  # add field in sale.order

    def action_confirm(self):
        for order in self:
            for line in order.order_line:
                if line.product_uom_qty <= 0:
                    raise ValidationError(
                        "Please enter a quantity value for all order lines before confirming the order.")
        return super(StockMoveNew, self).action_confirm()

    def _get_order_lines_to_report(self):
        # if self._context.get('my_report'):
        #     # pass your lines from here
        #     pass
        # else:
        res = super(StockMoveNew, self)._get_order_lines_to_report()
        print(" res>>>>>>>>>>>>>>", res)
        return res

    # calculate total quantity from sale.order.line in total_quantity field in sale.order start here
    @api.depends('order_line.product_uom_qty', 'order_line.product_id.type')
    def _compute_total_quantity(self):
        for order in self:
            total_qty = sum(
                order.order_line.filtered(lambda line: line.product_id.type == 'product').mapped('product_uom_qty')
            )
            order.total_quantity = total_qty


    # calculate total quantity from sale.order.line in total_quantity field in sale.order end here


class StockMove(models.Model):
    _inherit = 'stock.picking'
    custom_name = fields.Char(string="Custom Name")


# related='sale_id.custom_name',

class StockOrderLineNew(models.Model):
    _inherit = 'sale.order.line'
    extra = fields.Integer(string="Extra Tax")


#     def _prepare_procurement_values(self, group_id=False):
#         values = super(StockOrderLineNew, self)._prepare_procurement_values(group_id)
#         values.update({
#             'extra': self.extra
#         })
#         return values
# class StockRule(models.Model):
#     _inherit = 'stock.rule'
#
#     def _get_custom_move_fields(self):
#         fields = super(StockRule, self)._get_custom_move_fields()
#         fields += ['extra']
#         return fields

class StockMovePickingNew(models.Model):
    _inherit = 'stock.move'
    extra = fields.Integer(string="Extra Tax")


# related='sale_line_id.extra',


class ResPartner(models.Model):
    _inherit = 'res.partner'

    commission_amount = fields.Integer(string="Commission Amount")
    percentage = fields.Integer(string="Percentage")


class posOrders_new(models.Model):
    _inherit = "pos.order"

    note = fields.Char(string="Note")


class Product_product_new_button(models.Model):
    _inherit = "product.product"

    def new_button(self):
        pass

    # def get_expensive_products(self):
    #     pass

    # function for showing list price through popup in product.product model start here
    def my_button(self):
        # Create a context with the product's list price
        context = {
            'default_lst_price': self.lst_price,
        }

        return {
            'type': 'ir.actions.act_window',
            'name': 'List Price',
            'view_mode': 'form',
            'res_model': 'product.lst_price.popup',
            'target': 'new',
            'context': context,
        }
    # function for showing list price through popup in product.product model end here
