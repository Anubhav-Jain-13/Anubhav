from odoo import models, fields, api, _

class PracticeInformationWizard(models.TransientModel):
     #Attributes
    _name = "practice.wizard.info1"
    _description = "This model is about practice wizard"


    name = fields.Char(string='Name')



