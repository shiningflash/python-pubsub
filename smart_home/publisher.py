import os

from google.cloud import pubsub_v1

credentials_path = '/Users/mac/python-pubsub/smart_home/mysticcurve_privatekey.json'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

publisher = pubsub_v1.PublisherClient()
topic_path = 'projects/mystic-curve-337915/topics/env-sensors'


def send_clearance():
    data = "The house is safe. All good."
    data = data.encode('utf-8')
    
    attributes = {
        'sensorName': 'home-001',
        'temperature': '72.0',
        'humadity': '60'
    }
    
    future = publisher.publish(topic_path, data, **attributes)
    print('Published message id', future.result())


if __name__ == '__main__':
    send_clearance()
