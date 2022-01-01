from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMenuBar, QMessageBox

class MenuBar(QMenuBar):
    def __init__(self, parent=None):
        super(MenuBar, self).__init__(parent)

        self.setGeometry(QtCore.QRect(0, 0, 890, 22))
        self.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self)
        self.menuAbout.setObjectName("menuAbout")
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(self)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(self)
        self.actionHelp.setObjectName("actionHelp")
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionHelp)
        self.addAction(self.menuAbout.menuAction())
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.menuAbout.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))

    def about(self):
        '''Message box for about tab'''
        msg = QMessageBox()
        msg.setWindowTitle("About")
        msg.setText("RSS Reader is a simple rss reader\n"
                    "created by Julian Gonzalez.")
        img = QtGui.QPixmap("./src/img/author.jpg")
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