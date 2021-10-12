import pyttsx3
def setup():
    global engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    rate =engine.getProperty('rate')
    engine.setProperty('rate',100)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


setup()
speak("hello good moring")    
