# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    rma_request_id = fields.Many2one('rma.request', string='RMA Request', store=True, readonly=False)
