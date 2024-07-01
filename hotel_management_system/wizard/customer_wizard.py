# -*- coding: utf-8 -*-

from odoo import fields, models


class Demo(models.TransientModel):
    _name = "customer.wizard"

    name = fields.Char(string="Name", help="what is your name")
    Report_issue = fields.Text(string="Report", help="what is your problem")

    # function for submit button in wizard start
    def submit(self):
        print("submit")


class CancelButton(models.TransientModel):
    _name = "customer.wizard"

    name = fields.Char(string="Name", help="what is your name")
    Report_issue = fields.Text(string="Report", help="what is your problem")

    # function for submit button in wizard start
    def submit(self):
        print("submit")
