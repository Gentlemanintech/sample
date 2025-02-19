from flask import Flask
import requests

app = Flask(__name__)

ACCESS_TOKEN = "EAAFZBJUNJNjoBOwgo5RMIQkPAssSou6HgNV8Gh6uD3taAqoz7Q4T9VfqiDZANceNsjdXYFeL0pJYTCfpCV7LbZAZAmTYf2T05EtVCfcHcNLATycbqf4xooZAVrcZBmxyViwOedSftqfjJf4pR7HBWEswUZAu7hJbJi4coqvABDp16axkmoX8XO0c1bQyc7gf6dF0g4xfPmqc9eOyjWp5K9m89ofx4iBDKX6tw0ZD"
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
                                "link": "https://scontent.whatsapp.net/v/t61.29466-34/473402686_1359234888537845_7548250917299565939_n.png?ccb=1-7&_nc_sid=8b1bef&_nc_eui2=AeHSqty5ezc2WVON6RhjS8o2Eyhlut-_HRETKGW6378dETdxuSWROhj4TQ4RBCbxAQRJZsZJsARTzZ9Umm_bYIBh&_nc_ohc=-dNaJDzc6-EQ7kNvgEF4DZg&_nc_oc=AdhF9A0HD2ZYVm5ISkyBsTgeAZy3LvpdUbUaVIYuPxFUfkGzaxMlf7IedctEeEBGQcI&_nc_zt=3&_nc_ht=scontent.whatsapp.net&edm=AH51TzQEAAAA&_nc_gid=A-CVdCpfHmqCRVXqsNBjy5o&oh=01_Q5AaIEtLRqLTDAQWbnLKfLo2uA49n-O925RgpG2bkFJNtgjt&oe=67DD9BE2"
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