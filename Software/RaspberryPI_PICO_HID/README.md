# Raspberry Pi Pico as HID Keyboard

a Raspberry Pi Pico acts as an HID Keyboard running Circuitpython.

Due to reasons unkown to me, the Pico needs a reset after the Raspberry Pi is powered up.
I therefore added a relais that puts the RUN Pin to ground for a short time during the setup and start of the pyDKSY-bs.py program.
It then seems to work fine.
