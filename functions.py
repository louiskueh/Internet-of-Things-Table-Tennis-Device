#ampy --port COM5 put main.py
from machine import Pin, I2C
from umqtt.simple import MQTTClient
import time, ujson,network,machine,ubinascii, math

def difference (x,y):
    dif = abs(x-y)%360
    if dif > 180:
        return 360 - dif
    else :
        return dif
def pikachu():
    print ("░░░░█░▀▄░░░░░░░░░░▄▄███▀░░ ")
    print ("░░░░█░░░▀▄░▄▄▄▄▄░▄▀░░░█▀░░ ")
    print ("░░░░░▀▄░░░▀░░░░░▀░░░▄▀░░░░ ")
    print ("░░░░░░░▌░▄▄░░░▄▄░▐▀▀░░░░░░ ██████╗ ██╗██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗   ██╗")
    print ("░░░░░░▐░░█▄░░░▄█░░▌▄▄▀▀▀▀█ ██╔══██╗██║██║ ██╔╝██╔══██╗██╔════╝██║  ██║██║   ██║")
    print ("░░░░░░▌▄▄▀▀░▄░▀▀▄▄▐░░░░░░█ ██████╔╝██║█████╔╝ ███████║██║     ███████║██║   ██║")
    print ("░░░▄▀▀▐▀▀░░░░░░░▀▀▌▄▄▄░░░█ ██╔═══╝ ██║██╔═██╗ ██╔══██║██║     ██╔══██║██║   ██║")
    print ("░░░█░░░▀▄░░░░░░░▄▀░░░░█▀▀▀ ██║     ██║██║  ██╗██║  ██║╚██████╗██║  ██║╚██████╔╝")
    print ("░░░░▀▄░░▀░░▀▀▀░░▀░░░▄█░░░░ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ")

def start_swing():
    print ("     _             _                  _             ")
    print (" ___| |_ __ _ _ __| |_   _____      _(_)_ __   __ _ ")
    print ("/ __| __/ _` | '__| __| / __\\ \\ /\\ / / | '_ \\ / _` |")
    print ("\\__ \\ || (_| | |  | |_  \\__ \\\\ V  V /| | | | | (_| |")
    print ("|___/\\__\\__,_|_|   \\__| |___/ \\_/\\_/ |_|_| |_|\\__, |")
    print ("                                              |___/ ")

def flat_swing():
    print ("███████╗██╗      █████╗ ████████╗    ███████╗██╗    ██╗██╗███╗   ██╗ ██████╗   ██╗")
    print ("██╔════╝██║     ██╔══██╗╚══██╔══╝    ██╔════╝██║    ██║██║████╗  ██║██╔════╝   ██║")
    print ("█████╗  ██║     ███████║   ██║       ███████╗██║ █╗ ██║██║██╔██╗ ██║██║  ███╗  ██║")
    print ("██╔══╝  ██║     ██╔══██║   ██║       ╚════██║██║███╗██║██║██║╚██╗██║██║   ██║  ╚═╝")
    print ("██║     ███████╗██║  ██║   ██║       ███████║╚███╔███╔╝██║██║ ╚████║╚██████╔╝  ██╗")
    print ("╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝       ╚══════╝ ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝   ╚═╝")

def top_spin():
    print ("████████╗ ██████╗ ██████╗     ███████╗██████╗ ██╗███╗   ██╗  ██╗")
    print ("╚══██╔══╝██╔═══██╗██╔══██╗    ██╔════╝██╔══██╗██║████╗  ██║  ██║")
    print ("   ██║   ██║   ██║██████╔╝    ███████╗██████╔╝██║██╔██╗ ██║  ██║")
    print ("   ██║   ██║   ██║██╔═══╝     ╚════██║██╔═══╝ ██║██║╚██╗██║  ╚═╝")
    print ("   ██║   ╚██████╔╝██║         ███████║██║     ██║██║ ╚████║  ██╗")
    print ("   ╚═╝    ╚═════╝ ╚═╝         ╚══════╝╚═╝     ╚═╝╚═╝  ╚═══╝  ╚═╝")

def compass(angle):
    if angle > 337.5 or angle < 22.5:
        print("  _______")
        print(" /   N   \\")
        print("|    |    |")
        print("|E   |   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 22.5 and angle < 67.5:
        print("  _______")
        print(" /   N   \\")
        print("|     /   |")
        print("|E   /   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 67.5 and angle < 112.5:
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   --- W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 112.5 and angle < 157.5:
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   \   W|")
        print("|     \   |")
        print(" \___S___/")
    elif angle > 157.5 and angle < 202.5:
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   |   W|")
        print("|    |    |")
        print(" \___S___/")
    elif angle > 202.5 and angle < 247.5:
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E   /   W|")
        print("|   /     |")
        print(" \___S___/")
    elif angle > 247.5 and angle < 292.5:
        print("  _______")
        print(" /   N   \\")
        print("|         |")
        print("|E ---   W|")
        print("|         |")
        print(" \___S___/")
    elif angle > 292.5 and angle < 337.5:
        print("  _______")
        print(" /   N   \\")
        print("|   \     |")
        print("|E   \   W|")
        print("|         |")
        print(" \___S___/")



def angle (x,y):
    if y == 0:
        y = 0.000001
    # heading = math.degrees(math.atan(x/y))
    heading = math.atan2(y, x)
    # if (angle < 0):
    #     angle = 90 - angle
    declinationAngle = 0.00756
    heading += declinationAngle

    if heading < 0:
        heading += 2 * 3.1415

    if heading > 2 * 3.1415:
        heading -= 2 * 3.1415

    headingDegrees = heading * 180/ 3.1415

    return headingDegrees

def calibrate (i2c):
    # =============== Calibration ====================
    minX = 9999
    minY = 9999
    maxX = -9999
    maxY = -9999
    t_end = time.time() + 20
    print ('starting calibration. Please move magnetometer in circles for 1 min')
    while time.time() < t_end :
        data = i2c.readfrom_mem(30, 0x03, 6)

        x = twos_complement(int.from_bytes(data[:2], 'big'))
        z = twos_complement(int.from_bytes(data[2:4], 'big'))
        y = twos_complement(int.from_bytes(data[-2:], 'big'))
        # print (str(x) + ', ' + str(y))
        if x < minX:
            print("New minX = " + str(minX))
            minX = x
    	if y < minY:
            print("New minY = " + str(minY))
            minY=y
    	if x > maxX:
            print("New maxX = " + str(maxX))
            maxX=x
    	if y > maxY:
            print("New maxY = " + str(maxY))
            maxY=y
        #i2c.writeto(30, b'\x03')
        time.sleep_ms(100)
    print ('Finished calibration')
    xOffset = (maxX + minX) / 2 ;
    yOffset = (maxY + minY) / 2 ;
    return xOffset,yOffset


def sub_cb(topic, msg):
    print((topic, msg))

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


def setup_cont_M(i2c):

    # print(i2c.scan())                    # scan for slaves, returning a list of 7-bit addresses
    i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    i2c.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    print('Setup successful')
    time.sleep_ms(6)
