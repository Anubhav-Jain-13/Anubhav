{
    "name": "Point Of sale",
    "author": "Anubhav",
    "version": "1.0.0",
    "sequence": -500,
    "category": "POS",
    "website": "www.pos.com",
    "summary": "This model is about pos info",
    "depends": ['base', 'mail', 'web', 'sale', 'sale_management', 'point_of_sale', 'hr_expense', 'website'],

    "data": [

    ],


    'assets': {
        'point_of_sale._assets_pos': [
            'wb_pos/static/src/js/sample_button.js',
            'wb_pos/static/src/xml/button.xml',
            'wb_pos/static/src/xml/chrome.xml',
        ],

    },

    "demo": [],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
