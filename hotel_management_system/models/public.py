# -*- coding: utf-8 -*-
# save data of website controller task start here

from odoo import models, fields


class PublicModel(models.Model):
    # Attributes
    _name = "public.info"
    _description = "This model is about public user"

    # fields
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    message = fields.Char(string='Message')
# save data of website controller task end here
