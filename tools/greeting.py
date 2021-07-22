
from tools.speaker import speak
import datetime

def wish_me():
    hour = int(datetime.datetime.now().hour)
    print("Assistant....")
    
    if hour >= 0 and hour < 12:
        speak("Good Morning!, Rajkumar.....")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!, Rajkumar.....")
    
    elif hour >= 18 and hour < 24:
        speak("Good Evening!, Rajkumar.....")

    speak("Hello Sir! I'm Soofi, Your Personal Assistant.")