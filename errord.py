# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Error.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Error(object):
    def setupUi(self, Error, txt):
        Error.setObjectName("Error")
        Error.resize(620, 452)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Error.sizePolicy().hasHeightForWidth())
        Error.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Error)
        self.gridLayout.setObjectName("gridLayout")
        self.errormsg = QtWidgets.QTextBrowser(Error)
        self.errormsg.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.errormsg.setObjectName("errormsg")
        self.gridLayout.addWidget(self.errormsg, 2, 1, 1, 1)
        self.Title = QtWidgets.QLabel(Error)
        self.Title.setObjectName("Title")
        self.gridLayout.addWidget(self.Title, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.okb = QtWidgets.QPushButton(Error)
        self.okb.setMaximumSize(QtCore.QSize(100, 16777215))
        self.okb.setObjectName("okb")
        self.gridLayout.addWidget(self.okb, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 2, 2, 1, 1)

        self.retranslateUi(Error)
        QtCore.QMetaObject.connectSlotsByName(Error)
        self.okb.clicked.connect(Error.close)
        text=txt
        self.errormsg.setText(text)
    def retranslateUi(self, Error):
        _translate = QtCore.QCoreApplication.translate
        Error.setWindowTitle(_translate("Error", "Dialog"))
        self.errormsg.setHtml(_translate("Error", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt;\">PARSEC HAS AN ERROR</span></p></body></html>"))
        self.Title.setText(_translate("Error", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ERROR</span></p></body></html>"))
        self.okb.setText(_translate("Error", "Ók"))


