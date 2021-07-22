
# import os, sys
# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.append(parentdir)

# from ui_home import *

import speech_recognition as sr

def takeCommand(self):
    
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        # self.ui.status.setText("Listening...")
        r.energy_threshold = 10 
        audio = r.listen(source)
        try:
            print("Recognizing...")
            # self.ui.status.setText("Recognizing...")
            self.ui.status.setText("Listening...")
            query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
            print(f"User said: {query}\n")  # User query will be printed.
            self.ui.status.setText("")
        except:
            # print(e)
            self.ui.status.setText("Re-Trying...")
            print("Say that again please...")  # Say that again will be printed in case of improper voice
            return "None"  # None string will be returned
    return query