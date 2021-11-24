# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from readRSS import ReadRSS

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, data):
        MainWindow.setObjectName("Rss Reader")
        MainWindow.resize(890, 591)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 20, 221, 471))
        self.treeView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 500, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.text = "Add Feed"
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(260, 30, 20, 471))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.menubar.addAction(self.menuAbout.menuAction())

        # tree view
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Feeds"])
        self.treeView.setModel(self.model)
        self.importData(data)
        self.treeView.clicked.connect(self.loadContent)

        # Connect Menu actions
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def importData(self, data):
        '''Add feed keys and titles'''
        root = self.model.invisibleRootItem()
        for item in data:
            for key in item:
                parent = QtGui.QStandardItem(key)
                parent.setEditable(False)
                titles = self.addTitles(item[key])
                for title in titles:
                    t = QtGui.QStandardItem(title)
                    t.setEditable(False)
                    parent.appendRow(t)
                root.appendRow(parent)         

    def addTitles(self, url):
        reader = ReadRSS(url)
        return reader.getTitles()
    
    def loadContent(self):
        index = QtCore.QModelIndex(self.treeView.currentIndex())
        print(index.data())

    def about(self):
        '''Message box for about tab'''
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("RSS Reader is a simple rss reader\n"
                    "created by Julian Gonzalez.")
        img = QtGui.QPixmap("author.jpg")
        msg.setIconPixmap(img.scaled(QtCore.QSize(150,150), 
                          transformMode=QtCore.Qt.SmoothTransformation))

        runMsg = msg.exec_()

    def help(self):
        '''Message box for help tab'''
        msg = QMessageBox()
        msg.setWindowTitle("RSS Reader Help")
        msg.setIcon(QMessageBox.Question)
        msg.setText("Select an rss feed from the list on the left\n"
                    "and the view on the right will display that feed")

        runMsg = msg.exec_()


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
