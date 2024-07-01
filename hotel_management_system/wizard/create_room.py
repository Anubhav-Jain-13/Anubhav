# -*- coding: utf-8 -*-

from odoo import fields, models


# calling wizard from menu for room model
class CreateRoom(models.TransientModel):
    # attribute
    _name = "room.wizard"
    _description = "This model is about room information"

    # fields
    room_number = fields.Integer(string="room_number")
    floor_number = fields.Integer(string="floor_number")
    room_type = fields.Selection([("deluxe", "Deluxe"), ("luxury", "Luxury"), ("standard", "Standard")],
                                 string="room_type")
    price = fields.Monetary(string="price")
    currency_id = fields.Many2one('res.currency')
    status = fields.Selection([("available", "Available"), ("occupied", "Occupied")], string="status")
    housekeeping_ids = fields.One2many('housekeeping.info', 'room_id', string="Housekeeping Tasks")
    sequence = fields.Integer(string="sq.")
