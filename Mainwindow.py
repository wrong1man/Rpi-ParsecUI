# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from errord import Ui_Error as Form2
import pexpect
class Ui_Dialog(object):
    def setupUi(self, Dialog, user, pw, serv):
        print('main win')
        #Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint) Removes title bar
        Dialog.setObjectName("Dialog")
        Dialog.resize(768, 564)
        Dialog.setMinimumSize(QtCore.QSize(0, 480))
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabbar = QtWidgets.QFrame(Dialog)
        self.tabbar.setMinimumSize(QtCore.QSize(0, 48))
        self.tabbar.setMaximumSize(QtCore.QSize(16777215, 58))
        self.tabbar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom: 1px solid rgb(229, 229, 236);")
        self.tabbar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tabbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tabbar.setObjectName("tabbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tabbar)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.playtab = QtWidgets.QLabel(self.tabbar)
        self.playtab.setObjectName("playtab")
        self.horizontalLayout.addWidget(self.playtab)
        self.friendstab = QtWidgets.QLabel(self.tabbar)
        self.friendstab.setObjectName("friendstab")
        self.horizontalLayout.addWidget(self.friendstab)
        self.hosttab = QtWidgets.QLabel(self.tabbar)
        self.hosttab.setObjectName("hosttab")
        self.horizontalLayout.addWidget(self.hosttab)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.help = QtWidgets.QLabel(self.tabbar)
        self.help.setObjectName("help")
        self.horizontalLayout.addWidget(self.help)
        self.username = QtWidgets.QLabel(self.tabbar)
        self.username.setStyleSheet("font: 75 10pt \"Arial Rounded MT Bold\";\n"
"color: rgb(153, 153, 179);")
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.settings = QtWidgets.QPushButton(self.tabbar)
        self.settings.setMinimumSize(QtCore.QSize(43, 47))
        self.settings.setStyleSheet("QPushButton#settings{\n"
"background-image:url(options.png);\n"
"    border: 0px solid rgb(229, 229, 236);\n"
"}\n"
"\n"
"QPushButton#settings:hover {\n"
" \n"
"    background-image: url(optionshover.png);\n"
" }\n"
"")
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.minb = QtWidgets.QPushButton(self.tabbar)
        self.minb.setMinimumSize(QtCore.QSize(40, 47))
        self.minb.setMaximumSize(QtCore.QSize(40, 47))
        self.minb.setStyleSheet("QPushButton#minb{\n"
"    \n"
"    background-image: url(:/all/resources/minimize.png);\n"
"    border: 0px solid rgb(229, 229, 236);\n"
"}\n"
"\n"
"QPushButton#minb:hover {\n"
" \n"
"    background-image: url(:/all/resources/minimizehover.png);\n"
" }")
        self.minb.setText("")
        self.minb.setObjectName("minb")
        self.horizontalLayout.addWidget(self.minb)
        self.maxb = QtWidgets.QPushButton(self.tabbar)
        self.maxb.setMinimumSize(QtCore.QSize(40, 47))
        self.maxb.setMaximumSize(QtCore.QSize(40, 47))
        self.maxb.setStyleSheet("QPushButton#maxb{\n"
"    \n"
"    background-image: url(:/all/resources/maximize.png);\n"
"    border: 0px solid rgb(229, 229, 236);\n"
"}\n"
"\n"
"QPushButton#maxb:hover {\n"
" \n"
"    background-image: url(:/all/resources/maximizehover.png);\n"
" }")
        self.maxb.setText("")
        self.maxb.setObjectName("maxb")
        self.horizontalLayout.addWidget(self.maxb)
        self.closeb = QtWidgets.QPushButton(self.tabbar)
        self.closeb.setMinimumSize(QtCore.QSize(40, 48))
        self.closeb.setMaximumSize(QtCore.QSize(40, 48))
        self.closeb.setStyleSheet("QPushButton#closeb{;\n"
"    background-image: url(:/all/resources/close.png);\n"
"    border: 0px solid rgb(229, 229, 236);\n"
"}\n"
"\n"
"QPushButton#closeb:hover {\n"
" \n"
";\n"
"    background-image: url(:/all/resources/closehover.png);\n"
" }")
        self.closeb.setText("")
        self.closeb.setObjectName("closeb")
        self.horizontalLayout.addWidget(self.closeb)
        self.verticalLayout.addWidget(self.tabbar)
        self.mainframe = QtWidgets.QFrame(Dialog)
        self.mainframe.setStyleSheet("background-color: rgb(247, 247, 250);")
        self.mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainframe.setObjectName("mainframe")
        self.gridLayout = QtWidgets.QGridLayout(self.mainframe)
        self.gridLayout.setObjectName("gridLayout")
        self.reloadb = QtWidgets.QPushButton(self.mainframe)
        self.reloadb.setMinimumSize(QtCore.QSize(70, 30))
        self.reloadb.setMaximumSize(QtCore.QSize(70, 30))
        self.reloadb.setStyleSheet("QPushButton#reloadb {\n"
"    font: 75 12pt \"MS Reference Sans Serif\";\n"
"    background-color: white;\n"
"    border: 1px solid rgb(229, 229, 236);\n"
"    border-radius: 5px\n"
"\n"
" }\n"
"QPushButton#reloadb:hover {\n"
"    color: rgb(17, 29, 255);\n"
" }\n"
"QPushButton#reloadb:hover:!pressed\n"
"{\n"
"  border: 1px solid  rgb(153, 153, 179);\n"
"}\n"
"\n"
"QPushButton#reloadb {\n"
"color: rgb(75, 87, 244);\n"
"}\n"
"QPushButton#reloadb {\n"
"font: 75 10pt \"Arial Rounded MT Bold\";\n"
"\n"
"}")
        self.reloadb.setObjectName("reloadb")
        self.gridLayout.addWidget(self.reloadb, 0, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 0, 1, 1)
        self.computers = QtWidgets.QLabel(self.mainframe)
        self.computers.setMaximumSize(QtCore.QSize(16777215, 150))
        self.computers.setStyleSheet("font: 14pt bold \"Bahnschrift\";")
        self.computers.setObjectName("computers")
        self.gridLayout.addWidget(self.computers, 0, 2, 1, 1)
        self.pcname1 = QtWidgets.QLabel(self.mainframe)
        self.pcname1.setStyleSheet("font: 87 12pt \"Arial Black\";")
        self.pcname1.setObjectName("pcname1")
        self.gridLayout.addWidget(self.pcname1, 1, 3, 1, 1)
        self.pcimg = QtWidgets.QLabel(self.mainframe)
        self.pcimg.setStyleSheet("background url(:/all/resources\pc.png)")
        self.pcimg.setObjectName("pcimg")
        self.gridLayout.addWidget(self.pcimg, 1, 2, 1, 1)
        self.playb1 = QtWidgets.QPushButton(self.mainframe)
        self.playb1.setMinimumSize(QtCore.QSize(82, 43))
        self.playb1.setStyleSheet("QPushButton#playb1 {\n"
"    font: 75 12pt \"MS Reference Sans Serif\";\n"
"    background-color: rgb(75, 87, 244);\n"
"    border: 1px solid rgb(229, 229, 236);\n"
"    border-radius: 10px\n"
"\n"
" }\n"
"QPushButton#playb1:hover {\n"
"    background-color: rgb(17, 29, 255);\n"
" }\n"
"QPushButton#playb1:hover:!pressed\n"
"{\n"
"  border: 1px solid  rgb(153, 153, 179);\n"
"}\n"
"\n"
"QPushButton#playb1 {\n"
"color: white;\n"
"}\n"
"QPushButton#playb1 {\n"
"font: 75 10pt \"Arial Rounded MT Bold\";\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/all/resources/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.playb1.setObjectName("playb1")
        self.gridLayout.addWidget(self.playb1, 1, 5, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 4, 1, 1)
        self.verticalLayout.addWidget(self.mainframe)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        
        #end of ui code

        self.pcimg.hide()
        self.playb1.hide()
        self.closeb.clicked.connect(Dialog.close)
        self.minb.clicked.connect(Dialog.showMinimized)
        self.maxb.clicked.connect(Dialog.showMaximized)
        self.setservn(serv)
        self.playb1.clicked.connect(lambda: self.play(user,pw))
        self.reloadb.clicked.connect(lambda: self.reload(user,pw))
            
    def setservn(self,serv): #sets server name 
        print('enter sevrer set name')
        if  serv is not '':
            print('setting name')
            text=str(serv)
            self.pcname1.setText(text)
            self.pcimg.show()
            self.playb1.show()
        else:
            text=('No computers Available')
            print (text)
            self.pcname1.setText(text)
            self.pcimg.hide()
            self.playb1.hide()
        
    def play(self,usr,pw): #access server - should be integrated into reload; didn't work
        print('enter play')
        p=pexpect.spawn('parsec')
        state1=p.expect(['Email address:','saved',pexpect.EOF])
        print(state1)
        if state1== 1:
            p.sendline('n')
        else:
            pass
        p.sendline(usr)
        p.expect('Password:')
        p.sendline(pw)
        p.expect('Save')
        p.sendline('n')
        print('sent cred')
        a=p.expect(['server:', pexpect.EOF])
        print('expect 2:', a)
        if a==0:
            print('send 1')
            p.sendline('1')
            p.expect(pexpect.EOF, timeout=None)
        else:
            self.reload(usr,pw)

        
    def reload(self,user,pw): #reload function
        print ('enter reload')
        p=pexpect.spawn('parsec')
        print('spawned')
        state1=p.expect(['Email address:','saved',pexpect.EOF])
        print('pass expect 1')
        print(state1)
        if state1==2:
            #errordiag
            text=p.before.decode('utf-8')
            prelim='Something went wrong - Try to task kill all parsec processes through task manager!-\n Error log:\n'
            text= prelim+ str(text) + 'THIS WAS A CRITICAL ERROR - CLOSING GUI'
            critica=1
            print(text)
            p.close()
            self.errordiag(text,critica)
        elif state1==1:
            p.sendline('n')
        else:
            pass
        p.sendline(user)
        p.sendline(pw)
        p.sendline('n')
        print('sent cred')
        state2=p.expect(['Select server:',pexpect.EOF])
        print('pass expect 2')
        print(state2)
        if state2==1:
            text=p.before.decode('utf-8')
            if '-1002' in text and self.pcname1.text() is not 'No computers Available':
                print('no pc')
                p.close
                self.setservn('')
            else:
                prelim='Unexpected error\n Error log:\n'
                text=prelim+text +' This error might not be critical, try again.\n If the error persists restart the GUI'
                critica=0
                print(text)
                p.close()
                pass
                
        else:
            serv=p.before.decode('utf-8')
            a=serv.find('1)')
            serv=serv[a:]
            print(serv)
            self.setservn(serv)
            p.close

             
        
                    
    def errordiag(self,error,crit): #error dialog function
        disptxt=error
        errord = QtWidgets.QDialog()
        errord.ui = Form2()
        errord.ui.setupUi(errord, disptxt)
        errord.exec_()
        errord.show()
        print(crit)
        if crit==1:
            Dialog.close
        else:
            pass
       
                    
                    

        
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.playtab.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/all/resources/playtabgray.png\"/></p></body></html>"))
        self.friendstab.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/all/resources/friend.png\"/></p></body></html>"))
        self.hosttab.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/all/resources/host.png\"/></p></body></html>"))
        self.help.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/all/:/all/:/all/resources/help.png\"/></p></body></html>"))
        self.username.setText(_translate("Dialog", "<html><head/><body><p>WrongMan<br/>#xxxxxx</p></body></html>"))
        self.reloadb.setText(_translate("Dialog", "Reload"))
        self.computers.setText(_translate("Dialog", "Computers"))
        self.pcname1.setText(_translate("Dialog", "No computers Available"))
        self.pcimg.setText(_translate("Dialog", "<html><head/><body><p><img src=\":/all/:/all/:/all/resources/pc.png\"/></p></body></html>"))
        self.playb1.setText(_translate("Dialog", "PLAY"))

