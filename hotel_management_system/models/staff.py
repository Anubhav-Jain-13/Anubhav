from datetime import date
from odoo import models, fields, api


class StaffInformation(models.Model):
    # attributes
    _name = "staff.info"
    _description = "This model is about staff information"
    _rec_name = 'employee_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    def check_orm(self):
        # ORM search method
        search_func = self.env['staff.info'].search([])
        print("search_func------->", search_func)
        for rec in search_func:
            print("full name----->", rec.employee_name)

        # ORM search_count method
        search_co = self.env['staff.info'].search_count([('gender', '=', 'male')])
        print("search_co for male only------->", search_co)

        # ORM browse method
        browse = self.env['staff.info'].browse(3)
        print("age----->", browse.age)

    # ORM create method
    def create_orm(self):
        create_var = self.env['staff.info'].create({
            "employee_name": 'Anubhav',
            "phone_no": "8349366073"
        })

    # ORM copy method
    def copy_orm(self):
        brw_id = self.env['staff.info'].browse(2)
        brw_id.copy()


    # button for resign and active start here
    def resignation(self):
            for rec in self:
                rec.status = 'resign'

    def revert_to_active(self):
            for rec in self:
                rec.status = 'active'

    # button for resign and active end here


        # fields
    employee_name = fields.Char(string="employee_name", required=True, index=True, track_visibility="always")
    employee_position = fields.Selection(
        [("manager", "Manager"), ("waiter", "Waiter"), ("floor cleaner", "Floor cleaner"),
         ("washroom cleaner", "Washroom cleaner")], string="employee_position")
    phone_no = fields.Char(string="phone_no")
    email_id = fields.Char(string="email_id")
    staff_id_no = fields.Integer(string="Staff Id Number")
    DOB = fields.Date(string="DOB", help="enter your DOB")
    age = fields.Integer(string="Age", compute="_computed_age")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("other", "Other")], string="Gender")
    housekeeping_ids = fields.Many2many('housekeeping.info', string="Housekeeping Tasks")
    task_done = fields.Boolean(string="Task Done")
    image = fields.Binary(string="customer Image")
    sequence = fields.Integer(string="sq.")
    rating=fields.Selection([('0','verylow'),('1','low'),('2','good'),('3','very good'),('4','excellent')],string="rating")
    status = fields.Selection([('active', "Active"), ('resign', "Resign")], string="status", readonly=True, default='active')

    # compute function for age
    def _computed_age(self):
        for rec in self:
            today = date.today()
            if rec.DOB:
                rec.age = today.year - rec.DOB.year
            else:
                rec.age = 0





