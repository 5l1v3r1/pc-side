from playsound import playsound 
from networktables import NetworkTables
import time

ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")
sdFlagForInit = 0
sdFlagForBox = 0
sdFlagOnce = 0
sdFlagOnce1 = 0


while True:

        
    if ((sd.getBoolean("init", False) == True) and sdFlagForInit == 0):
        playsound('C:/Users/mars/Desktop/sesler/Eng/speech.mp3')
        lastPlayed = "Robot ready"
        sdFlagForInit = 1
      
    if ((sd.getBoolean("Limit Switch Status", False) == True) and sdFlagForBox == 0):
        playsound('C:/Users/mars/Desktop/sesler/Eng/have-box.mp3')
        sdFlagForBox = 1
        
    if ((sd.getBoolean("releaseCube", False) == True) and sdFlagForBox == 1):
        playsound('C:/Users/mars/Desktop/sesler/Eng/speechthrow.mp3')
        sdFlagForBox = 0
      
    if ((sd.getNumber("tyme", 999999.0) <= 100.0) and sdFlagOnce == 0):
        playsound('C:/Users/mars/Desktop/sesler/Eng/speech(2).mp3')
        lastPlayed = "Last 50 seconds"
        sdFlagOnce = 1
        
    if ((sd.getNumber("tyme", 999999.0) <= 115.0) and sdFlagOnce1 == 0):
        playsound('C:/Users/mars/Desktop/sesler/Eng/speech(3).mp3')
        lastPlayed = "Last 35 seconds"
        sdFlagOnce1 = 1
            

        