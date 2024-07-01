# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosOrder(models.Model):
    _inherit = "pos.order"

    custom_note = fields.Text(
        string="Order Note")

    # def get_discount(self):
    #     param_obj = self.env['ir.config_parameter'].sudo()
    #     discount_limit = param_obj.get_param('sale_discount_limit.discount_limit', default=0.0)
    #     return float(discount_limit)
    def get_discount(self):
        param_obj = self.env['ir.config_parameter'].sudo()
        percentage = param_obj.get_param('percentage', default=10)
        return float(percentage)

    @api.model
    def _order_fields(self, ui_order):
        order_result = super(PosOrder, self)._order_fields(ui_order)
        order_result['custom_note'] = ui_order.get('note' or "");
        # order_result['note'] = ui_order.get('note' or "");
        return order_result

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    # is_discount_limit = fields.Boolean(string='',
    #     config_parameter='sale_discount_limit.is_discount_limit',
    #     help='Check this field for enabling discount limit', default="1")
    # discount_limit = fields.Float(string='%',
    #     config_parameter='sale_discount_limit.discount_limit',
    #     help='The discount limit amount in percentage ', default=10)

    # is_discount_limit = fields.Boolean(string='',
    #     config_parameter='percentage',
    #     help='Check this field for enabling discount limit', default="1")
    # discount_limit = fields.Float(string='%',
    #     config_parameter='percentage',
    #     help='The discount limit amount in percentage ', default=10)

    percentage = fields.Integer(string="Percentage",config_parameter="percentage")
