from playsound import playsound 
from networktables import NetworkTables

ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")
sdFlagForInit = 0
sdFlagForBox = 0
sdFlagOnce = 0
sdFlagOnce1 = 0
    
while True:

    #Türkçe        
        if ((sd.getBoolean("init", False) == True) and sdFlagForInit == 0):
            playsound('C:/Users/mars/Desktop/sesler/Tur/robotu-aciyorum.mp3')
            sdFlagForInit = 1
    
        if ((sd.getBoolean("Limit Switch Status", False) == True) and sdFlagForBox == 0):
            playsound('C:/Users/mars/Desktop/sesler/Tur/kutuyu-aldim.mp3')
            sdFlagForBox = 1
        
        if ((sd.getBoolean("releaseCube", False) == True) and sdFlagForBox == 1):
            playsound('C:/Users/mars/Desktop/sesler/Tur/kutuyu-atiyorum.mp3')
            sdFlagForBox = 0
    
        if ((sd.getNumber("time", 0.0) == 50.0) and sdFlagOnce == 0):
            playsound('C:/Users/mars/Desktop/sesler/Tur/son-50.mp3')
            sdFlagOnce = 1
            
        if ((sd.getNumber("tyme", 0.0) == 35.0) and sdFlagOnce1 == 0):
            playsound('C:/Users/mars/Desktop/sesler/Tur/do-it.mp3')
            sdFlagOnce1 = 1
            
    #English
        if ((sd.getBoolean("init", False) == True) and sdFlagForInit == 0):
            playsound('C:/Users/mars/Desktop/sesler/Eng')
            sdFlagForInit = 1
      
        if ((sd.getBoolean("Limit Switch Status", False) == True) and sdFlagForBox == 0):
            playsound('C:/Users/mars/Desktop/sesler/Eng')
            sdFlagForBox = 1
        
        if ((sd.getBoolean("releaseCube", False) == True) and sdFlagForBox == 1):
            playsound('C:/Users/mars/Desktop/sesler/Eng')
            sdFlagForBox = 0
      
        if ((sd.getNumber("time", 0.0) == 50.0) and sdFlagOnce == 0):
            playsound('C:/Users/mars/Desktop/sesler/Eng')
            sdFlagOnce = 1
        
        if ((sd.getNumber("tyme", 0.0) == 35.0) and sdFlagOnce1 == 0):
            playsound('C:/Users/mars/Desktop/sesler/Eng')
            sdFlagOnce1 = 1
      