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

print("Please Choose A Language / Lutfen Bir Dil Seciniz")
lang = input("\n Turkce icin TR Yaziniz / For English Type EN" + "\n")    
while True:

    if (lang == "TR" ):        
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
        print("anan")    
    elif(lang == "tr"):    
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
        print("anan")    
        
    if (lang == "EN"):
        
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
        print("your mom")
    elif(lang == "en"):
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
        print("your mom")
        
    elif(lang != "en" and lang != "EN" and lang != "tr" and lang != "TR"):
        print("restart the program and type a correct word(en or tr)")
        print("lutfen gecerli bir dil giriniz(tr ya da en)")
        time.sleep(3)
        break
        