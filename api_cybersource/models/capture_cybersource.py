# -*- coding: utf-8 -*-

from odoo import models, fields
import requests
import datetime
import hmac
import hashlib
import base64
import json


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # function for transfer sale order record to cybersource transaction start here
    def capture_cybersource(self):
        self.ensure_one()
        order = self

        url = "https://apitest.cybersource.com/pts/v2/payments"
        payload = {
            "clientReferenceInformation": {
                "code": "TC50171_3"
            },
            "paymentInformation": {
                "card": {
                    "number": "4111111111111111",
                    "expirationMonth": "12",
                    "expirationYear": "2031"
                }
            },
            "orderInformation": {
                "amountDetails": {
                    "totalAmount": str(order.amount_total),  # Fetching total amount from the sale order
                    "currency": order.currency_id.name  # Fetching the currency from the sale order
                },
                "billTo": {
                    "firstName": "John",
                    "lastName": "Doe",
                    "address1": "1 Market St",
                    "locality": "san francisco",
                    "administrativeArea": "CA",
                    "postalCode": "94105",
                    "country": "US",
                    "email": "test@cybs.com",
                    "phoneNumber": "4158880000"
                }
            }
        }
        # Debugging: print the order details
        print(f"Order ID: {order.id}")
        print(f"Order Total Amount: {order.amount_total}")
        print(f"Order Currency: {order.currency_id.name}")

        # Prepare the headers
        merchant_id = "anubhav1309_1720527590"
        key_id = "9e019f41-b274-486d-825c-d1ebea1759e1"
        secret_key = "s1Nrneqe3y7GYrQpDdYp+vKp2zyBAlR04LcoqrQGAtA="  # Replace with your actual secret key
        timestamp = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        digest = base64.b64encode(hashlib.sha256(json.dumps(payload).encode('utf-8')).digest()).decode('utf-8')
        print(digest)
        signature_header = f"host: apitest.cybersource.com\nv-c-date: {timestamp}\nrequest-target: post /pts/v2/payments\ndigest: SHA-256={digest}\nv-c-merchant-id: {merchant_id}"
        signature = base64.b64encode(
            hmac.new(base64.b64decode(secret_key), signature_header.encode('utf-8'), hashlib.sha256).digest()).decode(
            'utf-8')
        signature = f'keyid="{key_id}", algorithm="HmacSHA256", headers="host v-c-date request-target digest v-c-merchant-id", signature="{signature}"'

        headers = {
            'host': "apitest.cybersource.com",
            'v-c-date': timestamp,
            'digest': f"SHA-256={digest}",
            'v-c-merchant-id': merchant_id,
            'signature': signature,
            'Content-Type': 'application/json'
        }

        response = requests.post(url, json=payload, headers=headers)
        print(response)
        if response.status_code == 201:
            self.message_post(body="Payment successfully captured via CyberSource.")
            self._create_invoices()
        else:
            self.message_post(body=f"Failed to capture payment: {response.text}")
        return True
        # function for transfer sale order record to cybersource transaction start here


# add three new field inside notebook in payment.provider start here
class Cybersource(models.Model):
    _inherit = "payment.provider"

    aps_merchant_ids = fields.Char(string="APS Merchant Identifier")
    aps_api_key_id = fields.Char(string="APS Api Access")
    aps_secret_key = fields.Char(string="APS secret key")
# add three new field inside notebook in payment.provider end here
