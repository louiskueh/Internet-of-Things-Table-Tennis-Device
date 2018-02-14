#ampy --port COM5 put main.py
from machine import Pin, I2C
from umqtt.simple import MQTTClient
from ubinascii import hexlify
from machine import unique_id
#check network
from network import WLAN,AP_IF,STA_IF
from time import sleep_ms
from ujson import dumps

#==================Additional functions========================
# Twos complement
# MQTT send/receive
# Connect to wifi

def sub_cb(topic, msg):
    print((topic, msg))

#16 bit twos complement (magnetometer)
def twos_complement(val):
    if (val & (1 << (16 - 1))):
        val = val - (1 << 16)
    return val

#12 bit twos complement (accelerometer)
def twos_complement12(val):
    if (val & (1 << (12 - 1))):
        val = val - (1 << 12)
    return val

def mqttConnect():
    CLIENT_ID = hexlify(unique_id())
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS,port = 1883)
    client.connect()
    print ('connected to broker sucessfully')
    sleep_ms(100)
    return client

def mqttSend(name,val,client):
    dict = {name : val}
    jsonString = dumps(dict)
    CLIENT_ID = hexlify(unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"
    client.publish(TOPIC, bytes (jsonString, 'utf-8'))
    print ('sent: ' + jsonString + str(TOPIC))

# Send 3 data
def mqttSend3(x,y,z,client):
    dict = {'XY': x, 'YZ':y, 'XZ':z}
    jsonString = dumps(dict)
    CLIENT_ID = hexlify(unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"
    client.publish(TOPIC, bytes (jsonString, 'utf-8'))
    print ('sent: ' + jsonString + str(TOPIC))
## Receive data from broker
def mqttReceive():

    CLIENT_ID = hexlify(unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    c =  MQTTClient(CLIENT_ID,BROKER_ADDRESS,port = 1883)
    print ('Waiting to recieve')
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(b"pikachu/rec")
    while True:
        if True:
            # Blocking wait for message
            c.wait_msg()
        else:
            # Non-blocking wait for message
            c.check_msg()
            # Then need to sleep to avoid 100% CPU usage (in a real
            # app other useful actions would be performed instead)
            sleep_ms(1000)

    c.disconnect()

def do_connect():
    ap_if = WLAN(AP_IF)
    ap_if.active(False)
    sta_if = WLAN(STA_IF)
    sta_if.active(True)
    sleep_ms(100)
    sta_if.connect('EEERover', 'exhibition')

    # Needed for reliable setup
    sleep_ms(2000)

    # reattempt network conneciton until success
    while sta_if.isconnected() == False:
        print("Attempting to re-connect to network")
        ap_if = WLAN(AP_IF)
        ap_if.active(False)
        sta_if = WLAN(STA_IF)
        sta_if.active(True)
        sleep_ms(100)
        sta_if.connect('EEERover', 'exhibition')
        #Needed for setup
        sleep_ms(2000)
    print('Network connected:', sta_if.isconnected())
