# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PosOrder(models.Model):
    _inherit = "pos.order"

    custom_note = fields.Text(string="Order Note")
    location = fields.Char(string="Location")

    def get_discount(self):
        param_obj = self.env['ir.config_parameter'].sudo()
        percentage = param_obj.get_param('percentage', default=10)
        return float(percentage)

    @api.model
    def _order_fields(self, ui_order):
        order_result = super(PosOrder, self)._order_fields(ui_order)
        order_result['custom_note'] = ui_order.get('note' or "")
        # order_result['location'] = ui_order.get('location' or "")
        order_result['location'] = ui_order.get('location_pos')
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
    # add location task start here
    location = fields.Many2many(string='Location',related='pos_config_id.location_ids',readonly=False)

class PosConfigs(models.Model):
    _inherit = "pos.config"

    location_ids = fields.Many2many('res.location',string="Location Id")

    def get_locations(self):
        result = []
        data = self.env['pos.config'].search([])
        for rec in data:
            for i in rec.location_ids:
                # result.append(i.name)
                result.append({
                    'name': i.name,
                    'address': i.address,
                    'pin_code': i.pin_code,
                })
        print(result)
        return result
    # add location task end here



class PosPartnerList(models.Model):
    _inherit = 'res.partner'

    @api.model
    def custom_button_action(self):
        # Your custom logic here
        # This could involve creating a record, opening a wizard, etc.
        return {
            'type': 'ir.actions.act_window',
            'name': 'Custom Action',
            'view_mode': 'form',
            'res_model': 'res.partner',
            'target': 'new',
        }
