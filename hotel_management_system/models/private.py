# -*- coding: utf-8 -*-
# save data of website controller task start here
from odoo import models, fields


class PrivateModel(models.Model):
    # Attributes
    _name = "private.info"
    _description = "This model is about private user"

    # fields
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    message = fields.Char(string='Message')
# save data of website controller task end here
