from odoo import models, fields, api, _

class PracticeInformation(models.Model):
     #Attributes
    _name = "practice.info1"
    _description = "This model is about practice"


    name = fields.Char(string='Name')

    



