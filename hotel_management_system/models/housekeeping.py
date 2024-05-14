from odoo import models, fields, _, api
from odoo.exceptions import UserError


class HousekeepingInformation(models.Model):
    # Attributes
    _name = "housekeeping.info"
    _description = "This model is about Housekeeping information"
    _rec_name = "task_description"

    # fields
    task_description = fields.Text(string="Task description")
    scheduled_date = fields.Date(string="Scheduled_date")
    room_id = fields.Many2one('room.info', string="Room no")
    staff_ids = fields.Many2many('staff.info', string="Assigned_to", domain=[('gender', '=', 'male')])
    sequence = fields.Integer(string="sq.")

