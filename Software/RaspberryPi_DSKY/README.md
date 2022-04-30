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

## Virtual AGC installation

```
sudo apt-get install 
libsdl-dev
libncurses5-dev
liballegro4-dev
wx3.0-headers
tcl
tk
git
sudo apt-get install *wx*dev*
sudo apt-get install *wx*header*

git clone --depth 1 https://github.com/virtualagc/virtualagc

cd virtualagc
make install

================================================================
Run Virtual AGC from its desktop icon.
Or else, run Virtual AGC from a command-line as follows:
  cd ~/VirtualAGC/Resources
  ../bin/VirtualAGC
================================================================
```

## start virtualAGC

start virtualAGC in Forground to see output
```
/home/pi/VirtualAGC/bin/yaAGC --core="/home/pi/VirtualAGC/Luminary099.bin" --port=19697 --cfg="/home/pi/VirtualAGC/LM.ini"
```

start virtualAGC as Service without output to shell
```
/home/pi/VirtualAGC/bin/yaAGC --core="/home/pi/VirtualAGC/Luminary099.bin" --port=19697 --cfg="/home/pi/VirtualAGC/LM.ini"  &>/dev/null &
```
