from machine import Pin, I2C
import math, time,functions
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

print(i2c.scan())
#Send actiave 400hx, high resolution enable xyz
i2c.writeto_mem(24,0x20,b'0x77')
# Continous measurement
i2c.writeto_mem(24,0x23,b'0x38')




def readACC(adr1,adr2):
    #0x28,0x29
    acc_l = i2c.readfrom_mem(24, adr1, 1)
    acc_h = i2c.readfrom_mem(24, adr2, 1)
    h = int.from_bytes(acc_h,'big')
    l =int.from_bytes(acc_l,'big')
    acc_combined = round(((h * 2**8) | l )/(2**4))
    print ('combined: ' + str(acc_combined))
    return functions.twos_complement(acc_combined)
#
# def readACCy():
#     acc_l = i2c.readfrom_mem(24, 0x2A, 1)
#     acc_h = i2c.readfrom_mem(24, 0x2B, 1)
#     acc_combined = (acc_l | acc_h << 8)
#
#     return acc_combined  if acc_combined < 32768 else acc_combined - 65536
#
# def readACCz():
#     acc_l = i2c.readfrom_mem(24, 0x2C, 1)
#     acc_h = i2c.readfrom_mem(24, 0x2D, 1)
#     acc_combined = (acc_l | acc_h << 8)
#
#     return acc_combined  if acc_combined < 32768 else acc_combined - 65536


while True:
    ACCx = readACC(0x28,0x29)
    ACCy = readACC(0x2A,0x2B)
    ACCz = readACC(0x2C,0x2D)
    #status = print(i2c.readfrom_mem(24, 0x27, 1))
    print(i2c.readfrom_mem(24,0x24,1))
    print ("ACCx: " + str((ACCx* 0.244)/1000) + "ACCy: " + str((ACCy* 0.244)/1000) + "ACCz: " + str((ACCz* 0.244)/1000) )
    time.sleep_ms(100)
                  # scan for slaves, returning a list of 7-bit addresses
    # i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    # i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    # i2c,.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    # print('Setup successful')
    # time.sleep_ms(6)
    # i2c.writeto_mem
    # data = i2c.readfrom_mem(30, 0x03, 6)
    #
    # x = twos_complement(int.from_bytes(data[:2], 'big'))
    # z = twos_complement(int.from_bytes(data[2:4], 'big'))
    # y = twos_complement(int.from_bytes(data[-2:], 'big'))
    #
    # i2c.writeto(30, b'\x03')
    # time.sleep_ms(100)
