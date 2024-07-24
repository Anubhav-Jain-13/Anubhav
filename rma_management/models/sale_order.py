# -*- coding: utf-8 -*-
from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_replacement_order = fields.Boolean(string='RMA Request', readonly=True)
