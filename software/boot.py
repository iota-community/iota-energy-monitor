# """
# This file is executed on every boot (including wake-boot from deepsleep)
# """
import utime
import framebuf

from libs import screen
from libs import rgbled
from assets import iota_logo

# Wake up LED
rgbled.init()
rgbled.yellow()

# Init OLED Screen
oled = screen.init()

# Boot Image
fbuf = framebuf.FrameBuffer(iota_logo.data, 50, 48, framebuf.MONO_HLSB)
oled.blit(fbuf, 39, 4)
oled.invert(False)
oled.show()
utime.sleep_ms(1000)

# Boot Text with version
oled.fill(0)
oled.text("IOTA Energy", 20, 15)
oled.text("Monitor 0.13", 16, 30)
oled.show()
utime.sleep_ms(1000)
