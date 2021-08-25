import os
from playsound import playsound

while 1:
    text = input("Enter your text :")
    if text == 'exit': break
    speech = "tts --text '"+text+"' --out_path output.wav"
    os.system(speech)
    playsound('output.wav')