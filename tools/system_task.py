
from tools.tools_module import *
from tools.listener import takeCommand
from pyautogui import *
import subprocess
import os

query = ""
count = 0
def sys_task(inputType,self):
    speak("Hello Sir, I am ready to access the system applications. Please tell me, What do you want to do now?...")
    
    global query
    # global count

    # if count >= 5:
    #     speak('Oh no, i think still... you are busy.... So for now, i am going to sleep.... Please call me if you want...')
    #     count = 0
    #     return

    # count += 1
    
    if inputType in ['userInput']:
        query = prompt(text='System Task', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    if query in ['open notepad','notepad','open note','note']:
        speak("Notpad is open successfully...")
        print("Open Successful!")
        codePath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(codePath)
        sys_task(inputType,self)
    
    elif query in ['open chrome browser','open chrome','open google chrome','google chrome','chrome']:
        speak("Chrome browser is open successfully...")
        print("Open Successful!")
        try:
            codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        except:
            codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\Application\\msedge.exe"
        os.startfile(codePath)
        sys_task(inputType,self)

    elif query in ['open default browser','open browser','open edge','edge','edge browser','browser']:
        speak("Default browser is open successfully...")
        print("Open Successful!")
        codePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
        os.startfile(codePath)
        sys_task(inputType,self)
        
    elif query in ['open vs code','open visual studio code','open code','vs code','code']:
        speak("VS code is open successfully...")
        print("Open Successful!")
        codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

    elif query in ['log off','sign out','sleep']:
        speak("Ok , your pc will log off in 10 sec make sure you exit from all applications...")
        subprocess.call(["shutdown", "/l"])
        sys_task(inputType,self)
    
    elif query in ['close system task','close','exit','quit','return','go back']:
        speak("System task has been done, Successfully!")
        return
        
    else:
        speak("Sorry, I am not able to understand...")
        sys_task(inputType,self)
    
