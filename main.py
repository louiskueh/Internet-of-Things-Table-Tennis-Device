from machine import Pin, I2C
from umqtt.simple import MQTTClient
import time, ujson,network,machine,ubinascii

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
    BROKER_ADDRESS = "192.168.0.10"
    TOPIC = b"#pikachu"

    # End
    client = MQTTClient(CLIENT_ID,BROKER_ADDRESS)
    client.connect()
    client.publish(TOPIC, bytes (jsonString, 'utf-8'))
    print ('sent: ' + jsonString )

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
        print("Attempting to re-connect to work")
        ap_if = network.WLAN(network.AP_IF)
        ap_if.active(False)
        sta_if = network.WLAN(network.STA_IF)
        sta_if.active(True)
        time.sleep_ms(100)
        sta_if.connect('EEERover', 'exhibition')
        #Needed for setup
        time.sleep_ms(2000)
    print('Network connected:', sta_if.isconnected())


def setup_cont_M():
    # print(i2c.scan())                      # scan for slaves, returning a list of 7-bit addresses
    i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    i2c.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    time.sleep_ms(6)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# Connect to wifi
do_connect()

setup_cont_M()  # Initializecontinuous measurement

while True:
    # Read 6 bytes starting from reg 3  - Reg 3 - 8 contain X Z Y
    data = i2c.readfrom_mem(30, 0x03, 6)

    x = twos_complement(int.from_bytes(data[:2], 'big'))
    z = twos_complement(int.from_bytes(data[2:4], 'big'))
    y = twos_complement(int.from_bytes(data[-2:], 'big'))
    #print ("json: " + mqttSend(x,y,z) )
    mqttSend(x,y,z)
    #print (str(x) + ', ' + str(y) + ', ' + str(z))
    i2c.writeto(30, b'\x03')
    time.sleep_ms(100)
