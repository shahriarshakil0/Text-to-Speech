import pyttsx3
engine = pyttsx3.init() 

""" RATE"""
rate = engine.getProperty('rate')                         
engine.setProperty('rate', 150)

"""VOLUME"""
volume = engine.getProperty('volume')                         
engine.setProperty('volume',1.0) 

"""VOICE"""
voices = engine.getProperty('voices')   
engine.setProperty('voice', voices[0].id)

#Input your text
while 1:
    text = input("Enter yout text: ")
    if text == 'exit': break
    engine.say(text)
    engine.runAndWait()
    engine.stop()
    """Saving Voice to a file"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()