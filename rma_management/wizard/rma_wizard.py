# -*- coding: utf-8 -*-

from odoo import fields, models, api


class RmaWizard(models.TransientModel):
    # attribute
    _name = "rma.wizard"
    _description = "RMA Wizard"

    # fields
    rma_request_id = fields.Many2one('rma.request', string="RMA Request", required=True)
    action = fields.Selection([('approve', 'Approve'), ('reject', 'Reject')], string='Action', required=True)
    replacement_order_id = fields.Many2one("sale.order", string='Replacement Order', required=False)
    refund_invoice_id = fields.Many2one("account.move", string="Refund Invoice", required=False)

    # function for wizard buttons start here
    def approved(self):
        self.ensure_one()
        rma_request = self.rma_request_id

        if not rma_request:
            return

        # Create a new sale order
        new_sale_order = self.env['sale.order'].create({
            'partner_id': rma_request.customer_id.id,
            'is_replacement_order': True,
            'order_line': [(0, 0, {
                'product_id': rma_request.product_id.id,
                'product_uom_qty': 1,  # Adjust quantity as needed
                'price_unit': rma_request.product_id.list_price,  # Adjust price as needed
                'rma_request_id': rma_request.id,
            })],
        })

        # Update the RMA request with the new sale order
        rma_request.write({
            'rma_status': 'completed',
            'replacement_order_id': new_sale_order.id,
            'refund_invoice_id': self.refund_invoice_id.id,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Replacement Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'res_id': new_sale_order.id,
            'target': 'current',
        }

    def reject(self):
        self.ensure_one()
        rma_request = self.rma_request_id

        if not rma_request:
            return

        # Create a refund invoice
        invoice_vals = {
            'move_type': 'out_refund',
            'partner_id': rma_request.customer_id.id,
            'invoice_date': fields.Date.context_today(self),
            'invoice_line_ids': [(0, 0, {
                'product_id': rma_request.product_id.id,
                'quantity': 1,
                'price_unit': rma_request.product_id.list_price,
            })]
        }
        refund_invoice = self.env['account.move'].create(invoice_vals)

        # Update the RMA request with the refund invoice
        rma_request.write({
            'rma_status': 'rejected',
            'replacement_order_id': refund_invoice.id,
            'refund_invoice_id': refund_invoice.id,
        })

        return {
            'type': 'ir.actions.act_window',
            'name': 'Refund Invoice',
            'res_model': 'account.move',
            'view_mode': 'form',
            'res_id': refund_invoice.id,
            'target': 'current',
        }
    # function for wizard buttons end here

    #  for getting active id in wizard and update the fields start here
    @api.model
    def default_get(self, fields):
        res = super(RmaWizard, self).default_get(fields)
        rma_request_id = self._context.get('active_id')
        if rma_request_id:
            rma_request = self.env['rma.request'].browse(rma_request_id)
            res.update({
                'rma_request_id': rma_request_id,
                # 'replacement_order_id': rma_request.sale_order_id.id,
            })
        return res
    #  for getting active id in wizard and update the fields end here





