import requests


WEBHOOK_URL = "https://webhook.site/2bbbcd28-4631-46e7-a710-ed7c02fb152e"


def send_webhook(event_data):

    try:

        response = requests.post(
            WEBHOOK_URL,
            json=event_data,
            timeout=5
        )

        print("Webhook sent:", response.status_code)

    except Exception as e:

        print("Webhook error:", e)