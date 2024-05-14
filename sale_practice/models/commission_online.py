from odoo import models, fields, api, _


class CommissionOnLine(models.Model):
    _name = "commission.online"
    _description = "ABC"

    order_no = fields.Char(string="Order Number")
    customer = fields.Char(string="Customer")
    salesperson = fields.Char(string="Salesperson")
    commission_percentage = fields.Float(string="Commission Percentage")
    commission = fields.Float(string="Commission Amount")
    total = fields.Float(string="Amount Total")


class SaleOrder(models.Model):
    _inherit = "sale.order"
    commission = fields.Float(string="Commission")

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        partner_name = self.env['res.partner'].browse(vals.get('partner_id')).name if vals.get('partner_id') else False
        user_name = self.env['res.users'].browse(vals.get('user_id')).name if vals.get('user_id') else False
        total_amount = res.amount_total
        rec = self.env['commission.online'].create({
            'order_no': vals.get('name'),
            'customer': partner_name,
            'salesperson': user_name,
            'commission_percentage': 5,
            'commission': vals.get('commission'),
            'total': total_amount
        })
        return res

