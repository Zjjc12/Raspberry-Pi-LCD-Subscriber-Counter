Raspberry Pi LCD Subscriber Counter

To install (Download dependencies)

```console
sh OLEDinstall.sh
git clone https://github.com/guyc/py-gaugette.git
cd py-gaugette
sudo python setup.py install
sudo pip install wiringpi
```

Edit main.py and input your youtubeapi key

Then run python script "main.py"

SPI OLED Wiring

| SPI OLED 	| RPI     	|
|----------	|---------	|
| GND      	| GND     	|
| VCC      	| 3v3     	|
| D0/CLK   	| SCLK    	|
| D1/MOSI  	| MOSI    	|
| RES      	| GPIO 14 	|
| DC       	| GPIO 15 	|
| CS       	| CEO/CSO 	|
