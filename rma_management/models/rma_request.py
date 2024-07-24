# -*- coding: utf-8 -*-

from odoo import models, fields, api


class RmaRequest(models.Model):
    # Attributes
    _name = 'rma.request'
    _description = 'Return merchandise authorization request'
    _rec_name = 'rma_status'

    # fields
    sale_order_id = fields.Many2one('sale.order', string='Sale Order', required=True, readonly=False)
    product_id = fields.Many2one('product.product', string='Returned Product', required=True, readonly=False)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True, readonly=False, store=True)
    return_reason = fields.Selection([('defective', 'Defective'), ('wrong_item', 'Wrong Item'), ('other', 'Other')],
                                     string='Return Reason', required=True, readonly=False)
    return_date = fields.Date(string='Return Date', default=fields.Date.context_today, required=True, readonly=True)
    rma_status = fields.Selection(
        [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('completed', 'Completed')],
        string='RMA Status', required=False, readonly=True, default="pending")
    replacement_order_id = fields.Many2one('sale.order', string='Replacement Order', readonly=True)
    refund_invoice_id = fields.Many2one('account.move', string='Refund Invoice', readonly=True)

    @api.onchange('sale_order_id')
    def _onchange_sale_order_id(self):
        # Fetch the customer from the sale order
        if self.sale_order_id:
            self.customer_id = self.sale_order_id.partner_id.id
        if self.sale_order_id:
            # Fetch the first product from the sale order
            order_lines = self.sale_order_id.order_line
            if order_lines:
                self.product_id = order_lines[0].product_id
            else:
                self.product_id = False
        else:
            self.product_id = False

    # button function start here
    def pending_rma(self):
        for rec in self:
            rec.rma_status = 'pending'

    def approve_rma(self):
        for rec in self:
            rec.rma_status = 'approved'

    def action_reject(self):
        for rec in self:
            rec.rma_status = 'rejected'

    def action_complete(self):
        for rec in self:
            rec.rma_status = 'completed'
    # button function end here
