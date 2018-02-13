from machine import Pin, I2C
from math import sqrt
import  time, functions, acc, mag, text

# Initialize
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

# Connect to wifi
#functions.do_connect()

# Initializecontinuous measurement
mag.setup_cont(i2c)

# Initialize accelerometer
acc.setup(i2c)

xOffset , yOffset = 0,0#functions.calibrate(i2c)

def start ():
    n = 0
    while n < 3:
        x, y, z = mag.readXYZ(i2c)

        #print ("json: " + mqttSend(x,y,z) )
        #functions.mqttReceive()
        #mqttSend(x,y,z)
        # print (str(x) + ', ' + str(y) + ', ' + str(z))
        # print (str(x) + ', ' + str(y))
        # print ('magnitude = ' + str(math.sqrt(x*x + y*y)) )
        xy = mag.angle(x,y)
        xz = mag.angle(x,z)
        yz = mag.angle(y,z)
        # print ('XY:' + str(xy) + ',        XZ:' + str(functions.angle(x,z)) + ' ,       YZ:' + str(functions.angle(y,z)) )
        # functions.compass(xy);
        # functions.compass(yz);
        # functions.compass(xz);

        if n == 0:
            # text.start_swing()
            print ('Calculating...')
            inxy = xy
            inxz = xz
            inyz = yz

        if n == 2:
            print ('Result:')
            yzd = mag.difference(yz,inyz)
            xyd = mag.difference(xy,inxy)
            xzd = mag.difference(xz,inxz)
            #print('angles yz: ' + str(yzd) +' xy: ' + str(xyd) + ' yz: ' +str(xzd) )
            # print (str(yzd) + ','+ str(xyd) + ',' + str(xzd))
            if yzd >= 50 and xyd <=50 and xzd <= 50:
                text.flat_swing()
                #print ('angle achieved :' + str(yzd))
                global flatCount
                flatCount += 1

            elif yzd >=29 and xy >= 56 and xzd >= 13:
                text.top_spin()
            else:
                # print ('yz :' + str(yzd) + ' xy: ' + str(xyd) + ' xz: ' + str(xzd))
                print ('Angle achieved = ' + str(yzd))
                print ('No swing detected')
                # print ('Deviation      = ' + str(40 - yzd))
                # print ('Please ensure you swing from your waist to the front of your body.')
                return 0

        # i2c.writeto(30, b'\x03')
        n += 1
        time.sleep_ms(150)

#=================================Start program ==================
text.pikachu()
flatCount = 0
input("PLEASE PRESS ENTER TO START")
text.ready()

pressed = 1;

while True :
    first = Pin(12, Pin.IN, Pin.PULL_UP).value()
    if first:
        time.sleep(0.01)
        second = Pin(12, Pin.IN, Pin.PULL_UP).value()
        if first and not second:
            pressed = not pressed
            text.ready()

    if pressed == 1:
        if acc.magnitude(i2c) > 150:
            start()
            text.ready()
    if pressed == 0:
        print ('fake compass')
        # x,y,z = mag.readXYZ(i2c)
        # xy = mag.angle(x,y)
        # xz = mag.angle(x,z)
        # yz = mag.angle(y,z)
        # print ('xy')
        # text.compass(xy)
        # print ('xz')
        # text.compass(xz)
        # print ('yz')
        # text.compass(yz)
        # time.sleep_ms(400)





    # flatCount = flatCount + start()
    # print ('flatCount: ' + str(flatCount) )
    # print('wait for a while before swinging')
    # acc.readXYZ(i2c)
    # print ('===============')
    # print ('')
    # print ('')

    # x,y,z = mag.readXYZ(i2c)
    # xy = mag.angle(x,y)
    # xz = mag.angle(x,z)
    # yz = mag.angle(y,z)
    # print ('xy')
    # text.compass(xy)
    # print ('xyz')
    # text.compass(xz)
    # print ('yz')
    # text.compass(yz)
    # time.sleep_ms(400)
