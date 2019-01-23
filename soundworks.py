# -*- coding: utf-8 -*-

from playsound import playsound 
from networktables import NetworkTables 


ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")
sdFlagForInit = 0
sdFlagForBox = 0
sdFlagOnce = 0
sdFlagOnce1 = 0
queue = 0
seconds = (str)(sd.getNumber("matchTime", 0))
secondsList = list(seconds)

if (len(secondsList) == 3):
    firstDigit = secondsList[2]
    secondDigit = secondsList[1]
    thirdDigit = secondsList[0]

if (len(secondsList) == 2):
    firstDigit = secondsList[1]
    secondDigit = secondsList[0]
        
        

while (True):
    
    if (sdFlagForInit == 0):
        
        playsound('C:/Users/mars/Desktop/pc-side/ready.mp3')
        sdFlagForInit = 1

    if (sd.getBoolean('tymeButton', False) == True):
        
        if (len(secondsList) == 3):
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/üç basamaklı/' + thirdDigit + '.mp3')
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/iki basamaklı/' + secondDigit + '.mp3')
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/bir basamaklı/' + firstDigit + '.mp3')
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/secondsLeft/.mp3')
            
        if (len(secondsList) == 2):
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr' + secondDigit + '.mp3')
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr' + firstDigit + '.mp3')
            playsound('C:/Users/mars/Desktop/pc-side/sounds/tr/secondsLeft/.mp3')
            
        sd.putBoolean('tymeButton', False)
    
    if (sd.getString("roboState", "disabled") == "teleop" and sdFlagOnce == 0):
        playsound('C:/Users/mars/Desktop/pc-side/sesler/tr/teleop.mp3')
        sdFlagOnce += 1  