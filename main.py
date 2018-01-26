from machine import Pin, I2C
import timed

def twos_complement(val):
    if (val & (1 << (16 - 1))):
        val = val - (1 << 16)
    return val

def setup_cont_M():
    # print(i2c.scan())                      # scan for slaves, returning a list of 7-bit addresses
    i2c.writeto_mem(30, 0x00, b'\x70')     # 8 Samples, 15 Hz
    i2c.writeto_mem(30, 0x01, b'\xA0')     # gain = 5
    i2c.writeto_mem(30, 0x02, b'\x00')     # Set to continous measurement mode
    time.sleep_ms(6)

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

setup_cont_M()  # Initializecontinuous measurement
while True:
    # Read 6 bytes starting from reg 3  - Reg 3 - 8 contain X Z Y
    data = i2c.readfrom_mem(30, 0x03, 6)

    x = twos_complement(int.from_bytes(data[:2], 'big'))
    z = twos_complement(int.from_bytes(data[2:4], 'big'))
    y = twos_complement(int.from_bytes(data[-2:], 'big'))

    print (str(x) + ', ' + str(y) + ', ' + str(z))
    i2c.writeto(30, b'\x03')
    time.sleep_ms(100)
