
from tools.tools_module import *
from pyautogui import *

query = ""
count = 0

def start_edit_mode(inputType,self):
    speak("Please tell me, What do you want to do now?...")
    
    global query
    # global count

    # if count >= 5:
    #     speak('Oh no, i think still... you are busy.... So for now, i am going to sleep.... Please call me if you want...')
    #     count = 0
    #     return

    # count += 1
    
    if inputType in ['userInput']:
        query = prompt(text='Action Type', title='Say Something..' , default='').lower()
    else:
        query = takeCommand(self).lower()

    if query in ['take screenshot','screenshot','take snap','snap']:
        img = screenshot('my_screenshot.png')
        speak("screenshot image has been saved, successfully...")
        print(img)
        start_edit_mode(inputType,self)

    elif query in ['select all','select','select all text']:
        click(683, 300)
        hotkey('ctrl', 'a')
        speak("All text are selected...")
        start_edit_mode(inputType,self)

    elif query in ['copy all','copy','copy all text']:
        click(683, 300)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'c')
        speak("All text are copied...")
        start_edit_mode(inputType,self)
            
    elif query in ['kat all' , 'kat' , 'kat all text']:
        click(683, 300)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'x')
        speak("All text are cut...")
        start_edit_mode(inputType,self)

    elif query in ['pest here' , 'pest']:
        click(683, 300)
        hotkey('ctrl', 'v')
        speak("All text are pasted...")
        start_edit_mode(inputType,self)

    elif query in ['undo']:
        click(683, 330)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'z')
        speak("Undo successfully...")
        start_edit_mode(inputType,self)

    elif query in ['save it','save']:
        click(683, 300)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 's')
        speak("File saved successfully..")
        start_edit_mode(inputType,self)

    elif query in ['open text new file','open new file','new file']:
        click(683, 300)
        hotkey('ctrl', 'a')
        hotkey('ctrl', 'n')
        speak("New file opened..")
        start_edit_mode(inputType,self)

    elif query in ['write something','i want to write something','write']:
        speak("Please tell me, What do you want to write?...")
        
        if inputType in ['userInput']:
            query = prompt(text='System Task', title='Say Something..' , default='').lower()
        else:
            query = takeCommand(self).lower()
            
        click(683, 300)
        write(query, interval=0.25)
        speak("you wrote, like ..........,"+query)
        start_edit_mode(inputType,self)

    elif query in ['close edit mode' , 'close' , 'exit' , 'quit','return','go back']:
        speak("Edit mode is successfully closed...")
    
    else:
        speak("Sorry, I am not able to understand...")
        start_edit_mode(inputType,self)


# start_edit_mode()