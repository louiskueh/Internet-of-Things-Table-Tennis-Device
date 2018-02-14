from machine import Pin, I2C
from math import sqrt
from time import sleep_ms
import functions, acc, mag

#========== functions =============
# Twos complement
# MQTT send/receive
# Connect to wifi

#========== acc ===============
# accelerometer API

#========== mag ===============
# magnetometer api



# Main function to detect change in angle within 300ms
def start (client):
    n = 0
    while n < 3:
        x, y, z = mag.readXYZ(i2c)
        xy = mag.angle(x,y)
        xz = mag.angle(x,z)
        yz = mag.angle(y,z)

        if n == 0:
            print ('Calculating...')
            inxy = xy
            inxz = xz
            inyz = yz

        if n == 2:
            print ('Result:')
            yzd = mag.difference(yz,inyz)
            xyd = mag.difference(xy,inxy)
            xzd = mag.difference(xz,inxz)

            if yzd >= 50 and xyd <=50 and xzd <= 50:
                functions.mqttSend('s',1,client)
                print ('flat swing')

            elif yzd >=29 and xy >= 56 and xzd >= 13:
                functions.mqttSend('s',2,client)
                print('top spin')
            else:
                functions.mqttSend('s',0,client)
                print ('Angle achieved = ' + str(yzd))
                print ('No swing detected')
                return 0

        n += 1
        sleep_ms(150)

#=================================Start program ============================
# Initialize i2c
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# Connect to wifi
functions.do_connect()

# Initializecontinuous measurement
mag.setup_cont(i2c)

# Initialize accelerometer
acc.setup(i2c)

# Calibration (currently not needed for angle measurement)
#xOffset , yOffset = 0,0
#functions.calibrate(i2c)

#Setup mqtt client, ensure you are connected to EE Rover
client = functions.mqttConnect()

input("PLEASE PRESS ENTER TO START")
print('ready')

pressed = 1;
while True :
    #button pressed will swap pressed value
    #pressed = 1 - we are measuring swings
    #pressed = 0 - we are using the compass mode
    first = Pin(12, Pin.IN, Pin.PULL_UP).value()
    if first:
        sleep_ms(10)
        second = Pin(12, Pin.IN, Pin.PULL_UP).value()
        if first and not second:
            pressed = not pressed
            print('Button pressed')

    if pressed == 1:
        if acc.magnitude(i2c) > 150:
            start(client)
    if pressed == 0:
        x, y, z = mag.readXYZ(i2c)
        functions.mqttSend('c',mag.angle(x,y),client)

        sleep_ms(50)
