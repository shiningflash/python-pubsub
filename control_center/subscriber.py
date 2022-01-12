import redis

environment = 'dev'

if __name__ == '__main__':
    client = redis.Redis(host='127.0.0.1', port=6379)
    ps = client.pubsub()
    ps.subscribe(environment)
    
    while True:
        message = ps.get_message()
        if message and not message.get('data') == 1:
            print(message.get('data').decode('utf-8'))
