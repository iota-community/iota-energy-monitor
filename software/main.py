import utime
import machine
import socket
import ssl
import time

from network import WLAN
from network import LTE
from libs import rgbled
from libs import kv
from libs import screen
from libs import wifi
from libs import emonlib
from libs import urequests

adc = machine.ADC()  # create an ADC object

emon1 = emonlib.Emonlib()
config = kv.getAll()
print(config)

rgbled.init()
rgbled.green()

oled = screen.init()


def getCurrent():
    print("Fetching")
    emon1.current("P16", 144.43)
    return emon1.calc_current_rms(1480)


def main():
    while True:
        amps = getCurrent()
        watts = amps / 1000 * 240
        print("Current MilliAmps: ", amps)
        print("Current Watts: ", amps / 1000 * 240)
        oled.fill(0)
        if watts > 5:
            oled.text("PowerConsumption", 0, 0)
            oled.text("Watts: {}".format(watts), 0, 15)

            response = urequests.request(
                "POST", "http://{}:{}/produce".format(config['IOTA_ENDPOINT'],
                                                      config['IOTA_PORT']),
                '{"uuid": "{}","energy":'.format(config['IOTA_UUID']) +
                str(watts) + '}', None, {
                    "Content-Type": "application/json"
                }).text
            print(response)
        else:
            oled.text("Please connect", 0, 0)
            oled.text("CT Clamp", 0, 15)
        oled.show()

        utime.sleep_ms(10000)


if config['AP_SSID'] == False:
    # Display instructions
    oled.fill(0)
    oled.text("Setting up", 0, 0)
    oled.text("WiFi network", 0, 15)
    oled.show()
    #Start WiFi Station for config updates
    wifi.create_wifi()

    # Import and Start Webserver
    import webserver
    server = webserver.init()
    server.StartManaged()

    # Display instructions
    oled.fill(0)
    oled.text("Join WiFi:", 0, 0)
    oled.text("IOTA-CXC-MODULE", 0, 15)
    oled.text("Navigate to:", 0, 40)
    oled.text("192.168.4.1", 0, 55)
    oled.show()
    utime.sleep_ms(1000)

else:
    wifi.connect_wifi(config['AP_SSID'], config['AP_PWD'], oled)
    print("Connected to WiFi")
    main()
