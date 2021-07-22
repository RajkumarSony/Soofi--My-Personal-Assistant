
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    try:
        engine.say(audio)
        engine.runAndWait()
    except:
        print("wait few seconds...")

# speak("audio")