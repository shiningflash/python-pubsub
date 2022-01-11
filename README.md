# python-pubsub

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
$ pip install --upgrade google-cloud-pubsub
```

### Run code

---

```
$ python3 publisher.py
$ python3 subscriber.py
```
