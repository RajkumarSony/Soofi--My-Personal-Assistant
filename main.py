
import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

## ==> GUI FILE
from app_modules import *

## ==> GLOBALS
counter = 0
jumper = 0

class Home(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_Home()
        self.ui.setupUi(self)
        
        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent

        ## PRINT ==> SYSTEM
        print('System: ' + platform.system())
        print('Version: ' +platform.release())

        ## ==> LOAD DEFINITIONS
        UIFunctions.uiDefinitions(self)
        # ==> END ##

        ## SHOW ==> MAIN WINDOW
        self.show()
        ## ==> END ##

        ## ==> UI FUNCTIONS
        UIFunctions.uiFunctions(self)
        # ==> END ##


    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

## ==> SPLASHSCREEN WINDOW
class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## ==> SET INITIAL PROGRESS BAR TO (0) ZERO
        self.progressBarValue(0)

        ## ==> REMOVE STANDARD TITLE BAR
        self.setWindowFlags(Qt.FramelessWindowHint) # Remove title bar
        self.setAttribute(Qt.WA_TranslucentBackground) # Set background to transparent

        ## ==> APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(1)

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

        ## ==> UI LOADING
        UIFunctions.uiLoading(self)
        # ==> END ##

    ## DEF TO LOANDING
    ########################################################################
    def progress (self):
        global counter
        global jumper
        value = counter

        ## ==> HTML TEXT PERCENTAGE
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""

        ## ==> REPLACE VALUE
        newHtml = htmlText.replace("{VALUE}", str(jumper))

        if(value > jumper):
            ## ==> APPLY NEW PERCENTAGE TEXT
            self.ui.labelPercentage.setText(newHtml)
            jumper += 1

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value >= 100: value = 1.000
        self.progressBarValue(value)

        ## ==> CLOSE SPLASH SCREE AND OPEN APP
        if counter >= 100:
            ## ==> STOP TIMER
            self.timer.stop()

            ## ==> CLOSE SPLASH SCREEN
            self.close()

            ## ==> SHOW MAIN WINDOW
            self.main = Home()
            self.main.show()

        # INCREASE COUNTER
        counter += 0.1

    ## ==> DEF PROGRESS BAR VALUE
    ########################################################################
    def progressBarValue(self, value):

        ## ==> PROGRESSBAR STYLESHEET BASE
        styleSheet = """
        QFrame{
        	border-radius: 150px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} rgba(85, 170, 255, 255));
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        ## ==> GET NEW VALUES
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        ## ==> SET VALUES TO NEW STYLESHEET
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        ## ==> APPLY STYLESHEET WITH NEW VALUES
        self.ui.circularProgress.setStyleSheet(newStylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = SplashScreen()
    sys.exit(app.exec_())