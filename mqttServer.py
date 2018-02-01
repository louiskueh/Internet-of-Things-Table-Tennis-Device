import context  # Ensures paho is in PYTHONPATH
import paho.mqtt.subscribe as subscribe

topics = ['#pikachu']

m = subscribe.simple(topics, hostname="ubinascii.hexlify(machine.unique_id())", retained=False, msg_count=2)
for a in m:
    print(a.topic)
    print(a.payload)
