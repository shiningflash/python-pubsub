# [Pub/Sub :: Using Redis (project: control center)](https://github.com/shiningflash/python-pubsub/tree/main/control_center)

This video is about the PUB/SUB feature of redis which allows you create message queues, and it could even be utilized to create a small control center in which the clients perform operations based on the channels they are subscribed to.

### Set up Redis

---

I am showing commands to install redis in mac. For linux and windows user, please, learn from internet if redis is not present in your device.

```
$ brew update
$ brew install redis
```

To start redis, `$ brew services start redis`.
To stop redis, `$ brew services stop redis`.
To test redis, `$ redis-cli ping`. It will response with 'PONG`, if everything is good! To go to redis config file, `$ nano /usr/local/etc/redis.conf`.

You're ready to go!!

### Requirements

---

```
$ pip3 install redis
```

### Run code

---

```
$ python3 publisher.py <environment_name> <action_name>
$ python3 subscriber.py
```

For example, `$ python3 publisher.py dev 'stop server'`.

---
