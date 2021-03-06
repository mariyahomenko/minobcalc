from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow2):
        MainWindow2.setObjectName("MainWindow2")
        MainWindow2.resize(617, 646)
        MainWindow2.setStyleSheet("QMainWindow {\n"
"background: rgb(196,222,234);\n"
"}\n"
"\n"
"QPushButton {\n"
"background: rgb(163,203,222);\n"
"border: 1px solid #7f3a19;\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background: #ffff52;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background: #7bb87b;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 8, 2, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 7, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 2, 1)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 2, 2, 2, 2)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 7, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 5, 2, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 2, 1)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setText("")
        self.label_18.setPixmap(QtGui.QPixmap("gerb.png"))
        self.label_18.setScaledContents(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 6, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 2)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 7, 2, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 6, 2, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 8, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 4, 2, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 5, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 2, 1, 1)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.lineEdit_6.setReadOnly(True)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow2", "MainWindow"))
        self.label_8.setText(_translate("MainWindow2", "????????????????????\n"
"????????????"))
        self.label_7.setText(_translate("MainWindow2", "????????????????????"))
        self.label_6.setText(_translate("MainWindow2", "???\n"
"??/??\n"
""))
        self.label_4.setText(_translate("MainWindow2", "?????????????????????????? ?? ???????????????????????? ???????????????????? ????????\n"
"????????????????, ????????????????????????, ???????????????? ?? ??????????????????,\n"
"???????????????????????? ?? ?????????????? ???????????? ????????????????\n"
"????????????????????"))
        self.label_5.setText(_translate("MainWindow2", "1"))
        self.label_9.setText(_translate("MainWindow2", "2"))
        self.label_10.setText(_translate("MainWindow2", "?????????????????????? ???????????????????? ???????? ?????????? ??????????????\n"
"?????????? ?? ???????????? ????????????, ???????????????????????? ????\n"
"?????????????? ???????????????????????? ?????????? ????????????????????????\n"
"?????????????? ???????????????????? ??????????????????"))
        self.label_11.setText(_translate("MainWindow2", "?????????????????????? ???????????? ?????? ???????????????????? ?????????? ????\n"
"???????????????????? ?????????? ????????????????????????"))
        self.label_12.setText(_translate("MainWindow2", "3"))
        self.label_13.setText(_translate("MainWindow2", "4"))
        self.label_14.setText(_translate("MainWindow2", "???????????????????? ??????????????????, ????????????????????\n"
"?????????????????????????????? ???????????????? ?? ????????????????????\n"
"?????????????????? ???? ?????????????? ????????????"))
        self.label_15.setText(_translate("MainWindow2", "5"))
        self.label_16.setText(_translate("MainWindow2", "?????????????????????? ???????????????????????? ?????????????????? ??\n"
"???????????????????????????????? ???????????????????? ??????????????????\n"
"???? ?????????????????????? ???????? ????????????????????????\n"
"?????????????????????? ?? ?????????????????????????? ???? ????????????????????"))
        self.label_17.setText(_translate("MainWindow2", "?????????? ??1"))
        self.pushButton.setText(_translate("MainWindow2", "???"))
        self.lineEdit.setPlaceholderText('max = 0.2')
        self.lineEdit_2.setPlaceholderText('max = 0.2')
        self.lineEdit_3.setPlaceholderText('max = 0.2')
        self.lineEdit_4.setPlaceholderText('max = 0.2')
        self.lineEdit_5.setPlaceholderText('max = 0.2')
        self.lineEdit_6.setPlaceholderText('max = 1')
