
# ==> GUI FILE
from pyautogui import KEYBOARD_KEYS
from ui_popup import Ui_Popup
from PyQt5.QtCore import QTimer, QTime, Qt
from manager import manage
from main import *
from call_popup import *
# ==> RELATED FUNCTIONS
from json import load
from tools.current_weather import get_current_weather

# ==> TOOLS FUNCTIONS
from tools.tools_module import *

## ==> GLOBALS
GLOBAL_STATE = 0
GLOBAL_TITLE_BAR = True

## ==> COUT INITIAL MENU
count = 1

# class Popup(QMainWindow):

#     ## ==> MAIN -> POPUP WINDOW
#     #============================

#     ## POPUP ==> USER INPUT THROUGH ENTER KEY
#     def keyPressEvent(self, event):
#         if event.key():
#             self.close()
#             Popup.input_text = str(self.ui.a_input.text().lower())
#             manage(Popup.input_text,"userInput",self) #Pass Query as a parameter
#             print(Popup.input_text)

#     def __init__(self):
#         Popup.input_text = ""
#         QMainWindow.__init__(self)
#         self.ui = Ui_Popup()
#         self.ui.setupUi(self)
#         self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
#         self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent
#         self.show()

#         self.ui.closebtn.clicked.connect(lambda: self.close())

class UIFunctions(Home):

    ## ==> MAIN -> UI FUNSTIONS
    #==========================

    ## TOOLS ==> LOAD TOOLS
    def loadTools(self):
        weather = get_current_weather("",self,"Patna")
        self.ui.tempareture.setText(weather[0:4])
        self.ui.weathertype.setText(weather[4:])
        self.ui.ui_time.setText(get_current_time())
        self.ui.period.setText(get_meridien())
        self.ui.ui_date.setText(get_current_date())

    ## TOOLS ==> USER INPUT
    def userInput(title,btn,self=None):
        query = Popup.userInput(title,'btn',self)
        manage(query,"userInput",self)
        
        
    ## TOOLS ==> TAKE VOICE
    def takeVoice(self=None):
        query = takeCommand(self).lower()
        print(query)
        self.ui.status.setText("Listening...")
        manage(query,"takeVoice",self)
        

    ## ==> MAIN -> UI FUNSTIONS
    #==========================
    def uiFunctions(self):
        wish_me()

        ## SHOW ==> CLOSE APPLICATION
        self.ui.closebtn.clicked.connect(lambda: self.close())

        ## SHOW ==> USER INPUT
        self.ui.user_input.clicked.connect(lambda: Popup.userInput('Access Command','btn',self))
            
        ## SHOW ==> TAKE VOICE
        self.ui.speakbtn.clicked.connect(lambda: UIFunctions.takeVoice(self))
    
    # def self.ui.user_input():

    ## ==> MAIN -> UI LOADING
    #==========================
    def uiLoading(self):
        speak("Loading your AI personal assistant - Soofi...")


    def uiDefinitions(self):
        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(lambda: UIFunctions.loadTools(self))
        # TIMER IN MILLISECONDS
        self.timer.start(1000) # update every second

        UIFunctions.loadTools(self)
        
        ## SHOW ==> DROP SHADOW
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
