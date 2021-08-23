from gtts import gTTS
from playsound import playsound

language = 'en'
while 1:
    text = input("Enter your text :")
    if text == 'exit': break
    tts = gTTS(text,lang=language,slow=False)
    tts.save('speech.wav')
    playsound('speech.wav')