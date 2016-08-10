import RPi.GPIO as GPIO
import time
import sqlite3 as lite
import os

GPIO.setmode(GPIO.BCM)

#connect to HON sqlite DB
conn = lite.connect('HON.db', check_same_thread = False)

#Bind pins as input & up position
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def my_callback(channel):
    print "falling edge detected on 18 - GREEN"
    #os.system('mpg123 -q yeah.mp3 &')
    os.system('mpg123 -q Tone.mp3 &')
    c = conn.cursor()
    c.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (1,'NA')") #TODO add location attr (ie. store) & terminal id
    conn.commit()

def my_callback2(channel):
    print "falling edge detected on 24 - RED"
    #os.system('mpg123 -q what.mp3 &')
    os.system('mpg123 -q Tone.mp3 &')
    c2 = conn.cursor()
    c2.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (4,'NA')")
    conn.commit()

def my_callback3(channel):
    print "Reset button pressed"
    
GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, bouncetime=500)
GPIO.add_event_detect(24, GPIO.FALLING, callback=my_callback2, bouncetime=500)
GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback3, bouncetime=500)

try:
    x = GPIO.event_detected(27)
    while x is False:
        time.sleep(0.01)
        x = GPIO.event_detected(27)
        
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
