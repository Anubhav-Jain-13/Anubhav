from odoo import models, fields


# function for showing list price through popup in product.product model start here
class ProductLstPricePopup(models.TransientModel):
    _name = 'product.lst_price.popup'
    _description = 'List Price Popup'

    lst_price = fields.Float(string='List Price', readonly=True)
 # function for showing list price through popup in product.product model start here
