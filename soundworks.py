from gtts import gTTS
from playsound import playsound 
from networktables import NetworkTables 
import os

ip = "10.71.8.2"

NetworkTables.initialize(server = ip)
sd = NetworkTables.getTable("datatable")
sdFlagForInit = 0
sdFlagForBox = 0
sdFlagOnce = 0
sdFlagOnce1 = 0
seconds = sd.getNumber("matchTime", 0)
queue = 0        

while (True):
    
    if (sdFlagForInit == 0):
        playsound('C:/Users/mars/Desktop/pc-side/ready.mp3')
        sdFlagForInit = 1
        
    if (sd.boolean("tymeButton", False) == True):
        tts = gTTS(text = seconds + 'seconds left', lang='en')
        tts.save('textToSpeech' + queue + '.mp3')
        os.system("mpg321 good.mp3")
        playsound('C:/Users/mars/Desktop/pc-side/textToSpeech.mp3')
        queue = queue + 1 
        sd.putBoolean("tymeButton", False)