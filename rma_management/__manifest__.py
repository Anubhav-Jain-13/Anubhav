# -*- coding: utf-8 -*-
{
    "name": "RMA Management",
    "author": "Anubhav Jain",
    "version": "1.0.0",
    "sequence": -100,
    "category": "RMA Management",
    "website": "www.RMA.com",
    "summary": "To manage RMA process",
    "depends": ['base', 'mail', 'web', 'sale', 'sale_management', 'point_of_sale', 'hr_expense', 'website'],


    "data": ["security/ir.model.access.csv",
             "views/menu.xml",
             "wizard/rma_wizard.xml",
             "views/rma_management.xml",
             "views/sale_order_line.xml",
             "views/sale_order.xml",

           ],


    "demo": [],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
