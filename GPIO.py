from tkinter import *
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

LED = 11
Relay = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup (LED,GPIO.OUT)

GPIO.output(LED,0)
print("LED Current State Is OFF, Waiting you'r command..........")

window = Tk()

window.title = ("GPIO_Control")

window.geometry ("520x320")

def LED_ON ():
    
    GPIO.output(LED,1)
    print ('LED is ON')
    
def LED_OFF ():
    
    GPIO.output(LED,0)
    print('LED is OFF')
    
button_1 = Button(window, text = 'LED_ON', width =10, fg ='green', command= LED_ON)
button_1.pack()

button_2 = Button(window, text = 'LED_OFF', width =10, fg ='red', command= LED_OFF)
button_2.pack()

window.mainloop()