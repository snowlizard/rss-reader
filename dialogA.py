# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QDialog


class AddFeedDialog(QDialog):
    def __init__(self) -> None:
        super(QDialog, self).__init__()
        self.value = 0
        
        # Auto Generated Qt Designer 5
        self.setObjectName("FeedDialog")
        self.resize(400, 248)
        self.nameLabel = QtWidgets.QLabel(self)
        self.nameLabel.setGeometry(QtCore.QRect(20, 60, 71, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.urlLable = QtWidgets.QLabel(self)
        self.urlLable.setGeometry(QtCore.QRect(20, 120, 61, 31))
        self.urlLable.setObjectName("urlLable")
        self.nameEdit = QtWidgets.QLineEdit(self)
        self.nameEdit.setGeometry(QtCore.QRect(110, 70, 261, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.urlEdit = QtWidgets.QLineEdit(self)
        self.urlEdit.setGeometry(QtCore.QRect(100, 120, 271, 31))
        self.urlEdit.setObjectName("lineEdit")
        self.cancelBtn = QtWidgets.QPushButton(self)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 190, 151, 41))
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(self)
        self.addBtn.setGeometry(QtCore.QRect(80, 190, 141, 41))
        self.addBtn.setObjectName("addBtn")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # button events
        self.addBtn.clicked.connect(lambda: self.setValueDict(self))
        self.cancelBtn.clicked.connect(self.reject)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FeedDialog", "Add rss feed"))
        self.nameLabel.setText(_translate("FeedDialog", "Feed Name"))
        self.urlLable.setText(_translate("FeedDialog", "     URL"))
        self.cancelBtn.setText(_translate("FeedDialog", "Cancel"))
        self.addBtn.setText(_translate("FeedDialog", "Add"))

    def setValueDict(self):
        '''sets the variable value to a dictionary
        with the name and url as key value pairs set
        signal to accept'''
        text = self.nameEdit.text()
        url = self.urlEdit.text()
        self.value = {text: url}
        self.accept()