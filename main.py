from machine import Pin, I2C
import time,functions

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# Connect to wifi
#functions.do_connect()

# Initializecontinuous measurement
functions.setup_cont_M(i2c)
while True:
    # Read 6 bytes starting from reg 3  - Reg 3 - 8 contain X Z Y
    data = i2c.readfrom_mem(30, 0x03, 6)

    x = functions.twos_complement(int.from_bytes(data[:2], 'big'))
    z = functions.twos_complement(int.from_bytes(data[2:4], 'big'))
    y = functions.twos_complement(int.from_bytes(data[-2:], 'big'))
    #print ("json: " + mqttSend(x,y,z) )
    #functions.mqttReceive()
    #mqttSend(x,y,z)
    #print (str(x) + ', ' + str(y) + ', ' + str(z))
    print (str(x) + ', ' + str(y))
    i2c.writeto(30, b'\x03')
    time.sleep_ms(100)
