#Python 2

import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import sys


import httplib2
import json
import urllib


# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128) # Change rows & cols values depending on your display dimensions.
led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)

# Start of Code
count = 0

pSubs = 0
tSubs = 0
difference = 0

key = "ENTER YOUR KEY HERE"

pURL = "https://www.googleapis.com/youtube/v3/channels?key="+key+"&id=UC-lHJZR3Gqxm24_Vd_AJ5Yw&part=statistics";
tURL = "https://www.googleapis.com/youtube/v3/channels?key="+key+"&id=UCq-Fj5jknLsUf-MWSy4_brA&part=statistics";


def GetSubs(url):
  soup = urllib.urlopen(url)
  markup = soup.read()

  feed_json = json.loads(markup)
  sub_count = feed_json["items"][0]["statistics"]["subscriberCount"]

  return sub_count


while True:

    if(count % 100 == 0):
      pSubs = GetSubs(pURL)
      tSubs = GetSubs(tURL)
      difference = int(pSubs) - int(tSubs)

      print('Pewdiepie has %s subscribers' % (pSubs))
      print('T-Series has %s subscribers' % (tSubs))
      print('Difference: %s' % (difference))


    led.draw_text2(0,0,"Pewdiepie: " + str(pSubs),1)
    led.draw_text2(0,8,"T-Series: " + str(tSubs),1)
    led.draw_text2(32,16, str(difference),2)
    led.display()

    count = count + 1

    time.sleep(0.1)
