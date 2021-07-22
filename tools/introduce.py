
from tools.tools_module import *
from tools.speaker import speak

count = 0

def say_intro(inputType,self):
    speak("Hello Sir, I am ready to give the introduction. Please, ask something...")
    
    global query
    # global count

    # if count >= 5:
    #     speak('Oh no, i think still... you are busy.... So for now, i am going to sleep.... Please call me if you want...')
    #     count = 0
    #     return

    # count += 1
    
    if inputType in ['userInput']:
        query = prompt(text='Search Query', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    if query in ['who are you' , 'what can you do' , 'tell me something about you']:
        speak('I am Soofi version 1 point 0, your personal assistant. I am programmed to minor tasks like,'
                  ' take a photo using camera, get current time, take screenshot, access keyboard, search data from google,'
                  ' get greeting messages, get self introduction, send email, get top headline news from different resources of india,'
                  ' play musics, access system applications, get information about weather in different city,'
                  ' access web browser task, get specific information from wikipedia in different cities,'
                  ' and you can ask me computational or geographical questions too!')

    elif query in ['who made you' , 'who created you' , 'who descoverd you' , 'who developed you']:
        speak("I was built by Mister Rajkumar Sony, A MCA Student Of CMR Institute of Technology, Bangalore")
        print("I was built by Mr. Rajkumar Sony.")

    elif query in ['close edit mode' , 'close' , 'exit' , 'quit','return','go back']:
        speak("Edit mode is successfully closed...")
    
    else:
        speak("Sorry, I am not able to understand...")
        say_intro(inputType,self)
