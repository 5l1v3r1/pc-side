# -*- coding: utf-8 -*-

from playsound import playsound 
from networktables import NetworkTables 
import logging
logging.basicConfig(level=logging.DEBUG)

ip = "10.71.8.2"

NetworkTables.initialize(server=ip)
sd = NetworkTables.getTable("datatable")
sdFlagForInit = 0
sdFlagForBox = 0
sdFlagOnce = 0
sdFlagOnce1 = 0
queue = 0
        

while (True):
    
    seconds = sd.getNumber('tyme', 0)
    secondsList = list((str)(seconds))

    if (len(secondsList) == 5):
        firstDigit = secondsList[2]
        secondDigit = secondsList[1]
        thirdDigit = secondsList[0]

    if (len(secondsList) == 4):
        firstDigit = secondsList[1]
        secondDigit = secondsList[0]

    
    if (sdFlagForInit == 0):
        
        playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/hazir.mp3')
        sdFlagForInit = 1

    if (sd.getBoolean('tymeButton', False) == True):
        print(secondsList)
        
        if (len(secondsList) == 5):
            
            playsound('sounds/tr/ucbasamakli/' + (str)(thirdDigit) + "00" + '.mp3')
            
            if(secondDigit != 0):
                playsound('sounds/tr/ikibasamakli/' + (str)(secondDigit) + "0" + '.mp3')
            
            if(firstDigit == 0): 
                playsound('sounds/0.mp3')    
            elif():
                playsound('sounds/tr/birbasamakli/' + (str)(firstDigit) + '.mp3')
                
            playsound('sounds/tr/secondsLeft.mp3')
            
        if (len(secondsList) == 4):
            
            playsound('sounds/tr/ikibasamakli/' + (str)(secondDigit) + "0" + '.mp3')
            
            if(firstDigit == 0): 
                playsound('sounds/0.mp3')    
            elif(0):
                playsound('sounds/tr/birbasamakli/' + (str)(firstDigit) + '.mp3')
                
            playsound('sounds/tr/secondsLeft.mp3')
            
    sd.putBoolean('tymeButton', False)
    
    if (sd.getString('roboState', "disabled") == "teleop" and sdFlagOnce == 0):
        playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/teleop.mp3')
        sdFlagOnce += 1  