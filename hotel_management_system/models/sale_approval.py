# -*- coding: utf-8 -*-

from odoo import models, fields


# manager approval task start here
class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    sale_limit = fields.Float(string="Sales Limit", config_parameter="sale_limit")
# manager approval task end here
