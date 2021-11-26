# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWebEngineWidgets import *
from dataTree import FeedView
from menubar import MenuBar

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
        # self.delButton.clicked.connecet()

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

    feeds = [
    {"ars index": 'https://feeds.arstechnica.com/arstechnica/index'},
    {"ars features": 'https://feeds.arstechnica.com/arstechnica/features'},
    {"ars tech": 'https://feeds.arstechnica.com/arstechnica/technology-lab'},
    {"ltt programming": 'https://linustechtips.com/forum/20-programming.xml/'}
    ]

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, feeds)
    MainWindow.show()
    sys.exit(app.exec_())
