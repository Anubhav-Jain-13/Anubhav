{
    "name" : "sale practice",
    "author" : "Anubhav Jain",
    "version" : "1.0.0",
    "category" : "sale",
    "website" : "www.sale.com",
    "summary" : "This model is about sale info",
    "depends" : ['base','sale','sale_management','stock','point_of_sale','web'],
    "data" : ["security/ir.model.access.csv",
              "views/menu.xml",
              "wizard/practice_wizard.xml",
              "wizard/sale_wizard.xml",
              "views/menu_inherit.xml",
              "views/commission.xml",
              "views/commission_online.xml",
              "views/practice_view.xml",
              "views/sale.xml",
              "reports/practice.xml",
              ],
    "demo" : [],
    "installable" : True,
    "auto_install" : False,
    "license" : "LGPL-3",
    "sequence" : -100,
}