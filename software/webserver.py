from libs.MicroWebSrv2 import *
from time import sleep
from _thread import allocate_lock
import ujson
import utime
import machine
from libs import kv

ssid = False
pwd = False


@WebRoute(GET, '/', name='TestPost1/2')
def RequestTestPost(microWebSrv2, request):
    content = """\
    <!DOCTYPE html>
    <html>
        <head>
            <title>Setup WiFi</title>
        </head>
        <body>
            <h2>CxC Energy Monitor - WiFi Setup</h2>
            Please enter WiFi settings, to connect the module to the internet.<br />
            <form action="/" method="post">
                Name: <input type="text" name="ssid"><br />
                Password:  <input type="text" name="pwd"><br />
                <input type="submit" value="Submit">
            </form>
        </body>
    </html>
    """
    request.Response.ReturnOk(content)


# ------------------------------------------------------------------------


@WebRoute(POST, '/', name='TestPost2/2')
def RequestTestPost(microWebSrv2, request):
    data = request.GetPostedURLEncodedForm()
    try:
        ssid = data['ssid']
        pwd = data['pwd']
    except:
        request.Response.ReturnBadRequest()
        return
    content = """\
    <!DOCTYPE html>
    <html>
        <head>
            <title>WiFi Fallback Setup</title>
        </head>
        <body>
            <h2>CxC Energy Monitor - Settings received</h2>
            The device will now try to connect to the WiFi. if the process fails the device's WiFi network will appear<br />
        </body>
    </html>
    """
    request.Response.ReturnOk(content)
    ## Save Config
    kv.set('AP_PWD', pwd)
    kv.set('AP_SSID', ssid)
    utime.sleep_ms(3000)
    print("Resetting Machine")
    machine.reset()


def init():
    # Instanciates the MicroWebSrv2 class,
    mws2 = MicroWebSrv2()
    mws2.SetEmbeddedConfig()
    mws2.BindAddress = ('192.168.4.1', 80)
    mws2.NotFoundURL = '/'
    return mws2
