{
    "name": "Hotel data",
    "author": "Anubhav Jain",
    "version": "1.0.0",
    "sequence": -100,
    "category": "Hotel management",
    "website": "www.hotel.com",
    "summary": "This model is about hotel info",
    "depends": ['base', 'mail', 'web', 'sale', 'sale_management', 'point_of_sale', 'hr_expense', 'website'],

    "data": ["security/ir.model.access.csv",
             "views/menu.xml",
             "wizard/customer_wizard.xml",
             "wizard/create_room_wizard.xml",
             "views/customer_view.xml",
             "views/room_view.xml",
             "views/staff_view.xml",
             "views/housekeeping_view.xml",
             "views/pos.xml",
             "views/add_button_sale.xml",
             "views/location.xml",
             "reports/report.xml",
             "reports/room_report.xml",
             "reports/staff_report.xml",
             "reports/customer_report.xml",
             "data/sequence.xml",
             "data/schedular_birthday.xml",
             "data/mail_template.xml",
             ],

    'assets': {
        'web.assets_backend': [
            'hotel_management_system/static/src/js/expense_button.js',
            'hotel_management_system/static/src/views/button.xml',
            'hotel_management_system/static/src/js/A_class.js',
            'hotel_management_system/static/src/js/B_class.js',
            'hotel_management_system/static/src/js/add_button_sale.js',

        ],

        'web.assets_frontend': [
            'hotel_management_system/static/src/js/website_change_report.js',

        ],

    },

    'assets': {
        'point_of_sale._assets_pos': [
            'hotel_management_system/static/src/js/custom_note.js',
            'hotel_management_system/static/src/js/my_discount.js',
            'hotel_management_system/static/src/js/notes.js',
            'hotel_management_system/static/src/js/sundry_button.js',
            'hotel_management_system/static/src/js/location_button.js',
            'hotel_management_system/static/src/js/custom_button_popup.js',
            'hotel_management_system/static/src/views/button.xml',
            'hotel_management_system/static/src/views/custom_button_popup.xml',
        ],

    },

    "demo": [],
    "installable": True,
    "auto_install": False,
    "license": "LGPL-3",
}
