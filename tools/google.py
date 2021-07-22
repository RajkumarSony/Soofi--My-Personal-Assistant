
from tools.tools_module import *
from pyautogui import *
import webbrowser

query =""

def google_search(inputType,self):
    speak('Now Google is ready. Please tell me, What do you want to search?')
    
    global query
    
    if inputType in ['userInput']:
        query = prompt(text='Search Query', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    speak('This query is searching on google, by using your web brawser.')
    speak('Please wait....')
    # print("Query Searching...")
    webbrowser.open("https://www.google.com/search?q="+query)