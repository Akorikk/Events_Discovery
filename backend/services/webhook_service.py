import requests


WEBHOOK_URL = "https://webhook.site/11869edc-5325-4bb7-96ae-ffd3fb5084db"


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