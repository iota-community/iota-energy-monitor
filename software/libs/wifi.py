import utime
import machine
from network import WLAN

from libs import kv
from libs import screen

import socket
import ssl
import time


## Setup WiFi
def connect_wifi(network, password, oled):
    wlan = WLAN()
    wlan.deinit()
    wlan.init(mode=WLAN.STA)
    wlan.ifconfig(config=('dhcp'))

    wlan.scan()  # scan for available networks
    wlan.connect(ssid=network, auth=(WLAN.WPA2, password))

    for _ in range(15):
        if wlan.isconnected():
            print("Joining Success")
            # Boot Text with version
            oled.fill(0)
            oled.text("Connected to:", 0, 0)
            oled.text(network, 0, 15)
            oled.text("IP Address:", 0, 40)
            oled.text(wlan.ifconfig()[0], 0, 55)
            oled.show()
            utime.sleep_ms(1000)
            return
        else:
            # Boot Text with version
            oled.fill(0)
            oled.text("Connecting to:", 0, 0)
            oled.text(network, 0, 15)
            oled.show()
            utime.sleep_ms(1000)

    # WiFi Creds probably broken
    print("Can't Join Clearing Credentials")
    kv.set("AP_PWD", False)
    kv.set("AP_SSID", False)

    oled.fill(0)
    oled.text("Failed to", 0, 0)
    oled.text("connect to:", 0, 15)
    oled.text(network, 0, 30)
    oled.text("Rebooting", 0, 55)
    oled.show()
    utime.sleep_ms(3000)
    machine.reset()


def create_wifi():
    print("Setting up WiFi")
    wlan = WLAN(mode=WLAN.AP,
                ssid='IOTA-CXC-MODULE',
                auth=(None),
                channel=7,
                antenna=WLAN.INT_ANT)
    wlan.ifconfig(config=('192.168.4.1', '255.255.255.0', '192.168.4.1',
                          '8.8.8.8'))
    print(wlan.ifconfig())