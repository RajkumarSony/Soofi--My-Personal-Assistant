
from tools.tools_module import *
from tools.speaker import speak
import wikipedia

query = ""

def search_wiki(inputType,self):
    speak('Now Wikipedia is ready. Please tell me, What do you want to search?')

    global query
    
    if inputType in ['userInput']:
        query = prompt(text='Search Query', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    speak('This query is searching on wikipedia')
    speak('Please wait....')
    query = query.replace("wikipedia", "")
    try:
        results = wikipedia.summary(query, sentences=3)
    except:
        # print('Invalid Query!')
        speak("Sorry, According to Wikipedia, The given query is not found.")
        return

    if not results:
        speak("Sorry, No result found from Wikipedia")
        # print("Sorry, No result found from Wikipedia")

    speak("According to Wikipedia")
    # print(results)
    speak(results)