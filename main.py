# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

import sys

sys.path.insert(1, './src')

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import *
from dataTree import FeedView
from menubar import MenuBar
import json

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("Rss Reader")
        MainWindow.resize(890, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # feed data
        self.data = data
        self.treeView = FeedView(parent=self.centralwidget, data=self.data)

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(10, 500, 101, 41))
        self.addButton.setObjectName("pushButton")

        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(120, 500, 111, 41))
        self.delButton.setObjectName("pushButton_2")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 30, 20, 471))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = MenuBar(parent=MainWindow)
        MainWindow.setMenuBar(self.menuBar)

        # feed browser
        self.browser = QWebEngineView(self.centralwidget)
        self.browser.setGeometry(QtCore.QRect(300, 30, 561, 541))
        self.browser.setUrl(QtCore.QUrl("author.jpg"))

        # actions
        self.treeView.clicked.connect(self.loadFeed)
        self.addButton.clicked.connect(self.treeView.addFeed)
        self.delButton.clicked.connect(self.treeView.removeFeed)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RSS Reader"))
        self.addButton.setText(_translate("MainWindow", "Add Feed"))
        self.delButton.setText(_translate("MainWindow", "Remove Feed"))
    
    def loadFeed(self):
        content = self.treeView.loadContent()
        self.browser.page().setHtml(content)
        self.browser.show()

if __name__ == "__main__":
    import sys

    ofile = open("./src/data.json")
    newFeed = json.load(ofile)
    ofile.close()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, newFeed)
    MainWindow.show()
    sys.exit(app.exec_())
