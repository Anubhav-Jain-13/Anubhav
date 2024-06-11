import xmlrpc.client

# Replace with your actual server URL, database name, username, and password
url = 'http://localhost:8069'
db = 'Test17'  # Replace with your actual database name
username = 'odoo__17'  # The email address you set for the new user
# username = 'admin'
password = 'admin'  # The password you set for the user

# Common endpoint to authenticate and fetch the user ID
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

if uid:
    print(f"Authenticated as {username} (uid: {uid})")

    # Object endpoint to perform operations
    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    # Search for sale orders that are in 'draft' and with the same user mentioned
    sale_order_user_ids = models.execute_kw(db, uid, password,
                                            'sale.order', 'search',
                                            [[['state', '=', 'draft'], ['create_uid', '=', uid]]])
    print(f"Found {len(sale_order_user_ids)} sale orders in draft state.")

    # Confirm each sale order
    for sale_order_id in sale_order_user_ids:
        result = models.execute_kw(db, uid, password,
            'sale.order', 'action_confirm',
            [[sale_order_id]])
        print(f"Sale Order ID {sale_order_id} confirmed: {result}")

    # Search for sale orders that are in 'draft' and also added offset and limit
    # offset will all to fetch the data after the offset count given in value
    # limit will only fetch the limited number of record which is diven in the value
    sale_order_ids = models.execute_kw(db, uid, password,
                                       'sale.order', 'search',
                                       [[['state', '=', 'draft']]], {'offset': 2, 'limit': 5})
    print("sale orders", sale_order_ids)
    sale_orders = models.execute_kw(db, uid, password, 'sale.order', 'read', [sale_order_ids],
                                    {'fields': ['name', 'date_order', 'partner_id']})
    print(sale_orders)
    for order in sale_orders:
        print(order)

    # Fetching count of the draft email base on domain
    sale_order_count = models.execute_kw(db, uid, password,
                                         'sale.order', 'search_count',
                                         [[['state', '=', 'draft']]])
    print(sale_order_count)

    # sale_orders = models.execute_kw(db, uid, password, 'sale.order', 'search', [[['state', '=', 'draft']]])

    # fields_get
    # fie_get = models.execute_kw(db, uid, password, 'customer.info', 'fields_get', [],
    #                             {'attributes': ['string', 'help', 'type']})
    # print(fie_get)

else:
    print("Authentication failed.")