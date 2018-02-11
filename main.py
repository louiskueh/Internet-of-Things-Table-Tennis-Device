from machine import Pin, I2C
import time, functions

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# Connect to wifi
#functions.do_connect()

# Initializecontinuous measurement
functions.setup_cont_M(i2c)


xOffset,yOffset = 0,0#functions.calibrate(i2c)
print ('x y offset = ' + str(xOffset) +' , ' + str(yOffset))


functions.pikachu()

def start ():
    n = 0
    while n< 11:
        # Read 6 bytes starting from reg 3  - Reg 3 - 8 contain X Z Y
        data = i2c.readfrom_mem(30, 0x03, 6)

        x = functions.twos_complement(int.from_bytes(data[:2], 'big')) -xOffset
        z = functions.twos_complement(int.from_bytes(data[2:4], 'big'))
        y = functions.twos_complement(int.from_bytes(data[-2:], 'big')) - yOffset

        #print ("json: " + mqttSend(x,y,z) )
        #functions.mqttReceive()
        #mqttSend(x,y,z)
        # print (str(x) + ', ' + str(y) + ', ' + str(z))
        # print (str(x) + ', ' + str(y))
        # print ('magnitude = ' + str(math.sqrt(x*x + y*y)) )
        xy = functions.angle(x,y)
        xz = functions.angle(x,z)
        yz = functions.angle(y,z)
        # print ('XY:' + str(xy) + ',        XZ:' + str(functions.angle(x,z)) + ' ,       YZ:' + str(functions.angle(y,z)) )
        # functions.compass(xy);
        # functions.compass(yz);
        # functions.compass(xz);
        if n == 0:
            inxy = xy
            inxz = xz
            inyz = yz
        if n == 10:

            # if xy >= 310 or xy <= 50 or inxy >= 310 or inxy <= 50:
            #     xy = (xy+150)%360
            #     inxy = (inxy+150)%360
            # if yz >= 310 or yz <= 50 or inyz >= 310 or inyz <= 50:
            #     yz = (yz+150)%360
            #     inyz = (inyz+150)%360
            # if xz >= 310 or xz <= 50 or inxz >= 310 or inxz <= 50:
            #     xz = (xz+150)%360
            #     inxz = (inxz+150)%360

            print('angle measured yz: ' + str(abs(yz-inyz)) +' xy: ' + str(abs(xy - inxy)) + ' yz: ' + str(abs(yz - inyz)))
            if abs(yz-inyz) >= 40 :
            #and abs(xy - inxy) <=50 and abs(yz - inyz) <= 50:
                functions.flat_swing()
                return 1
            else:
                print('You failed the flat swing. You angle was ' + str(abs(yz-inyz)))
                print ('Please ensure you swing from your waist to the front of your body.Your deviation from a proper flat swing is : '
                + str(50 - abs(yz-inyz))  )
                return 0
        n += 1
        i2c.writeto(30, b'\x03')
        time.sleep_ms(150)


input("PLEASE PRESS ENTER TO START")
flatCount = 0

while True :
    functions.start_swing()
    flatCount = flatCount +start()
    print ('flatCount: ' + str(flatCount) )
    print('wait for a while before swinging')
    time.sleep_ms(1500)
