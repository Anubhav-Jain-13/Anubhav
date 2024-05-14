from odoo import models, fields, api, _


class Commission(models.Model):
    _name = "commission.model"

    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    customer = fields.Many2one("res.users", string="Salesperson", required=False)
    list = fields.Many2many('sale.order', string="List",compute="_compute_order_list")

    @api.depends('start_date', 'end_date')
    def _compute_order_list(self):
        for record in self:
            if record.start_date and record.end_date and record.customer.name:
                print(record.customer.name)
                domain = [('date_order', '>=', record.start_date), ('date_order', '<=', record.end_date),
                          ('user_id', '=', record.customer.name)]
                orders = self.env['sale.order'].search(domain)
                record.list = [(6, 0, orders.ids)]
            else:
                record.list = False

    def action_show_matching_orders(self):
        pass