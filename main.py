from machine import Pin,I2C
import time
print('Pikachu')
     # create I2C peripheral at frequency of 400kHz
                                # depending on the port, extra parameters may be required
                                # to select the peripheral and/or pins to use

i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

print(i2c.scan())                      # scan for slaves, returning a list of 7-bit addresses


# i2c.writeto(30, b'3932272')         # write 3 bytes to slave with 7-bit address 42
# i2c.readfrom(42, 4)             # read 4 bytes from slave with 7-bit address 42
#
# i2c.readfrom_mem(42, 8, 3)      # read 3 bytes from memory of slave 42,
#                                 #   starting at memory-address 8 in the slave
# i2c.writeto_mem(42, 2, b'\x10') # write 1 byte to memory of slave 42
#                                 #   starting at address 2 in the slave
# i2c.writeto_mem(30, 0x00, b'\x70')
# i2c.writeto_mem(30, 0x01, b'\xA0')
i2c.writeto_mem(30, 0x00, b'\x70')
i2c.writeto_mem(30, 0x01, b'\xA0')
i2c.writeto_mem(30, 0x02, b'\x00')

time.sleep_ms(6)
print ('written to mem')
def twos_complement (val):
    if (val & (1 << (16 - 1))):
        val = val - (1 << 16)
        #print ('Two\'s Complement activated')
    return val
while True:
    data = i2c.readfrom_mem(30, 0x06, 6)
    #intdata = int.from_bytes(data,’big’)

    x = twos_complement(int.from_bytes(data[:2],'big'))
    z = twos_complement(int.from_bytes(data[2:4],'big'))
    y = twos_complement(int.from_bytes(data[-2:],'big'))
    #x =int.from_bytes(x,’big’)
    # y = data[2:4]
    # z = data [:2
    print (str(x) + ', ' + str(y) + ', ' + str(z))
    #time.sleep(1)
    #i2c.writeto_mem(30, 0x02, b'\x00')
