import base64
from io import BytesIO

import self
import xlwt

from odoo import models, fields, api, exceptions
from odoo.exceptions import UserError, ValidationError




class RoomInformation(models.Model):
    # attributes
    _name = "room.info"
    _description = "This model is about room information"
    _rec_name = 'room_number'

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
    # field for smart button
    listed_property_count = fields.Integer(string='Listed Property Count',
                                           compute='_compute_listed_property_count')

    # smart button
    def action_order_list(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Room LIST',
            'res_model': 'room.info',
            'view_mode': 'tree,form',
            'target': 'new',
            'domain': [('price', '=', self.price)]
        }

    @api.depends('price')
    def _compute_listed_property_count(self):
        for record in self:
            listed_property_count = self.env['room.info'].search_count(
                [('price', '=', record.price)])
            record.listed_property_count = listed_property_count

    # ORM create method


@api.model
def create(self, vals):
    res = super(RoomInformation, self).create(vals)
    print(type(res))
    print("created>>>>>>>>>>", vals)
    return res

    # ORM write method


def write(self, vals):
    res = super(RoomInformation, self).write(vals)
    print(type(res))
    print("writed>>>>>>>>>>", vals)
    return res

    # ORM unlink method


def unlink(self):
    for room in self:
        if room.status == 'occupied':
            raise exceptions.UserError(
                "Cannot delete room '{}' because it is currently occupied.".format(room.room_number))
    print("unlinking room:", self.ids)
    return super(RoomInformation, self).unlink()

    # ORM search method


def search_rooms_by_status(self):
    rooms = self.env['room.info'].search([('status', '=', "available")])
    print(rooms)
    return rooms

    # ORM copy method


def copy(self, default=None):
    if self.status == 'occupied':
        raise ValidationError(
            "Cannot copy room '{}' because it is currently occupied.".format(self.room_number))
    res = super(RoomInformation, self).copy(default)
    print(type(res))
    return res

