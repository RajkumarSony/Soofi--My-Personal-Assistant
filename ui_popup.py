
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Popup(object):
    def setupUi(self, Popup):
        if not Popup.objectName():
            Popup.setObjectName(u"Popup")
        Popup.resize(468, 315)
        Popup.setFocusPolicy(Qt.StrongFocus)
        Popup.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        Popup.setDockNestingEnabled(True)
        Popup.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(Popup)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_29 = QFrame(self.centralwidget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(11, 186, 120, 120))
        self.frame_29.setStyleSheet(u"border-radius:60px;\n"
"background-color:rgb(0, 18, 25);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.centralwidget)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(17, 10, 51, 51))
        self.frame_31.setStyleSheet(u"#frame_31{\n"
"     border-radius:25px;\n"
"     background-color: #20BAFC;\n"
"	 border:5px solid rgb(0, 18, 25);\n"
"}\n"
"")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setGeometry(QRect(7, 7, 37, 37))
        self.frame_32.setStyleSheet(u"#frame_32 {\n"
"	border-radius: 18px;	\n"
"	;background-color: #00192C;\n"
"}\n"
"")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.container_7 = QFrame(self.centralwidget)
        self.container_7.setObjectName(u"container_7")
        self.container_7.setGeometry(QRect(38, 26, 421, 201))
        self.container_7.setStyleSheet(u"QFrame{\n"
"	background-color:rgb(0, 18, 25);\n"
"    border-radius: 30px;\n"
"}")
        self.container_7.setFrameShape(QFrame.NoFrame)
        self.container_7.setFrameShadow(QFrame.Raised)
        self.circularBg_5 = QFrame(self.container_7)
        self.circularBg_5.setObjectName(u"circularBg_5")
        self.circularBg_5.setGeometry(QRect(20, 25, 441, 61))
        self.circularBg_5.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: #20BAFC;\n"
"}")
        self.circularBg_5.setFrameShape(QFrame.NoFrame)
        self.circularBg_5.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.circularBg_5)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(5, 5, 431, 51))
        self.frame.setStyleSheet(u"\n"
"	border: 2px solid #00192C;\n"
"	border-radius: 25px;	\n"
"	background-color: rgb(4,39,58);\n"
"	\n"
"	font: 25 16pt \"Bahnschrift Light\";\n"
"	color: #fff;\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.aaa = QFrame(self.container_7)
        self.aaa.setObjectName(u"aaa")
        self.aaa.setGeometry(QRect(36, 120, 351, 45))
        self.aaa.setStyleSheet(u"border-radius: 22px;\n"
"border:2px solid #20BAFC;\n"
"background-color: rgb(255, 255, 255);")
        self.aaa.setFrameShape(QFrame.StyledPanel)
        self.aaa.setFrameShadow(QFrame.Raised)
        self.aa = QFrame(self.aaa)
        self.aa.setObjectName(u"aa")
        self.aa.setGeometry(QRect(2, 2, 347, 41))
        self.aa.setStyleSheet(u"#aa{\n"
"border-radius: 20px;\n"
"border:2px solid #00192C;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.aa.setFrameShape(QFrame.StyledPanel)
        self.aa.setFrameShadow(QFrame.Raised)
        self.a_input = QLineEdit(self.aa)
        self.a_input.setObjectName(u"a_input")
        self.a_input.setGeometry(QRect(10, 2, 328, 37))
        self.a_input.setStyleSheet(u"#a_input{\n"
"border-radius: 18px;\n"
"border:2px solid #fff;\n"
"font: 25 14pt \"Bahnschrift Light\";\n"
"}")
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(21, 196, 101, 101))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"\n"
"	border-radius: 50px;\n"
"    border:2px solid #20BAFC;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_42 = QFrame(self.frame_3)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(30, 30, 41, 41))
        self.frame_42.setStyleSheet(u"border-radius:20px;\n"
"background-color:#20BAFC;")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setGeometry(QRect(5, 5, 31, 31))
        self.frame_43.setStyleSheet(u"border-radius:15px;\n"
"background-color: #00192C;")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.frame_44 = QFrame(self.frame_42)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(20, 20, 41, 41))
        self.frame_44.setStyleSheet(u"border-radius:20px;\n"
"background-color:#20BAFC;")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(63, 66, 371, 31))
        self.title.setStyleSheet(u"\n"
"	\n"
"	font: 25 16pt \"Bahnschrift Light\";\n"
"	color: #fff;\n"
"")
        self.title.setAlignment(Qt.AlignCenter)
        self.closebtn = QPushButton(self.centralwidget)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setEnabled(True)
        self.closebtn.setGeometry(QRect(440, 20, 20, 21))
        self.closebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closebtn.setStyleSheet(u"QPushButton {\n"
"	font: 8pt \"Comic Sans MS\";\n"
"	border: none;\n"
"	border-radius: 10px;		\n"
"	background-color: #ca1606;\n"
"\n"
"	font: 25 8pt \"Microsoft YaHei UI Light\";\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        Popup.setCentralWidget(self.centralwidget)
        self.frame_29.raise_()
        self.container_7.raise_()
        self.frame_3.raise_()
        self.frame_31.raise_()
        self.title.raise_()
        self.closebtn.raise_()

        self.retranslateUi(Popup)

        QMetaObject.connectSlotsByName(Popup)
    # setupUi

    def retranslateUi(self, Popup):
        Popup.setWindowTitle(QCoreApplication.translate("Popup", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Popup", u"Access Command", None))
#if QT_CONFIG(tooltip)
        self.closebtn.setToolTip(QCoreApplication.translate("Popup", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closebtn.setText(QCoreApplication.translate("Popup", u"x", None))
    # retranslateUi

