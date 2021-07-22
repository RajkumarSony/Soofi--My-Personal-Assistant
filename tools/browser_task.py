
from tools.tools_module import *
from tools.domain_validate import *
from pyautogui import *
import webbrowser

query = ""
count = 0
def open_browser(inputType,self):
    speak("Now Browser is ready. Please tell me, What do you want to do now?...")
    
    global query
    # global count

    # if count >= 5:
    #     speak('Oh no, i think still... you are busy.... So for now, i am going to sleep.... Please call me if you want...')
    #     count = 0
    #     return

    # count += 1
    
    if inputType in ['userInput']:
        query = prompt(text='Give Favorite Link', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    if query in ['open stackoverflow','stackoverflow','stack overflow']:
        webbrowser.open_new_tab("https://stackoverflow.com/login")
        speak("In web browser, stackoverflow is opening...., It may take few seconds....")
        # print("Open Successful!")

    elif query in ['open youtube','youtube']:
        webbrowser.open_new_tab("https://youtube.com")
        speak("In web browser, youtube is opening...., It may take few seconds....")
        # print("Open Successful!")
    
    elif query in ['open google','google']:
        webbrowser.open_new_tab("https://youtube.com")
        speak("In web browser, youtube is opening...., It may take few seconds....")
        # print("Open Successful!")

    elif query in ['open whatsapp','whatsapp']:
        webbrowser.open_new_tab("https://web.whatsapp.com.com")
        speak("In web browser, whatsapp is opening...., It may take few seconds....")
        # print("Open Successful!")

    elif query in ['open github','github']:
        webbrowser.open_new_tab("https://github.com")
        speak("In web browser, github is opening...., It may take few seconds....")
        # print("Open Successful!")

    elif query in ['open google classroom','google classroom','google class room','classroom','class room']:
        webbrowser.open_new_tab("https://classroom.google.com/u/0/h")
        speak("In web browser, google classroom is opening...., It may take few seconds....")
        # print("Open Successful!")

    elif query in ['open my gmail','open gmail','open my gmail account','open gmail account','gmail']:
        webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
        speak("In web browser, your gmail is opening...., It may take few seconds....")
        # print("Open Successful!")
    
    elif query in ['open blank tab','blank tab','blanktab']:
        webbrowser.open_new_tab("https://")
        speak("In web browser, blank tab is opening...., It may take few seconds....")
        # print("Open Successful!")
    
    elif query in ['close browser','close','exit','quit','return','go back']:
        speak("Browser task is successfully closed...")
    
    else:
        if(isValidDomain(query)):
            webbrowser.open_new_tab("https://"+query)
            speak("In web browser, "+query+" is opening...., It may take few seconds....")
        else:
            speak("Given url is not valid...")
        open_browser(inputType,self)
