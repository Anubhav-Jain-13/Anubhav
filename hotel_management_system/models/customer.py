from odoo import models, fields, api, _

class CustomerInformation(models.Model):
     #Attributes
    _name = "customer.info"
    _description = "This model is about customer information"
    _rec_name = "customer_name"
    _inherit = ['mail.thread', 'mail.activity.mixin']  #chatter

    # fields
    customerID = fields.Char(string='CustomerID', readonly=True, copy=False, default=lambda self: _('New'))
    customer_name = fields.Char(string="Customer_name", required=True, translate="True", track_visibility="always")
    html_field = fields.Html(string='HTML Field',
                              help='This is an HTML field for storing rich text content.')
    email_id = fields.Char(string="Email_Id",widget="email")
    phone_no = fields.Char(string="Phone_no")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("other", "Other")], string="Gender")
    address = fields.Char(string="Address")
    customer_id_name = fields.Selection([("aadhar", "Aadhar"), ("pan", "Pan")], string="Customer_id_name")
    customer_id_number = fields.Char(string="customer_id_number")
    booking_time = fields.Datetime(string="Booking Time", compute='_compute_booking_time', store=True)
    image = fields.Binary(string="customer Image")
    signature = fields.Binary(string='Signature')
    sequence = fields.Integer(string="sq.")


                     # compute function for booking time
    @api.depends('customer_name', 'email_id', 'phone_no')  # Add all relevant fields that affect booking_time
    def _compute_booking_time(self):
        for record in self:
            # Set booking_time to the current datetime
            record.booking_time = fields.Datetime.now()


                      #ir_sequence for customers
@api.model
def create(self, vals):
    if vals.get('customerID',_('New')) == ('New'):
        vals['customerID'] = self.env['ir.sequence'].next_by_code('customer.seq.info') or _('New')
    res = super(CustomerInformation,self).create(vals)
    return res


                 # sql_constraints
_sql_constraints = [
    ('unique_name', 'UNIQUE (customer_name)', 'Customer name must be unique.')
]


                  #create ORM method
@api.model
def create(self, vals):
    res = super(CustomerInformation, self).create(vals)
    if vals.get('gender') == "male":
        res['customer_name'] = "Mr." + res["customer_name"]
    elif vals.get('gender') == "female":
        res['customer_name'] = "Mrs." + res["customer_name"]
    else:
        return res
    return res



# schedular task start here
class ResPartner(models.Model):
    _inherit = "res.partner"

    dob = fields.Date(string="DOB")
    def run_bdy_notification(self):
        today = fields.Date.today()
        today_month_day = today.strftime('%m-%d')
        all_records = self.search([])
        for rec in all_records:
            if rec.dob and rec.dob.strftime('%m-%d') == today_month_day:
                email_values = {
                    'email_to': rec.email,
                    'subject': f"Happy Birthday {rec.name}"
                }
                print(f"Happy Birthday {rec.display_name}")
                mail_template = self.env.ref('hotel_management_system.birthday_email_template')
                mail_template.send_mail(rec.id, email_values=email_values, force_send=True)
                print(f"Happy Birthday {rec.display_name} Again")
# schedular task end here