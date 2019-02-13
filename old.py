# Sample Python code for user authorization

import os

import google.oauth2.credentials

'''
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
'''

import httplib2
import json
import urllib

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

'''
# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = service.channels().list(
    **kwargs
  ).execute()

  pewSubs = results['items'][0]['statistics']['subscriberCount']


if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channels_list_by_username(service,
      part='statistics',
      forUsername='Pewdiepie')

'''


# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 25
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Alternatively you can specify a software SPI implementation by providing
# digital GPIO pin numbers for all the required display pins.  For example
# on a Raspberry Pi with the 128x32 display you might use:
# disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST, dc=DC, sclk=18, din=25, cs=22)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)

count = 0

pSubs = 0
tSubs = 0
difference = 0

key = "AIzaSyBYNFKcZqt4uK1C5AcLzFpbz9hl8Uo6HLg"

pURL = "https://www.googleapis.com/youtube/v3/channels?key="+key+"&id=UC-lHJZR3Gqxm24_Vd_AJ5Yw&part=statistics";
tURL = "https://www.googleapis.com/youtube/v3/channels?key="+key+"&id=UCq-Fj5jknLsUf-MWSy4_brA&part=statistics";


while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    if(count % 1000 == 0):
      pSubs = GetSubs(pURL)
      tSubs = GetSubs(tURL)
    


    count = count + 1

    # Write two lines of text.
    
    draw.text((x, top), "Pewdiepie: " + str(pSubs),  font=font, fill=255)
    draw.text((x, top + 20), "T-Series: " + str(tSubs),  font=font, fill=255)
    print('Pewdiepie has %s subscribers' % (pSubs))
    print('T-Series has %s subscribers' % (tSubs))

    difference = pSubs - tSubs
  
    draw.textsize(str(difference))

    # Display image.
    disp.image(image)
    disp.display()
    time.sleep(0.1)


def GetSubs(url):
  soup = urllib.urlopen(url)
  markup = soup.read()

  feed_json = json.loads(markup)
  sub_count = feed_json["items"][0]["statistics"]["subscriberCount"]

  return sub_count
