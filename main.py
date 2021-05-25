from PyQt5 import QtGui, QtWidgets, QtCore
from win1 import Ui_MainWindow
from win2 import Ui_MainWindow2
from win3 import Ui_MainWindow3
from win4 import Ui_MainWindow4


import sys
import ctypes
from decimal import Decimal
import re


app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui1 = Ui_MainWindow()
ui1.setupUi(MainWindow)

MainWindow2 = QtWidgets.QMainWindow()
ui2 = Ui_MainWindow2()
ui2.setupUi(MainWindow2)

MainWindow3 = QtWidgets.QMainWindow()
ui3 = Ui_MainWindow3()
ui3.setupUi(MainWindow3)

MainWindow4 = QtWidgets.QMainWindow()
ui4 = Ui_MainWindow4()
ui4.setupUi(MainWindow4)

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
app.setWindowIcon(QtGui.QIcon('icon.ico'))
window = QtWidgets.QWidget()
window.setWindowIcon(QtGui.QIcon('icon.ico'))

MainWindow.show()


class globs():
    subdivision = ''
    fullname = ''
    k1 = 0
    k2 = 0


def showk1():
    MainWindow2.show()
    globs.subdivision = ui1.lineEdit.text()
    globs.fullname = ui1.lineEdit_2.text()
    MainWindow.close()
    ui4.label_9.setText(ui4.label_9.text() + globs.fullname)


def showk2():
    MainWindow3.show()
    MainWindow2.close()


def showlast():
    MainWindow4.show()
    MainWindow3.close()


def restart():
    globs.subdivision = ''
    globs.fullname = ''
    globs.k1 = 0
    globs.k2 = 0
    ui1.lineEdit.setText('')
    ui1.lineEdit_2.setText('')
    MainWindow.show()
    MainWindow4.close()
    ui2.lineEdit.setText('')
    ui2.lineEdit_2.setText('')
    ui2.lineEdit_3.setText('')
    ui2.lineEdit_4.setText('')
    ui2.lineEdit_5.setText('')
    ui2.lineEdit_6.setText('')
    ui3.lineEdit_6.setText('')
    ui3.checkBox.setEnabled(True)
    ui3.checkBox_2.setEnabled(True)
    ui3.checkBox_3.setEnabled(True)
    ui3.checkBox.setChecked(False)
    ui3.checkBox_2.setChecked(False)
    ui3.checkBox_3.setChecked(False)
    ui4.lineEdit.setText('')
    ui4.lineEdit_2.setText('')
    ui4.lineEdit_3.setText('')
    ui4.label_9.setText("Премия за счет экономии фонда оплаты труда работника\n"
"")


def calc_k1():
    try:
        k1_1 = ui2.lineEdit.text()
        k1_2 = ui2.lineEdit_2.text()
        k1_3 = ui2.lineEdit_3.text()
        k1_4 = ui2.lineEdit_4.text()
        k1_5 = ui2.lineEdit_5.text()
        reg = re.compile('[^0-9.,]')
        k1_1 = reg.sub('', k1_1)
        k1_2 = reg.sub('', k1_2)
        k1_3 = reg.sub('', k1_3)
        k1_4 = reg.sub('', k1_4)
        k1_5 = reg.sub('', k1_5)
        reg2 = re.compile('[^0-9]')
        k1_1 = reg2.sub('.', k1_1)
        k1_2 = reg2.sub('.', k1_2)
        k1_3 = reg2.sub('.', k1_3)
        k1_4 = reg2.sub('.', k1_4)
        k1_5 = reg2.sub('.', k1_5)
        ui2.lineEdit.setText(k1_1)
        ui2.lineEdit_2.setText(k1_2)
        ui2.lineEdit_3.setText(k1_3)
        ui2.lineEdit_4.setText(k1_4)
        ui2.lineEdit_5.setText(k1_5)
        if k1_1 == '':
            k1_1 = 0
        if Decimal(k1_1) > 0.2:
            k1_1 = 0.2
            ui2.lineEdit.setText('0.2')
        if k1_2 == '':
            k1_2 = 0
        if Decimal(k1_2) > 0.2:
            k1_2 = 0.2
            ui2.lineEdit_2.setText('0.2')
        if k1_3 == '':
            k1_3 = 0
        if Decimal(k1_3) > 0.2:
            k1_3 = 0.2
            ui2.lineEdit_3.setText('0.2')
        if k1_4 == '':
            k1_4 = 0
        if Decimal(k1_4) > 0.2:
            k1_4 = 0.2
            ui2.lineEdit_4.setText('0.2')
        if k1_5 == '':
            k1_5 = 0
        if Decimal(k1_5) > 0.2:
            k1_5 = 0.2
            ui2.lineEdit_5.setText('0.2')
        k1 = Decimal(k1_1) + Decimal(k1_2) + Decimal(k1_3) + Decimal(k1_4) + Decimal(k1_5)
        if Decimal(k1) < 1.1:
            ui2.lineEdit_6.setText(str(round(k1, 2)))
            globs.k1 = round(k1, 2)
        else:
            ui2.lineEdit_6.setText('...')
    except:
        ui2.lineEdit_6.setText('...')


def k2_1():
    x = ui3.checkBox.isChecked()
    ui3.lineEdit_6.setText('1')
    if x is True:
        ui3.checkBox.setEnabled(True)
        ui3.checkBox_2.setEnabled(False)
        ui3.checkBox_3.setEnabled(False)
        globs.k2 = Decimal(1)
    else:
        globs.k2 = Decimal(0)
        ui3.checkBox.setEnabled(True)
        ui3.checkBox_2.setEnabled(True)
        ui3.checkBox_3.setEnabled(True)
        ui3.lineEdit_6.setText('0')


def k2_2():
    x = ui3.checkBox_2.isChecked()
    ui3.lineEdit_6.setText('2')
    if x is True:
        ui3.checkBox.setEnabled(False)
        ui3.checkBox_2.setEnabled(True)
        ui3.checkBox_3.setEnabled(False)
        globs.k2 = Decimal(2)
    else:
        globs.k2 = Decimal(0)
        ui3.checkBox.setEnabled(True)
        ui3.checkBox_2.setEnabled(True)
        ui3.checkBox_3.setEnabled(True)
        ui3.lineEdit_6.setText('0')


def k2_3():
    x = ui3.checkBox_3.isChecked()
    ui3.lineEdit_6.setText('3')
    if x is True:
        ui3.checkBox.setEnabled(False)
        ui3.checkBox_2.setEnabled(False)
        ui3.checkBox_3.setEnabled(True)
        globs.k2 = Decimal(3)
    else:
        globs.k2 = Decimal(0)
        ui3.checkBox.setEnabled(True)
        ui3.checkBox_2.setEnabled(True)
        ui3.checkBox_3.setEnabled(True)
        ui3.lineEdit_6.setText('0')


def total():
    try:
        totalk = globs.k1 * globs.k2
        reg = re.compile('[^0-9.,]')
        reg2 = re.compile('[^0-9]')
        n1 = ui4.lineEdit.text()
        n1 = reg.sub('', n1)
        n1 = reg2.sub('.', n1)
        ui4.lineEdit.setText(n1)
        n2 = ui4.lineEdit_2.text()
        n2 = reg.sub('', n2)
        n2 = reg2.sub('.', n2)
        ui4.lineEdit_2.setText(n2)

        if n1 == '':
            n1 = 0
        if n2 == '':
            n2 = 0
        n3 = Decimal(n1) / Decimal(n2) * Decimal(totalk)
        ui4.lineEdit_3.setText(str(round(n3, 2)))
    except:
        ui4.lineEdit_3.setText('...')



ui1.pushButton.clicked.connect(lambda: showk1())
ui2.pushButton.clicked.connect(lambda: showk2())
ui3.pushButton.clicked.connect(lambda: showlast())
ui4.pushButton.clicked.connect(lambda: restart())

ui2.lineEdit.textChanged.connect(lambda: calc_k1())
ui2.lineEdit_2.textChanged.connect(lambda: calc_k1())
ui2.lineEdit_3.textChanged.connect(lambda: calc_k1())
ui2.lineEdit_4.textChanged.connect(lambda: calc_k1())
ui2.lineEdit_5.textChanged.connect(lambda: calc_k1())

ui3.checkBox.stateChanged.connect(lambda: k2_1())
ui3.checkBox_2.stateChanged.connect(lambda: k2_2())
ui3.checkBox_3.stateChanged.connect(lambda: k2_3())

ui4.lineEdit.textChanged.connect(lambda: total())
ui4.lineEdit_2.textChanged.connect(lambda: total())



sys.exit(app.exec_())
