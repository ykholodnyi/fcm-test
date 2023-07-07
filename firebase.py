import os

import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("./firebase-adminsdk.json")

default_app = firebase_admin.initialize_app(cred)

TOKEN = os.environ.get('TOKEN')
if not TOKEN:
    raise ValueError('TOKEN env variable is not set')


TITLE = os.environ.get('TITLE', 'Test title')
MESSAGE = os.environ.get('MESSAGE', 'Test message')
IOS_ALERT = os.environ.get('IOS_ALERT', 'Test alert')


def send_message():
    messages = [
        messaging.Message(
            notification=messaging.Notification(
                title=TITLE,
                body=MESSAGE,
            ),
            token=TOKEN,
            apns=messaging.APNSConfig(
                payload=messaging.APNSPayload(
                    aps=messaging.Aps(
                        content_available=True,
                        alert=IOS_ALERT,
                        badge=0,
                        sound=messaging.CriticalSound('default', 0.5)
                    )
                )
            ),
            android=messaging.AndroidConfig(
                priority='high',
            )
        ),
    ]

    response = messaging.send_each(messages)

    print(f'success: {response.success_count}, failed: {response.failure_count}')

    for resp in response.responses:
        if not resp.success:
            print(f'Error: {resp.exception}')


if __name__ == '__main__':
    send_message()
