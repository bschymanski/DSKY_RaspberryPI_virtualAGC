import board
from digitalio import DigitalInOut, Pull
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

#button_in = DigitalInOut(board.GP10) # defaults to input
#button_in.pull = Pull.UP # turn on internal pull-up resistor
#button = Debouncer(button_in)
pins = (board.GP6, board.GP7, board.GP8, board.GP9,board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21, board.GP22, board.GP26, board.GP27)
buttons = []   # will hold list of Debouncer objects
for pin in pins:   # set up each pin
    tmp_pin = DigitalInOut(pin) # defaults to input
    tmp_pin.pull = Pull.UP      # turn on internal pull-up resistor
    buttons.append( Debouncer(tmp_pin) )

while True:
    for i in range(len(buttons)):
        buttons[i].update()
        if buttons[i].fell:
            print("button",i,"pressed!")
            if i == 0:
                print("0")
                kbd.send(Keycode.ZERO)
                
            if i == 1:
                print("1")
                kbd.send(Keycode.ONE)
                
            if i == 2:
                print("2")
                kbd.send(Keycode.TWO)
                
            if i == 3:
                print("3")
                kbd.send(Keycode.THREE)
                
            if i == 4:
                print("4")
                kbd.send(Keycode.FOUR)
                
                
            if i == 5:
                print("5")
                kbd.send(Keycode.FIVE)
                
            if i == 6:
                print("6")
                kbd.send(Keycode.SIX)
                
            if i == 7:
                print("7")
                kbd.send(Keycode.SEVEN)
                
            if i == 8:
                print("8")
                kbd.send(Keycode.EIGHT)
              
            if i == 9:
                print("9")
                kbd.send(Keycode.NINE)
                
                
            if i == 10:
                print("Verb")
                kbd.send(Keycode.V)
                
            if i == 11:
                print("Noun")
                kbd.send(Keycode.N)
                
            if i == 12:
                print("Plus")
                kbd.send(Keycode.KEYPAD_PLUS)
                
            if i == 13:
                print("Minus")
                kbd.send(Keycode.KEYPAD_MINUS)
                
            if i == 14:
                print("CLR")
                kbd.send(Keycode.C)
                
            if i == 15:
                print("PRO")
                kbd.send(Keycode.P)
            
            if i == 16:
                print("Key Rel")
                kbd.send(Keycode.K)

            if i == 17:
                print("Enter")
                kbd.send(Keycode.E)

            if i == 18:
                print("Reset")
                kbd.send(Keycode.R)
        if buttons[i].rose:
            #print("button",i,"released!")
            print(" ")
        
            