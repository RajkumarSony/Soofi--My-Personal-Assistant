
# ==> GUI FILE
from ui_popup import Ui_Popup
from PyQt5.QtCore import QTimer, QTime, Qt
import manager
from main import *

query = ""
temp = ""
class Popup(QMainWindow):

    ## ==> MAIN -> POPUP WINDOW
    #============================

    # POPUP ==> USER INPUT THROUGH ENTER KEY
    def keyPressEvent(self, event):
        global query
        global temp
        if event.key()=="":
            self.close()
            print('pass 4')
            query = str(self.ui.a_input.text().lower())
            # if temp == "btn":
            #     print("xxxx")
            manager.manage(query,"userInput",self)
            print(query)
            # manage(Popup.input_text,"userInput",self) #Pass Query as a parameter
            # print(Popup.input_text)



    ## TOOLS ==> USER INPUT
    def userInput(title,btn="",self=""):
        global query
        global temp
        temp = btn
        main = Popup()
        query = main.ui.a_input.text()
        return query

    def __init__(self):
        Popup.input_text = ""
        QMainWindow.__init__(self)
        self.ui = Ui_Popup()
        self.ui.setupUi(self)
        # self.ui.title.setText(title)
        self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent
        self.show()

        self.ui.closebtn.clicked.connect(lambda: self.close())