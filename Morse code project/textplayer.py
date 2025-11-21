import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 200)
engine.setProperty("volume", 0.9)

def playtextspeech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


