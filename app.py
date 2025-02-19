from flask import Flask
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAFZBJUNJNjoBO5NX24aj0YfzZBEOLLgkxidZADWAzwNFcZAd21vlcFVJreHbE8ZA9diSDluQh9PETLmw5QjzfRRSmjtbZAFsGP3BUXU4g2ZCZCHd3vu1Wi7LzPeZBuExJ7GlGzqrtxHWUly5aaIZBQOWZCNZCAzIkX2D8daYeyT7KJlqEK0tygLI3Azd4Y3p82o8Lcoh3yV92p7MuUTJDT7km8yNfZANT7B03atqZAONz"
PHONE_NUMBER_ID = "556897260845247"
RECIPIENT_NUMBER = "2347033406603"  # e.g., "1234567890"
TEMPLATE_NAME = "product_template"
WABA_ID = ' 617348098119948'

PRODUCT_NAME = "iPhone 13"
PRODUCT_DESCRIPTION = "128GB, Midnight Black, A15 Bionic Chip"
PRODUCT_LOCATION = "New York, USA"
PRODUCT_PRICE = "$799"
PRODUCT_QTY = "20 units"
PRODUCT_IMAGE = "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/iphone-13-finish-select-202207-6-1inch_AV1?wid=940&hei=1112&fmt=png-alpha&.v=1657641867367"
ORDER_URL = "https://yourstore.com/order"
AVAILABILITY_URL = "https://yourstore.com/check-availability"

@app.route("/")
def hello_world():
    url = f"https://graph.facebook.com/v19.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    data = {
        "messaging_product": "whatsapp",
        "to": RECIPIENT_NUMBER,
        "type": "template",
        "template": {
            "name": TEMPLATE_NAME,
            "language": {"code": "en"},
            "components": [
                {
                    "type": "HEADER",
                    "parameters": [
                        {
                            "type": "IMAGE",
                            "image": {
                                "link": "lemsip.png"
                            }
                        }
                    ]
                },
                {
                    "type": "BODY",
                    "parameters": [
                        {"type": "TEXT", "text": "Nike Air Force 1"},
                        {"type": "TEXT", "text": "Classic white sneakers with a timeless look."},
                        {"type": "TEXT", "text": "Lagos, Nigeria"},
                        {"type": "TEXT", "text": "$120"},
                        {"type": "TEXT", "text": "5 in stock"}
                    ]
                },
                {
                    "type": "BUTTON",
                    "sub_type": "URL",
                    "index": "0",
                    "parameters": [
                        {"type": "TEXT", "text": "Order Now"},
                        {"type": "TEXT", "text": "https://google.com/"}
                    ]
                },
                {
                    "type": "BUTTON",
                    "sub_type": "URL",
                    "index": "1",
                    "parameters": [
                        {"type": "TEXT", "text": "Check Availability"},
                        {"type": "TEXT", "text": "https://google.com/"}
                    ]
                }
            ]
        }
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())
    return "<p>Hello, Message Send!</p>" 


@app.route('/hello')
def helo():
    url = f"https://graph.facebook.com/v19.0/{WABA_ID}/message_templates"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}

    response = requests.get(url, headers=headers)
    print(response.json())
    return '<h1>Send template</h1>'


if __name__ == '__main__':
    app.run(debug=True)