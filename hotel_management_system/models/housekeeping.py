# -*- coding: utf-8 -*-

from odoo import models, fields


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

    # def get_tasks_by_staff(self, staff_ids):
    #     # Get all housekeeping tasks
    #     all_tasks = self.search([])
    #
    #     # Filter tasks that are assigned to any of the given staff members
    #     tasks_for_staff = all_tasks.filtered(lambda task: any(staff_id in task.staff_ids.ids for staff_id in staff_ids))
    #     return tasks_for_staff


