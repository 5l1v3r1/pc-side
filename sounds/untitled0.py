from gtts import gTTS

tts = gTTS(text = '', lang = 'en')
tts.save('teleop.mp3')