import pycom


def init():
    pycom.heartbeat(False)  # disable the heartbeat LED


def green():
    pycom.rgbled(0xff00)  # make the LED light up in g


def yellow():
    pycom.rgbled(0x7f7f00)  # yellow


def red():
    pycom.rgbled(0x7f0000)  # yellow


def off():
    pycom.heartbeat(True)  # disable the heartbeat LED
    pycom.heartbeat(False)  # disable the heartbeat LED