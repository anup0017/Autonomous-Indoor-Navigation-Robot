# import curses and GPIO
import curses
import datetime
import time
import csv
import numpy as np
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
# set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho() 
curses.cbreak()
screen.keypad(True)

dir = []
tim = []
i = 0

#myList = []
try:
        while(1):       
            char = screen.getch()
            if char == curses.KEY_UP:
                #GPIO.output(22,True)
                #GPIO.output(19,True)
                print "forward"
            #a = datetime.datetime.now().replace(microsecond=0)
                GPIO.output(16,False)
                GPIO.output(18,True)
                GPIO.output(23,False)
                GPIO.output(21,True)
                time.sleep(0.1)
                #print"off"
                GPIO.output(16,False)
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(21,False)
                
                dir.append('f')
                tim.append('0.1')
                i += 1
           
            elif char == curses.KEY_DOWN:
                print "backward"
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(23,True)
                GPIO.output(21,False)
                time.sleep(0.1)
                #print"off"
                GPIO.output(16,False)
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(21,False)
                
                dir.append('b')
                tim.append('0.1')
                i += 1
                
            elif char == curses.KEY_RIGHT:
                print "right"
                GPIO.output(16,False)
                GPIO.output(18,True)
                GPIO.output(23,True)
                GPIO.output(21,False)
                time.sleep(0.1)
                #print"off"
                GPIO.output(16,False)
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(21,False)
                
                dir.append('r')
                tim.append('0.1')
                i += 1
            
            elif char == curses.KEY_LEFT:
                print "left"
                GPIO.output(16,True)
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(21,True)
                time.sleep(0.1)
                #print"off"
                GPIO.output(16,False)
                GPIO.output(18,False)
                GPIO.output(23,False)
                GPIO.output(21,False)
                
                dir.append('l')
                tim.append('0.1')
                i += 1
            
            elif char == ord('q'):
                break
             
finally:
    #Close down curses properly, inc turn echo back on!
    curses.nocbreak(); screen.keypad(0); curses.echo()
    curses.endwin()
    for i in range(0, len(dir)):
        print(dir[i]+","+tim[i]+"\n")
    print("Data successfully exported \n")
    dir = np.array(dir)
    tim = np.array(tim)
    with open('finaldata.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for row in range(0,dir.shape[0]):
            myList = []
            myList.append(dir[row])
            myList.append(tim[row])
            writer.writerow(myList)
                
    GPIO.cleanup()
    #print(b-a)
    

