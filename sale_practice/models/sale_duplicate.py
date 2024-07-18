from datetime import timedelta

from odoo import models, fields, api


class SaleDuplicate(models.Model):
    _name = "sale.order.duplicate"
    _description = "sale order duplicate"

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Customer",
        required=True, change_default=True, index=True,
        tracking=1)
    sale_order_template_id = fields.Many2one(
        "sale.order.template", string="Default Sale Template")



