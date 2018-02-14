from machine import Pin, I2C
from math import sqrt
import functions

REG_CTRL1       = const(0x20)
REG_CTRL3       = const(0x22)
REG_CTRL4       = const(0x23)
REG_CTRL5       = const(0x24)
REG_OUT_X_L     = const(0x28)

#==================accelerometer========================
# Setup and read readXYZ


def setup(i2c):
    i2c.writeto_mem(24,REG_CTRL5, b'0xC0')
    # Enable all axes, normal mode.,     Set 400Hz data rate.
    i2c.writeto_mem(24,REG_CTRL1, b'0x57')
    # High res & BDU enabled.
    i2c.writeto_mem(24,REG_CTRL4, b'0x88')

def readACC(adr1,adr2,i2c):
    #0x28,0x29
    acc_l = i2c.readfrom_mem(24, adr1, 1)
    acc_h = i2c.readfrom_mem(24, adr2, 1)

    h = int.from_bytes(acc_h,'big')
    l =int.from_bytes(acc_l,'big')
    acc_combined = round(((h * 2**8) | l )/(2**4))
    #print ('combined: ' + str(acc_combined))
    return functions.twos_complement12(acc_combined)
def magnitude(i2c):
    ACCx = readACC(0x28,0x29,i2c)
    ACCy = readACC(0x2A,0x2B,i2c)
    ACCz = readACC(0x2C,0x2D,i2c)
    # print ("Magnitude : " + str(math.sqrt(pow(ACCx,2) + pow (ACCy,2) + pow(ACCz,2))) )
    return sqrt(pow(ACCx,2) + pow (ACCy,2) + pow(ACCz,2))
def readXYZ(i2c):
    ACCx = readACC(0x28,0x29,i2c)
    ACCy = readACC(0x2A,0x2B,i2c)
    ACCz = readACC(0x2C,0x2D,i2c)
    #data = i2c.readfrom_mem(24, REG_OUT_X_L | 0x80, 6)
    #status = print(i2c.readfrom_mem(24, 0x27, 1))
    print ("ACCx: " + str(round(ACCx)) + "   ACCy: " + str(round(ACCy)) + "  ACCz: " + str(round(ACCz) ))
    print ("Magnitude : " + sqrt(pow(ACCx,2) + pow (ACCy,2) + pow(ACCz,2)) )
    return ACCx, ACCy, ACCz
