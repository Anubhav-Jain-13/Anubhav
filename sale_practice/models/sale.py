from odoo import models, fields, _, api
from odoo.exceptions import ValidationError


class StockMoveNew(models.Model):
    _inherit = 'sale.order'
    custom_name = fields.Char(string="Custom Name")

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
    _inherit="pos.order"

    note = fields.Char(string="Note")



