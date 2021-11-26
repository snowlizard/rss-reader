# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogA.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class AddFeedDialog(QtWidgets.QDialog):
    def setupUi(self, FeedDialog):
        self.value = 0
        FeedDialog.setObjectName("FeedDialog")
        FeedDialog.resize(400, 248)
        self.nameLabel = QtWidgets.QLabel(FeedDialog)
        self.nameLabel.setGeometry(QtCore.QRect(20, 60, 71, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.urlLable = QtWidgets.QLabel(FeedDialog)
        self.urlLable.setGeometry(QtCore.QRect(20, 120, 61, 31))
        self.urlLable.setObjectName("urlLable")
        self.nameEdit = QtWidgets.QLineEdit(FeedDialog)
        self.nameEdit.setGeometry(QtCore.QRect(110, 70, 261, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.urlEdit = QtWidgets.QLineEdit(FeedDialog)
        self.urlEdit.setGeometry(QtCore.QRect(100, 120, 271, 31))
        self.urlEdit.setObjectName("lineEdit")
        self.cancelBtn = QtWidgets.QPushButton(FeedDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(230, 190, 151, 41))
        self.cancelBtn.setObjectName("cancelBtn")
        self.addBtn = QtWidgets.QPushButton(FeedDialog)
        self.addBtn.setGeometry(QtCore.QRect(80, 190, 141, 41))
        self.addBtn.setObjectName("addBtn")

        self.retranslateUi(FeedDialog)
        QtCore.QMetaObject.connectSlotsByName(FeedDialog)

        # button events
        self.addBtn.clicked.connect(lambda: self.setValueDict(FeedDialog))
        self.cancelBtn.clicked.connect(FeedDialog.reject)

    def retranslateUi(self, FeedDialog):
        _translate = QtCore.QCoreApplication.translate
        FeedDialog.setWindowTitle(_translate("FeedDialog", "Dialog"))
        self.nameLabel.setText(_translate("FeedDialog", "Feed Name"))
        self.urlLable.setText(_translate("FeedDialog", "     URL"))
        self.cancelBtn.setText(_translate("FeedDialog", "Cancel"))
        self.addBtn.setText(_translate("FeedDialog", "Add"))

    def setValueDict(self, feedDialog):
        text = self.nameEdit.text()
        url = self.urlEdit.text()
        self.value = {text: url}
        feedDialog.accept()