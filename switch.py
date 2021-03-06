import RPi.GPIO as GPIO
import time
import sqlite3 as lite
import os


#connect to HON sqlite DB
conn = lite.connect('HON.db')
c = conn.cursor()

#sleep time between button press
sleep_time = 2.0

GPIO.setmode(GPIO.BCM)

#Bind pins as input & up position
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

    input_stateGreen = GPIO.input(18)
    input_stateYellow = GPIO.input(4)
    input_stateOrange = GPIO.input(27)
    input_stateRed = GPIO.input(24)
   
    if input_stateGreen == False:
        print('GREEN Button Pressed')
        c.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (1,'NA')") #TODO add location attr (ie. store) & terminal id
        conn.commit()
        #print('Green Record written to DB.')
        os.system('mpg123 -q yeah.mp3 &')
        time.sleep(sleep_time)
    
    if input_stateYellow == False:
        print('ORANGE Button Pressed')
        c.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (2,'NA')")
        conn.commit()
        os.system('mpg123 -q okay.mp3 &')
        time.sleep(sleep_time)

    if input_stateOrange == False:
        print('YELLOW Button Pressed')
        c.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (3,'NA')")
        conn.commit()
        os.system('mpg123 -q okay.mp3 &')
        time.sleep(sleep_time)
    
    if input_stateRed == False:
        print('RED Button Pressed')
        c.execute("INSERT INTO tblHONResults ('HON_VALUE','LOYALTY_ID') VALUES (4,'NA')")
        conn.commit()
        os.system('mpg123 -q what.mp3 &')
        time.sleep(sleep_time)

#    except KeyboardInterrupt:
#        GPIO.cleanup()
#GPIO.cleanup()
    
