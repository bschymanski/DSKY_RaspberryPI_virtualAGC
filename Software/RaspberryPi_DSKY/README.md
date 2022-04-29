# DSKY running on the RaspberryPI virtualAGC
Python Program(s) to run the DSKY

## Python install and repositorys

Neopixel Library from Adafruit
https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```
## Reset Raspberry Pico HID
the Raspberry pi pico attached via USB seems to need a reset after the raspbery has booted, otherwise the HID Keyboard function is not recognized. Send a CTRL-D via Serial

```
sudo echo -en '\x04' > /dev/ttyACM0
```
