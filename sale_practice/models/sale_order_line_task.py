from odoo import models, fields, api


class StockOrderLineNew(models.Model):
    _inherit = 'sale.order.line'

    @api.model
    def create(self, vals):
        order_line = super(StockOrderLineNew, self).create(vals)
        if order_line.order_id:
            order_line.order_id._compute_total_quantity()
        return order_line

    def write(self, vals):
        res = super(StockOrderLineNew, self).write(vals)
        if self.order_id:
            self.order_id._compute_total_quantity()
        return res

    def unlink(self):
        orders = self.mapped('order_id')
        res = super(StockOrderLineNew, self).unlink()
        orders._compute_total_quantity()
        return res