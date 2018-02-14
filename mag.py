from machine import Pin, I2C
from math import atan2
from time import sleep_ms,time
import functions
# magnetometer

def difference (x,y):
    dif = abs(x-y)%360
    if dif > 180:
        return 360 - dif
    else :
        return dif

def angle (x,y):
    if y == 0:
        y = 0.000001
    # heading = math.degrees(math.atan(x/y))
    heading = atan2(y, x)
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
    t_end = time() + 20
    print ('starting calibration. Please move magnetometer in circles for 1 min')
    while time() < t_end :
        data = i2c.readfrom_mem(30, 0x03, 6)

        x = functions.twos_complement(int.from_bytes(data[:2], 'big'))
        z = functions.twos_complement(int.from_bytes(data[2:4], 'big'))
        y = functions.twos_complement(int.from_bytes(data[-2:], 'big'))
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
        sleep_ms(100)
    print ('Finished calibration')
    xOffset = (maxX + minX) / 2 ;
    yOffset = (maxY + minY) / 2 ;
    return xOffset,yOffset

def readXYZ(i2c):
    # Read 6 bytes starting from reg 3  - Reg 3 - 8 contain X Z Y
    data = i2c.readfrom_mem(30, 0x03, 6)

    x = functions.twos_complement(int.from_bytes(data[:2], 'big')) #- xOffset
    z = functions.twos_complement(int.from_bytes(data[2:4], 'big'))
    y = functions.twos_complement(int.from_bytes(data[-2:], 'big')) #- yOffset

    return  x, y, z

def setup_cont(i2c):
    # print(i2c.scan())                    # scan for slaves, returning a list of 7-bit addresses
    i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    i2c.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    print('Setup successful')
    sleep_ms(6)
