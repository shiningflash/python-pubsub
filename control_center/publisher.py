import sys

import redis

if __name__ == '__main__':
    if len(sys.argv) == 3:
        program, environment, action = sys.argv
        client = redis.Redis(host='127.0.0.1', port=6379)
        client.publish(environment, action)
    else:
        print("Please provide an environment, and an action!!")
