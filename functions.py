#ampy --port COM5 put main.py
from machine import Pin, I2C
from umqtt.simple import MQTTClient
import time, ujson, network, machine, ubinascii, math

#==================Additional functions========================
# Twos complement
# MQTT send/receive
# Connect to wifi

def sqroot(x, y):
    return sqrt(x, y)

def sub_cb(topic, msg):
    print((topic, msg))

def twos_complement(val):
    if (val & (1 << (16 - 1))):
        val = val - (1 << 16)
    return val

def twos_complement12(val):
    if (val & (1 << (12 - 1))):
        val = val - (1 << 12)
    return val
def mqttConnect():
    CLIENT_ID = ubinascii.hexlify(machine.unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"
    # End
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS,port = 1883)
    client.connect()
    print ('connected to broker sucessfully')
    time.sleep_ms(100)
    return client

def mqttSend(name,val,client):
    dict = {name : val}
    jsonString = ujson.dumps(dict)
    CLIENT_ID = ubinascii.hexlify(machine.unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"
    client.publish(TOPIC, bytes (jsonString, 'utf-8'))
    #print ('sent: hi with topic: ' + str(TOPIC)  )
    print ('sent: ' + jsonString + str(TOPIC))

# def mqttSend(x,y,z):
#     # X Y Z to json
#     dict = {'yzd' : x, 'xyd':y, 'xzd':z  }
#     jsonString = ujson.dumps(dict)
#     CLIENT_ID = ubinascii.hexlify(machine.unique_id())
#     #BROKER_ADDRESS = "192.168.0.10"
#     BROKER_ADDRESS = "192.168.0.87"
#     TOPIC = b"pikachu/cw"
#
#     # End
#     client = MQTTClient(CLIENT_ID,BROKER_ADDRESS,port = 1883)
#     client.connect()
#     #client.publish(TOPIC,b"hi")
#     client.publish(TOPIC, bytes (jsonString, 'utf-8'))
#     #print ('sent: hi with topic: ' + str(TOPIC)  )
#     print ('sent: ' + jsonString + str(TOPIC))

## Receive data from broker
def mqttReceive():

    CLIENT_ID = ubinascii.hexlify(machine.unique_id())
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
            time.sleep(1)

    c.disconnect()

def do_connect():
    import network
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    time.sleep_ms(100)
    sta_if.connect('EEERover', 'exhibition')

    # Needed for reliable setup
    time.sleep_ms(2000)

    # reattempt network conneciton until success
    while sta_if.isconnected() == False:
        print("Attempting to re-connect to network")
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        time.sleep_ms(100)
        sta_if.connect('EEERover', 'exhibition')
        #Needed for setup
        time.sleep_ms(2000)
    print('Network connected:', sta_if.isconnected())
