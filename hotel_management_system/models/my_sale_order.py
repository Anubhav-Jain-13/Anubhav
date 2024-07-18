from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # manager approval task start here
    state = fields.Selection(
        selection_add=[('to_approve', "To Approve")],
    )

    def approve(self):
        self.write({'state': 'sale'})
        return True

    # @api.model
    # def get_sale_limit(self):
    #     return float(self.env['ir.config_parameter'].sudo().get_param('sale_limit'))
    # def action_confirm(self):
    #     for order in self:
    #         sale_limit = self.get_sale_limit()
    #         if order.amount_total > sale_limit:
    #             order.write({'state': 'to_approve'})
    #         else:
    #             res = super(SaleOrder, self).action_confirm()
    #             return res

    # def action_confirm(self):
    #     pass
    #     res = super(SaleOrder, self).action_confirm()
    #     # Update status bar to 'to_approve'
    #     self.write({'state': 'to_approve'})
    #     return res
    # manager approval task end here
