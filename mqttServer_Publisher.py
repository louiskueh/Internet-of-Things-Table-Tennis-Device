#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
# This is the Publisher

client = mqtt.Client()
client.connect("192.168.0.87",1883,60)
i = 0
while i<100:
    client.publish("pikachu/rec", i);
    print("sent")
    i = i+1
    time.sleep(0.1)
client.disconnect();
