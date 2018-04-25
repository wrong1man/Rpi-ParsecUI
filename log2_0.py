# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'finallog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSignal
from Mainwindow import Ui_Dialog as Form
from errord import Ui_Error as Form2
import pexpect
import resources

class Ui_ParsecUI(object):
    def setupUi(self, ParsecUI):
        ParsecUI.setObjectName("ParsecUI")
        ParsecUI.resize(720, 651)
        ParsecUI.setMinimumSize(QtCore.QSize(100, 100))
        ParsecUI.setMaximumSize(QtCore.QSize(750, 750))
        ParsecUI.setBaseSize(QtCore.QSize(4, 4))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ParsecUI.setWindowIcon(icon)
        ParsecUI.setWindowOpacity(1.0)
        ParsecUI.setStyleSheet("QWidget#centralwidget{\n"
"    \n"
"    border-image: url(:/all/resources/Login1.png);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(ParsecUI)
        self.centralwidget.setMinimumSize(QtCore.QSize(100, 100))
        self.centralwidget.setMaximumSize(QtCore.QSize(1001, 1049))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(325, 300))
        self.frame.setMaximumSize(QtCore.QSize(325, 300))
        self.frame.setStyleSheet("background:rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.plogo = QtWidgets.QLabel(self.frame)
        self.plogo.setMaximumSize(QtCore.QSize(200, 70))
        self.plogo.setObjectName("plogo")
        self.verticalLayout.addWidget(self.plogo, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.emailtitle = QtWidgets.QLabel(self.frame)
        self.emailtitle.setStyleSheet("color: rgb(118, 118, 118);")
        self.emailtitle.setObjectName("emailtitle")
        self.verticalLayout.addWidget(self.emailtitle)
        self.userfield = QtWidgets.QLineEdit(self.frame)
        self.userfield.setMinimumSize(QtCore.QSize(0, 30))
        self.userfield.setMaximumSize(QtCore.QSize(280, 30))
        self.userfield.setStyleSheet("QLineEdit#userfield\n"
"{\n"
"  border: 1px solid rgb(141, 141, 141);\n"
"}")
        self.userfield.setText("")
        self.userfield.setObjectName("userfield")
        self.verticalLayout.addWidget(self.userfield)
        self.pwtitle = QtWidgets.QLabel(self.frame)
        self.pwtitle.setStyleSheet("color: rgb(118, 118, 118);")
        self.pwtitle.setObjectName("pwtitle")
        self.verticalLayout.addWidget(self.pwtitle)
        self.pwfield = QtWidgets.QLineEdit(self.frame)
        self.pwfield.setMinimumSize(QtCore.QSize(0, 30))
        self.pwfield.setMaximumSize(QtCore.QSize(280, 30))
        self.pwfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwfield.setStyleSheet("QLineEdit#pwfield\n"
"{\n"
"  border: 1px solid rgb(141, 141, 141);\n"
"}")
        self.pwfield.setText("")
        self.pwfield.setObjectName("pwfield")
        self.verticalLayout.addWidget(self.pwfield)
        self.bframe = QtWidgets.QFrame(self.frame)
        self.bframe.setMinimumSize(QtCore.QSize(0, 50))
        self.bframe.setMaximumSize(QtCore.QSize(16777215, 50))
        self.bframe.setObjectName("bframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.bframe)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.bframe)
        self.checkBox.setMaximumSize(QtCore.QSize(150, 16777215))
        self.checkBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.loginb = QtWidgets.QPushButton(self.bframe)
        self.loginb.setMinimumSize(QtCore.QSize(0, 40))
        self.loginb.setMaximumSize(QtCore.QSize(80, 40))
        self.loginb.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.loginb.setStyleSheet("QPushButton#loginb {\n"
"    font: 75 12pt \"MS Reference Sans Serif\";\n"
"     background-color:  rgb(75, 87, 244);\n"
" }\n"
"QPushButton#loginb:hover {\n"
"     background-color: rgb(17, 29, 255);\n"
" }\n"
"QPushButton#loginb:hover:!pressed\n"
"{\n"
"  border: 1px solid black;\n"
"}\n"
"\n"
"QPushButton#loginb {\n"
"color: white;\n"
"}\n"
"QPushButton#loginb {\n"
"font: 75 10pt \"Arial Rounded MT Bold\";\n"
"\n"
"}")
        self.loginb.setObjectName("loginb")
        self.horizontalLayout.addWidget(self.loginb)
        self.verticalLayout.addWidget(self.bframe)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.wrongpass = QtWidgets.QLabel(self.frame)
        self.wrongpass.setEnabled(False)
        self.wrongpass.setMaximumSize(QtCore.QSize(250, 25))
        self.wrongpass.setObjectName("wrongpass")
        self.verticalLayout.addWidget(self.wrongpass, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout.addWidget(self.frame, 6, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 9, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 1, 1, 1, 1)
        ParsecUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ParsecUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        ParsecUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ParsecUI)
        self.statusbar.setObjectName("statusbar")
        ParsecUI.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(ParsecUI)
        self.actionClose.setObjectName("actionClose")
        self.actionHelp = QtWidgets.QAction(ParsecUI)
        self.actionHelp.setObjectName("actionHelp")
        self.menuFile.addAction(self.actionClose)
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(ParsecUI)
        QtCore.QMetaObject.connectSlotsByName(ParsecUI)
        
        self.gif = QtWidgets.QLabel(self.frame)
        self.gif.setMaximumSize(QtCore.QSize(30, 30))
        #self.gif.setStyleSheet("border-image: url(loading-2.gif);")
        self.gif.setText("")
        self.gif.setObjectName("gif")
        self.horizontalLayout.addWidget(self.gif)
        self.movie = QtGui.QMovie('loading-2.gif', parent=self.gif) 
        self.movie.setCacheMode(QtGui.QMovie.CacheAll) 
        self.movie.setScaledSize(QtCore.QSize(30,30))
        #self.movie.setSpeed(100) 
        self.gif.setMovie(self.movie)
        self.gif.hide()
        
        #self.checkBox.hide()
        self.loginb.clicked.connect(lambda: self.testf()) #was maind
        self.actionClose.triggered.connect(lambda: sys.exit())
        self.wrongpass.hide()
        self.checkBox.clicked.connect(lambda: self.chekbx())
        self.checkpw()
        
       
    
    def checkpw(self):# check for saved passwords
        p=pexpect.spawn('parsec')
        print('Checking for saved passwords')
        state1=p.expect(['Email','saved',pexpect.EOF])
        print('pass expect 1')
        print(state1)
        if state1 == 0:
            pass
        elif state1==2:
            print('couldnt start parsec please kill task')
        else:
            self.checkBox.setText('Use saved password')
            self.checkBox.setChecked(True)
        p.close()
    
    def chekbx(self):#checkbox name change
        if self.checkBox.text() =='Use saved password':
            self.checkBox.setText("Save password")
        else:
            pass
        
    def Omaindialog(self,srv): #open main window - In the future Mainwindow will actually be the main window, istead of a dialog.
        print('opening main window')
        pw=self.pwfield.text()
        user=self.userfield.text()
        FirstUI.hide()
        dialog = QtWidgets.QDialog()
        dialog.ui = Form()
        dialog.ui.setupUi(dialog,user,pw,srv,self.checkBox.isChecked())
        dialog.exec_()
        dialog.show()
        Dialog.show
        sys.exit()

    def errordiag(self,error,crit): #Error dialog Function
        disptxt=error
        errord = QtWidgets.QDialog()
        errord.ui = Form2()
        errord.ui.setupUi(errord, disptxt)
        errord.exec_()
        errord.show()
        print(crit)
        if crit==1:
            sys.close
        else:
            pass
        return
    
    def testf(self):
        self.movie.start()
        self.gif.show()
        self.myThread = thread(self.userfield,self.pwfield, self.wrongpass, self.checkBox)
        self.myThread.start()
        print('finished')
        self.myThread.done.connect(self.threadrelay)
    
    def threadrelay(self, code, text):
        print('enter relay', code, text, code==3)
        self.movie.stop()
        self.gif.hide()
        self.myThread.exit()
        if code == 3:
            print(text)
            print('trying to open main diag')
            self.Omaindialog(text)
        elif code == 4:
            self.wrongpass.setText(text)
            self.wrongpass.show()            
        else:
            self.errordiag(text,code)
        

    def retranslateUi(self, ParsecUI):
        _translate = QtCore.QCoreApplication.translate
        ParsecUI.setWindowTitle(_translate("ParsecUI", "Parsec UI"))
        self.plogo.setText(_translate("ParsecUI", "<html><head/><body><p><img src=\":/all/resources/logo.png\"/></p></body></html>"))
        self.emailtitle.setText(_translate("ParsecUI", "Email"))
        self.pwtitle.setText(_translate("ParsecUI", "Password"))
        self.checkBox.setText(_translate("ParsecUI", "Save password"))
        self.loginb.setText(_translate("ParsecUI", "LOG IN"))
        self.wrongpass.setText(_translate("ParsecUI", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#cb1504;\">The username/password is icorrect!</span></p></body></html>"))
        self.menuFile.setTitle(_translate("ParsecUI", "File"))
        self.menuAbout.setTitle(_translate("ParsecUI", "About"))
        self.actionClose.setText(_translate("ParsecUI", "Exit"))
        self.actionHelp.setText(_translate("ParsecUI", "Help"))

class thread(QtCore.QThread):
    done=pyqtSignal(int, str)
    def __init__(self,usr,paw,wp,check, parent=None):
        QtCore.QThread.__init__(self)
        self.user=usr
        self.paw=paw
        self.wp=wp
        self.check=check
    def run (self):
        print(self.check.text() == "Save password", self.check.text())
        if (self.paw.text()=='' or self.user.text()=='') and self.check.text() == "Save password":
            print('if 1')
            txt=("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#cb1504;\">Please fill in both fields</span></p></body></html>")
            self.done.emit(4,txt)
            print('emited')
        elif ('@' not in self.user.text() or '.' not in self.user.text()) and self.check.text() == "Save password":
            print('if 2')
            txt=("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#cb1504;\">Please enter a valid Email</span></p></body></html>")
            self.done.emit(4,txt)
            print('emited')
        else:
            print('if 3')
            p=pexpect.spawn('parsec')
            print('spawned')
            state1=p.expect(['Email','saved',pexpect.EOF])
            print('pass expect 1')
            print(state1)
            if state1==2:
                #errordiag
                text=p.before.decode('utf-8')
                prelim='Something went wrong - Try to task kill all parsec processes through task manager!-\n Error log:\n'
                text= prelim+ str(text)
                print(text)
                p.close()
                self.done.emit(0, text)
            elif state1==1:
                if self.check.isChecked()==True and self.check.text()=='Use saved password':
                    p.sendline('y')
                else:
                    p.sendline('n')
                    p.sendline(self.user.text())
                    p.sendline(self.paw.text())
                    if self.check.isChecked()==True:
                        p.sendline('y')
                    else:
                        p.sendline('n')
            else:
                p.sendline(self.user.text())
                p.sendline(self.paw.text())
                if self.check.isChecked()==True:
                    p.sendline('y')
                else:
                    p.sendline('n')
            print('sent cred')
            state2=p.expect(['Select server:',pexpect.EOF])
            print('pass expect 2')
            print(state2)
            if state2==1:
                text=p.before.decode('utf-8')
                if '-1002' in text:
                    print('no pc')
                    p.close
                    self.done.emit(3,'')
                else:
                    prelim='Unexpected error\n Error log:\n'
                    text=prelim+text
                    print(text)
                    p.close()
                    self.done.emit(0, text)
                    
            else:
                serv=p.before.decode('utf-8')
                a=serv.find('1)')
                serv=serv[a:]
                print(serv)
                p.close()
                self.done.emit(3,serv)
        return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FirstUI = QtWidgets.QMainWindow()
    ui = Ui_ParsecUI()
    ui.setupUi(FirstUI)
    FirstUI.show()
    sys.exit(app.exec_())
