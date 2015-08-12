#By Chris Schoener and Nate Davis, Python 2

#Keyboard buffer doesn't work over SSH!!!

#TODO: 1) report tray to EC2 and receive response
#      2) add proper values to cfg (motor steps, light ports) and test

import ConfigParser #uses built in module to read config
import ast # for lists in config
import struct
from solenoid import *
import time
from light import *
from Student import *


    
#def reportTray(Tray)
#fake for now
#I'm thinking we set EC2 to a static IP and open a port, then send packets
#EC2 then just sends a 1 or 0 back to the IP it received from
#The question is what sort of communication does the PSU network allow
#Server will almost always return 1 unless someone manages to scan a non-box rfid
#    return 1


def main():
    config = ConfigParser.RawConfigParser()
    config.read("boxconfig.txt") 
    waitSecs = config.getint("general","seconds_box_is_unlocked")
    lock = solenoid(config.getint("lock", "pin"), waitSecs)
    greenLight = light(config.getint("light", "greenPin"))
    redLight = light(config.getint("light", "redPin"))
    # ^ not worth reading ^

    greenLight.off()
    redLight.off()
    
    while 1:

        currentStudent = Student(0, 0, False, 'students.db')
        
        idInput = raw_input('scan an RFID tag') 
        if(currentStudent.isInputRFID(idInput)): #report tray and open box
            if(currentStudent.isStudentInDB()):
                self.setStudentNumberFromDB()
                self.setHasG2GFromDB()
                if(self.hasG2G):
                    redLight.off()
                    greenLight.on()
                    lock.unlockThenLock()
                else:
                    redLight.on()
                    greenLight.off()
            else:
                redLight.on()
                greenLight.off()
        else:
            redLight.on()
            greenLight.on()

main()
    
