
## ==> GUI FILE
from tools.my_wiki import search_wiki
from tools.tools_module import *
from ui_popup import Ui_Popup
from PyQt5.QtCore import QTimer, QTime, Qt
from main import *
from ui_popup import Ui_Popup
from ui_home import Ui_Home
from tools.google import google_search
# from tools.current_weather import find_temperature
from tools.tools_module import *
from pyautogui import *
from call_popup import *

command = False
count = 0

def manage(query,inputType,self):
    global command
    global count

    if count >= 5:
        speak('Oh no, i think still... you are busy.... So for now, i am going to sleep.... Please call me if you want...')
        count = 0
        return

    count += 1

    if command == True:
        query = "hey"

    if query in ['hello sufi','hi sufi','hey sufi','hello','hi','hey']:
        speak('Hi Sir, Please tell me how may i help you now...')
        
        command = True
    
        if inputType in ['userInput']:
            # Popup.userInput("Main Menu","",self)
            # print(query)
            query = prompt(text='Main Menu', title='Say Something..' , default='').lower()
        else:
            query = takeCommand(self).lower()
            print(query)

        if query in ['access system task','access system application','open system application','system task','application','apps']:
            sys_task(inputType,self)
        
        elif query in ['open edit mode' , 'edit mode' , 'edit mode start' , 'start edit mode']:
            speak('Now Edit mode is opened.')
            start_edit_mode(inputType,self)
            manage(query,inputType,self)

        elif query in ['send mail','send email','send an email','i want to send an email','email','mail']:
            send_email(inputType,self)
            manage(query,inputType,self)

        elif query in ['weather forecasting','weather','temperature','find temperature','find the temperature']:
            city=""
            speak("It's my pleasure, I am ready to find the tempareture...")
            speak("Please give me the city name...")
            if inputType in ['userInput']:
                city = prompt(text='City Name', title='Say Something..' , default='').lower()
            else:
                city = takeCommand(self).lower()
            speak("please wait...")
            find_temperature(inputType,self,city)
            manage(query,inputType,self)

        elif query in ['search from google','google search','open google','hello google','google']:
            google_search(inputType,self)
            manage(query,inputType,self)

        elif query in ['search from wikipedia','wikipedia','open wikipedia','hello wikipedia','open wiki','wiki']:
            search_wiki(inputType,self)
            manage(query,inputType,self)

        elif query in ['i want to ask something','i want to ask','can i ask something','ask','excuse me','excuse']:
            ask_quesion(inputType,self)
            manage(query,inputType,self)

        elif query in ['open browser','open web browser','browser','please open the browser']:
            open_browser(inputType,self)
            manage(query,inputType,self)

        elif query in ['give me introduction','intro','introduction','give me intro','give me small intro']:
            say_intro(inputType,self)
            manage(query,inputType,self)

        elif query in ['good bye sufi' , 'ok bye sufi' , 'stop sufi' , 'good bye' , 'ok good bye' , 'bye' ]:
            speak("I'm Soofi and I'm going to sleep,Good bye, Sir!")
        
        elif query in ['time please','current time','time','tell time','telltime']:
            say_time(self)
            manage(query,inputType,self)

        elif query in ['current news','latest news','news','indian news']:
            latest_news()
            manage(query,inputType,self)
        
        elif query in ['play music' , 'play songs' , 'songs' , 'music']:
            play_music()
            manage(query,inputType,self)

        else:
            speak("It's Invalid menu option... Please try again")
            if inputType in ['userInput']:
                manage(query,inputType,self)
            else:
                manage(query,inputType,self)




    #     elif query in ['open camera' , 'camera']:
    #         open_camera()
        




    else:
        speak("It's Invalid command... Please try again")
        if inputType in ['userInput']:
            query = prompt(text='Access Command', title='Say Something..' , default='').lower()
            manage(query,inputType,self)
        else:
            query = takeCommand(self).lower()
            manage(query,inputType,self)