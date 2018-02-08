from machine import Pin, I2C
from umqtt.simple import MQTTClient
import time, ujson,network,machine,ubinascii

def sub_cb(topic, msg):
    print((topic, msg))
#ampy --port COM5 put main.py
def twos_complement(val):
    if (val & (1 << (16 - 1))):
        val = val - (1 << 16)
    return val

def mqttSend(x,y,z):
    # X Y Z to json
    dict = {'X' : x, 'Y':y, 'Z':z  }
    jsonString = ujson.dumps(dict)
    CLIENT_ID = ubinascii.hexlify(machine.unique_id())
    #BROKER_ADDRESS = "192.168.0.10"
    BROKER_ADDRESS = "192.168.0.87"
    TOPIC = b"pikachu/cw"

    # End
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS,port = 1883)
    client.connect()
    #client.publish(TOPIC,b"hi")
    client.publish(TOPIC, bytes (jsonString, 'utf-8'))
    #print ('sent: hi with topic: ' + str(TOPIC)  )
    print ('sent: ' + jsonString + str(TOPIC))
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
    #Needed for setup
    time.sleep_ms(2000)
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


def setup_cont_M(i2c):

    # print(i2c.scan())                    # scan for slaves, returning a list of 7-bit addresses
    i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    i2c.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    print('Setup successful')
    time.sleep_ms(6)
