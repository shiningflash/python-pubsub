# [python-pubsub](https://github.com/shiningflash/python-pubsub)

## 1. [Using Google Cloud Service (project: smart home)](https://github.com/shiningflash/python-pubsub/tree/main/smart_home)

We're going to enable Google Cloud Platform's Pub/Sub API and write a publisher and a subscriber in Python. Then we're going to allow for more than just string data to be sent.

Something to keep in mind is that Pubsub is almost always a nice-to-have. It's not a necessity. We use it to build a workflow with websites and cloud hosting, passing messages between services that otherwise don't talk to each other. Pubsub's great at storing our topic messages and letting cloud functions trigger and fire to keep a workflow running.

### Set up google cloud

---

1. go to [google cloud console](https://console.cloud.google.com/).
2. search pub/sub and go to pub/sub.
3. create a topic. It will create a subscriptions also. (If not created automatically, create one.)
4. go to Navigation Menu >> IAM & Admin >> Service Accounts. Create a service account.
5. go to the newly created service account >> KEYS. Create a new key and download. This is your private key. (Don't share it to anyone, otherwise they can access your account.) Move the private to your project repository folder.

You're ready to go!!!

### Requirements

---

```
$ pip3 install --upgrade google-cloud-pubsub
```

### Run code

---

```
$ python3 publisher.py
$ python3 subscriber.py
```

## 2. [Using Redis (project: control center)](https://github.com/shiningflash/python-pubsub/tree/main/control_center)

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
