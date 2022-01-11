import os
from concurrent.futures import TimeoutError

from google.cloud import pubsub_v1

credentials_path = '/Users/mac/python-pubsub/smart_home/mysticcurve_privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

subscriber = pubsub_v1.SubscriberClient()
subscription_path = 'projects/mystic-curve-337915/subscriptions/env-sensors-sub'

timeout = 15.0   # timeout in seconds


def callback(message):
    print(f'Received message: {message}')
    print(f'data: {message.data}')
    
    if message.attributes:
        print('Attributes')
        for key in message.attributes:
            value = message.attributes.get(key)
            print(f'{key}: {value}')
    
    message.ack()


def pull_data():
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f'Listening for message on {subscription_path}')
    return streaming_pull_future


if __name__ == '__main__':
    streaming_pull_future = pull_data()
    with subscriber:
        try:
            streaming_pull_future.result()  # without a timeout, it will wait and block
        except TimeoutError:
            streaming_pull_future.cancel()  # trigger shutdown
            streaming_pull_future.result()  # block until the shutdown
        
