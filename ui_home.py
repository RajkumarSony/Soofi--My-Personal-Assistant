
from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(1366, 730)
        self.centralwidget = QWidget(Home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.container_6 = QFrame(self.centralwidget)
        self.container_6.setObjectName(u"container_6")
        self.container_6.setGeometry(QRect(1200, 550, 201, 81))
        self.container_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 18, 25);\n"
"    border-radius: 40px;\n"
"}")
        self.container_6.setFrameShape(QFrame.NoFrame)
        self.container_6.setFrameShadow(QFrame.Raised)
        self.circularBg_3 = QFrame(self.container_6)
        self.circularBg_3.setObjectName(u"circularBg_3")
        self.circularBg_3.setGeometry(QRect(10, 10, 61, 61))
        self.circularBg_3.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: #20BAFC;\n"
"}")
        self.circularBg_3.setFrameShape(QFrame.NoFrame)
        self.circularBg_3.setFrameShadow(QFrame.Raised)
        self.speakbtn = QPushButton(self.circularBg_3)
        self.speakbtn.setObjectName(u"speakbtn")
        self.speakbtn.setGeometry(QRect(5, 5, 51, 51))
        self.speakbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.speakbtn.setStyleSheet(u"#speakbtn {\n"
"	border: 2px solid #00192C;\n"
"	border-radius: 25px;	\n"
"	image: url(:/Images/mic.png);\n"
"	;background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgb(6,77,111), stop:0.750 rgb(6,77,111));\n"
"}\n"
"#speakbtn:hover {\n"
"	background-color:  rgb(4,39,58);\n"
"	border: 2px solid #00192C;\n"
"}\n"
"#speakbtn:pressed {	\n"
"	background-color:#00192C;\n"
"	border: 2px solid #00192C;\n"
"}")
        self.label = QLabel(self.container_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(77, 20, 91, 41))
        self.label.setStyleSheet(u"#label{\n"
"	font: 75 24pt \"Candara\";\n"
"	color:#fff;\n"
"}")
        self.circularBg_2 = QFrame(self.centralwidget)
        self.circularBg_2.setObjectName(u"circularBg_2")
        self.circularBg_2.setGeometry(QRect(1270, 610, 131, 51))
        self.circularBg_2.setStyleSheet(u"QFrame{\n"
"	border-radius: 20px;\n"
"	background-color: rgba(77, 77, 77, 77);\n"
"}")
        self.circularBg_2.setFrameShape(QFrame.NoFrame)
        self.circularBg_2.setFrameShadow(QFrame.Raised)
        self.user_input = QPushButton(self.circularBg_2)
        self.user_input.setObjectName(u"user_input")
        self.user_input.setGeometry(QRect(9, 25, 100, 21))
        self.user_input.setMinimumSize(QSize(0, 0))
        self.user_input.setCursor(QCursor(Qt.PointingHandCursor))
        self.user_input.setStyleSheet(u"#user_input {\n"
"	border: 2px solid #00192C;\n"
"	border-radius: 10px;	\n"
"	background-color:  rgb(0, 18, 25);\n"
"	color: #fff;\n"
"}\n"
"\n"
"#user_input:pressed {	\n"
"	background-color: #00192C;\n"
"	border: 2px solid #00192C;\n"
"}")
        self.container_7 = QFrame(self.centralwidget)
        self.container_7.setObjectName(u"container_7")
        self.container_7.setGeometry(QRect(1080, 40, 201, 81))
        self.container_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 18, 25);\n"
"    border-radius: 40px;\n"
"}")
        self.container_7.setFrameShape(QFrame.NoFrame)
        self.container_7.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.container_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(77, 20, 91, 41))
        self.label_2.setStyleSheet(u"#label{\n"
"	font: 75 24pt \"Candara\";\n"
"	color:#fff;\n"
"}")
        self.circularBg_5 = QFrame(self.container_7)
        self.circularBg_5.setObjectName(u"circularBg_5")
        self.circularBg_5.setGeometry(QRect(10, 10, 181, 61))
        self.circularBg_5.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: #20BAFC;\n"
"}")
        self.circularBg_5.setFrameShape(QFrame.NoFrame)
        self.circularBg_5.setFrameShadow(QFrame.Raised)
        self.pushButton_3 = QPushButton(self.circularBg_5)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(6, 5, 129, 51))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"#pushButton_3 {\n"
"	border: 2px solid #00192C;\n"
"	border-radius: 25px;	\n"
"	background-color: rgb(4,39,58);\n"
"	\n"
"	font: 10pt \"Leelawadee UI\";\n"
"	color: #fff;\n"
"}\n"
"#pushButton_3:hover {\n"
"	background-color:  #00192C;\n"
"	border: 2px solid #00192C;\n"
"}\n"
"#pushButton_3:pressed {	\n"
"	background-color: #000;\n"
"	border: 2px solid #00192C;\n"
"}")
        self.circularBg_4 = QFrame(self.centralwidget)
        self.circularBg_4.setObjectName(u"circularBg_4")
        self.circularBg_4.setGeometry(QRect(1100, 70, 231, 181))
        self.circularBg_4.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: rgba(77, 77, 77, 77);\n"
"}")
        self.circularBg_4.setFrameShape(QFrame.NoFrame)
        self.circularBg_4.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(1240, 30, 101, 101))
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	image: url(:/Images/pic.png);\n"
"	border-radius: 50px;\n"
"    border:2px solid #20BAFC;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.closebtn = QPushButton(self.centralwidget)
        self.closebtn.setObjectName(u"closebtn")
        self.closebtn.setEnabled(True)
        self.closebtn.setGeometry(QRect(1350, 540, 16, 16))
        self.closebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.closebtn.setStyleSheet(u"QPushButton {\n"
"	font: 8pt \"Comic Sans MS\";\n"
"	border: none;\n"
"	border-radius: 8px;		\n"
"	background-color: #ca1606;\n"
"\n"
"	font: 25 8pt \"Microsoft YaHei UI Light\";\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover {		\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.frame_29 = QFrame(self.centralwidget)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setGeometry(QRect(1230, 20, 120, 120))
        self.frame_29.setStyleSheet(u"border-radius:60px;\n"
"background-color:rgb(0, 18, 25);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.frame_31 = QFrame(self.centralwidget)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setGeometry(QRect(1060, 20, 51, 51))
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
        self.container_8 = QFrame(self.centralwidget)
        self.container_8.setObjectName(u"container_8")
        self.container_8.setGeometry(QRect(-30, -40, 381, 111))
        self.container_8.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(0, 18, 25);\n"
"    border-radius: 40px;\n"
"}")
        self.container_8.setFrameShape(QFrame.NoFrame)
        self.container_8.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.container_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(77, 20, 91, 41))
        self.label_4.setStyleSheet(u"#label{\n"
"	font: 75 24pt \"Candara\";\n"
"	color:#fff;\n"
"}")
        self.circularBg_6 = QFrame(self.container_8)
        self.circularBg_6.setObjectName(u"circularBg_6")
        self.circularBg_6.setGeometry(QRect(14, 15, 361, 91))
        self.circularBg_6.setStyleSheet(u"QFrame{\n"
"	border-radius: 35px;\n"
"	background-color: #20BAFC;\n"
"}")
        self.circularBg_6.setFrameShape(QFrame.NoFrame)
        self.circularBg_6.setFrameShadow(QFrame.Raised)
        self.circularBg_7 = QFrame(self.circularBg_6)
        self.circularBg_7.setObjectName(u"circularBg_7")
        self.circularBg_7.setGeometry(QRect(6, 0, 352, 88))
        self.circularBg_7.setStyleSheet(u"#circularBg_7 {\n"
"	border: 2px solid #00192C;\n"
"	border-radius: 33px;	\n"
"	background-color: rgb(4,39,58);\n"
"	\n"
"	font: 10pt \"Leelawadee UI\";\n"
"	color: #fff;\n"
"}")
        self.circularBg_7.setFrameShape(QFrame.NoFrame)
        self.circularBg_7.setFrameShadow(QFrame.Raised)
        self.frame_33 = QFrame(self.centralwidget)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setGeometry(QRect(330, -20, 51, 51))
        self.frame_33.setStyleSheet(u"#frame_33{\n"
"     border-radius:25px;\n"
"     background-color: #20BAFC;\n"
"	 border:5px solid rgb(0, 18, 25);\n"
"}\n"
"")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(7, 7, 37, 37))
        self.frame_35.setStyleSheet(u"#frame_35 {\n"
"	border-radius: 18px;	\n"
"	;background-color: #00192C;\n"
"}\n"
"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.frame_36 = QFrame(self.centralwidget)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setGeometry(QRect(-20, 50, 51, 51))
        self.frame_36.setStyleSheet(u"#frame_36{\n"
"     border-radius:25px;\n"
"     background-color: #20BAFC;\n"
"	 border:5px solid rgb(0, 18, 25);\n"
"}\n"
"")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.frame_37 = QFrame(self.frame_36)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(7, 7, 37, 37))
        self.frame_37.setStyleSheet(u"#frame_37 {\n"
"	border-radius: 18px;	\n"
"	;background-color: #00192C;\n"
"}\n"
"")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(80, 10, 241, 41))
        self.label_5.setStyleSheet(u"#label_5{\n"
"	font: 16pt \"Segoe UI\";\n"
"	color: #fff;\n"
"}")
        self.frame_42 = QFrame(self.centralwidget)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(20, 10, 41, 41))
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
        self.ui_time = QLabel(self.centralwidget)
        self.ui_time.setObjectName(u"ui_time")
        self.ui_time.setGeometry(QRect(1122, 140, 151, 61))
        self.ui_time.setLayoutDirection(Qt.LeftToRight)
        self.ui_time.setStyleSheet(u"#ui_time{\n"
"	\n"
"	font: 25 36pt \"Bahnschrift Light\";\n"
"	color: #000;\n"
"	alignment:right;\n"
"}")
        self.period = QLabel(self.centralwidget)
        self.period.setObjectName(u"period")
        self.period.setGeometry(QRect(1270, 163, 41, 31))
        self.period.setStyleSheet(u"#period{\n"
"	\n"
"	font: 25 18pt \"Bahnschrift Light\";\n"
"	color : #000;\n"
"}")
        self.ui_date = QLabel(self.centralwidget)
        self.ui_date.setObjectName(u"ui_date")
        self.ui_date.setGeometry(QRect(1123, 200, 195, 31))
        self.ui_date.setStyleSheet(u"#ui_date{\n"
"	\n"
"	font: 25 16pt \"Bahnschrift Light\";\n"
"	color: #000;\n"
"}")
        self.circularBg_8 = QFrame(self.centralwidget)
        self.circularBg_8.setObjectName(u"circularBg_8")
        self.circularBg_8.setGeometry(QRect(330, -50, 161, 111))
        self.circularBg_8.setStyleSheet(u"QFrame{\n"
"	border-radius: 30px;\n"
"	background-color: rgba(77, 77, 77, 77);\n"
"}")
        self.circularBg_8.setFrameShape(QFrame.NoFrame)
        self.circularBg_8.setFrameShadow(QFrame.Raised)
        self.tempareture = QLabel(self.centralwidget)
        self.tempareture.setObjectName(u"tempareture")
        self.tempareture.setGeometry(QRect(410, 20, 81, 41))
        self.tempareture.setStyleSheet(u"#tempareture{\n"
"	\n"
"	font: 25 24pt \"Bahnschrift Light\";\n"
"	color:  #000;\n"
"}")
        self.weathertype = QLabel(self.centralwidget)
        self.weathertype.setObjectName(u"weathertype")
        self.weathertype.setGeometry(QRect(430, -5, 41, 31))
        self.weathertype.setLayoutDirection(Qt.RightToLeft)
        self.weathertype.setStyleSheet(u"#weathertype{\n"
"	\n"
"	font: 12pt \"Calibri\";\n"
"	color:  #000;\n"
"}\n"
"")
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 650, 251, 31))
        self.label_12.setStyleSheet(u"\n"
"font: 12pt \"Calibri\";\n"
"color: #fff;")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 680, 251, 31))
        self.label_15.setStyleSheet(u"\n"
"font: 10pt \"Calibri\";\n"
"color: #fff;")
        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setGeometry(QRect(1235, 521, 131, 20))
        self.status.setStyleSheet(u"#status{\n"
"	\n"
"	font: 12pt \"Bahnschrift SemiLight\";\n"
"	color: #000;\n"
"}")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(370, 28, 41, 31))
        self.label_3.setStyleSheet(u"#label_3{\n"
"	image: url(:/Images/cloud.png);\n"
"}")
        Home.setCentralWidget(self.centralwidget)
        self.circularBg_8.raise_()
        self.circularBg_4.raise_()
        self.frame_31.raise_()
        self.container_7.raise_()
        self.frame_29.raise_()
        self.circularBg_2.raise_()
        self.container_6.raise_()
        self.closebtn.raise_()
        self.frame_3.raise_()
        self.frame_33.raise_()
        self.frame_36.raise_()
        self.container_8.raise_()
        self.label_5.raise_()
        self.frame_42.raise_()
        self.ui_time.raise_()
        self.period.raise_()
        self.ui_date.raise_()
        self.tempareture.raise_()
        self.weathertype.raise_()
        self.label_12.raise_()
        self.label_15.raise_()
        self.status.raise_()
        self.label_3.raise_()

        self.retranslateUi(Home)

        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"MainWindow", None))
        self.speakbtn.setText("")
        self.label.setText(QCoreApplication.translate("Home", u"Speak", None))
        self.user_input.setText(QCoreApplication.translate("Home", u"User Input", None))
        self.label_2.setText(QCoreApplication.translate("Home", u"Speak", None))
        self.pushButton_3.setText(QCoreApplication.translate("Home", u"Raj Kumar Sony", None))
#if QT_CONFIG(tooltip)
        self.closebtn.setToolTip(QCoreApplication.translate("Home", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closebtn.setText(QCoreApplication.translate("Home", u"x", None))
        self.label_4.setText(QCoreApplication.translate("Home", u"Speak", None))
        self.label_5.setText(QCoreApplication.translate("Home", u"Soofi : Personal Assistant", None))
        self.ui_time.setText(QCoreApplication.translate("Home", u"02 : 48", None))
        self.period.setText(QCoreApplication.translate("Home", u"AM", None))
        self.ui_date.setText(QCoreApplication.translate("Home", u"Sun ,  09  Oct ' 2020", None))
        self.tempareture.setText(QCoreApplication.translate("Home", u"37\u00b0C", None))
        self.weathertype.setText(QCoreApplication.translate("Home", u"Type", None))
        self.label_12.setText(QCoreApplication.translate("Home", u"Developed By :  Raj Kumar Sony", None))
        self.label_15.setText(QCoreApplication.translate("Home", u"MCA Student of CMR Institute of Technology", None))
        self.status.setText("")
        self.label_3.setText("")
    # retranslateUi

