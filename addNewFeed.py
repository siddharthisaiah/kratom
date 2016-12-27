# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewFeed.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(587, 170)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(220, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.feedLinkLabel = QtGui.QLabel(Dialog)
        self.feedLinkLabel.setGeometry(QtCore.QRect(50, 30, 41, 16))
        self.feedLinkLabel.setObjectName(_fromUtf8("feedLinkLabel"))
        self.feedLinkLineEdit = QtGui.QLineEdit(Dialog)
        self.feedLinkLineEdit.setGeometry(QtCore.QRect(50, 50, 481, 21))
        self.feedLinkLineEdit.setObjectName(_fromUtf8("feedLinkLineEdit"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Add A New Feed", None))
        self.feedLinkLabel.setText(_translate("Dialog", "URL :", None))

