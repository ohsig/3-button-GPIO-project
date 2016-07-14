import RPi.GPIO as GPIO
import time
import sqlite3 as lite
#import tkMessageBox

#sqlite_file = 'HON.sqlite'
#table_name = 'tblHONResults'


#connect to HON sqlite DB
conn = lite.connect('HON.db')
c = conn.cursor()

GPIO.setmode(GPIO.BCM)

#Bind pins to input & up position
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    input_stateGreen = GPIO.input(18)
    
    if input_stateGreen == False:
        print('GREEN Button Pressed')
        #tkMessageBox.showinfo(title="BUTTON RESPONSE", message="GREEN!")
        #time.sleep(2.0)
        
        time.sleep(0.2)

    input_stateBlue = GPIO.input(4)
    
    if input_stateBlue == False:
        print('BLUE Button Pressed')
        #time.sleep(2.0)
        time.sleep(0.2)

    input_stateYellow = GPIO.input(27)
    
    if input_stateYellow == False:
        print('YELLOW Button Pressed')
        #time.sleep(2.0)
        time.sleep(0.2)

    input_stateRed = GPIO.input(24)
    
    if input_stateRed == False:
        print('RED Button Pressed')
        #time.sleep(2.0)
        time.sleep(0.2)
    
