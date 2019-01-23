from gtts import gTTS

tts = gTTS(text = 'Teleop ready', lang = 'en')
tts.save('teleop.mp3')