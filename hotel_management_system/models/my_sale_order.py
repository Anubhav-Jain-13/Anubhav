from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'


    # manager approval task start here
    state = fields.Selection(
        selection_add=[('to_approve', "To Approve")],
    )
    def approve(self):
        self.write({'state': 'sale'})
        return True

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        # Update status bar to 'to_approve'
        self.write({'state': 'to_approve'})
        return res
    # manager approval task end here

