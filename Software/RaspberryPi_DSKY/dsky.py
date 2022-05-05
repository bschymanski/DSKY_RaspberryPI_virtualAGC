import board
import neopixel
import time
# generate random integer values
from random import seed
from random import randint

# initialize the Status Indicator Panel with the Neopixels
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
board.D18
pixel_pin = board.D18
# The number of NeoPixels
num_pixels = 14
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.4, auto_write=True, pixel_order=ORDER
)

# define some colors for the Indicator Panel
yellow = (180, 120, 0)
red  = (160, 0, 0)
green =  (0, 120, 0)
white = (180, 140, 140)
black = (0, 0, 0)

# name the Neopixels after the function on the indicator Panel
p_uplink_acty = 13
p_no_att = 12
p_stby = 11
p_key_rel = 10
p_opr_err = 9
p_position = 8
p_clk = 7
p_temp = 6
p_gimbal_lock = 5
p_prog = 4
p_restart = 3
p_tracker = 2
p_alt = 1
p_vel = 0

#pixels[p_uplink_acty] = white
#pixels[p_no_att] = white
#pixels[p_stby] = white
#pixels[p_key_rel] = white
#pixels[p_opr_err] = white
#pixels[p_position] = white
#pixels[p_clk] = white
#pixels[p_temp] = yellow
#pixels[p_gimbal_lock] = yellow
#pixels[p_prog] = yellow
#pixels[p_restart] = yellow
#pixels[p_tracker] = yellow
#pixels[p_alt] = yellow
#pixels[p_vel] = yellow
#pixels.show()
#pixels[p_clk] = black

#for x in range(14):
#    pixels[x] = white
#    time.sleep(0.2)

#for x in range(14):
#    pixels[x] = black 
#    time.sleep(0.2)

pixels[p_uplink_acty] = white
pixels[p_temp] = yellow
time.sleep(0.5)

pixels[p_uplink_acty] = black
pixels[p_temp] = black

time.sleep(0.5)
pixels[p_uplink_acty] = white
pixels[p_temp] = yellow

time.sleep(0.5)
for x in range(50):
    p = randint(0, 13)
    pixels[p] = green
    time.sleep(0.2)
    pixels[p] = black
