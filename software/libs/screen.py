from machine import I2C
from libs import sh1106


def init():
    # Setup i2c
    i2c = I2C(0, I2C.MASTER, baudrate=100000, pins=('P8', 'P9'))
    # Init OLED Screen
    oled = sh1106.SH1106_I2C(128, 64, i2c)
    oled.rotate(False)
    return oled
