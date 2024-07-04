# -*- coding: utf-8 -*-

# add location task start here
from odoo import api, fields, models

class Location(models.Model):
    _name = "res.location"
    _description = "point od sale location"

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    pin_code = fields.Char(string="Pin Code")
# add location task end here