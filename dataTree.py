from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeView
from dialogA import AddFeedDialog
from readRSS import ReadRSS

class FeedView(QTreeView):
    def __init__(self, parent=None, data=[]) -> None:
        super(QTreeView, self).__init__(parent)

        self.setGeometry(QtCore.QRect(10, 20, 221, 471))

        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Feeds"])
        self.setModel(self.model)
        
        self.data = data
        self.importData()

    def importData(self):
        '''Add feed keys and titles'''
        self.root = self.model.invisibleRootItem()
        for item in self.data:
            for key in item:
                parent = QtGui.QStandardItem(key)
                parent.setEditable(False)
                titles = self.addTitles(item[key])
                for title in titles:
                    t = QtGui.QStandardItem(title)
                    t.setEditable(False)
                    parent.appendRow(t)
                self.root.appendRow(parent)         

    def addTitles(self, url):
        reader = ReadRSS(url)
        return reader.getTitles()
    
    def loadContent(self):
        index = QtCore.QModelIndex(self.currentIndex())
        title = index.data()
        key = index.parent().data()
        for items in self.data:
            for iKey in items:
                if iKey == key:
                    rss = ReadRSS(items[iKey])
                    contents = rss.getContent(title)
        return contents

    def addFeed(self):
        dialog = QtWidgets.QDialog()
        window = AddFeedDialog()
        window.setupUi(dialog)
        dialog.show()
        
        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.data.append(window.value)
            key = list(window.value.keys())[0]
            if key != "" or window.value[key] != "":
                rss = ReadRSS(window.value[key])
                parent = QtGui.QStandardItem(key)
                for title in rss.getTitles():
                    t = QtGui.QStandardItem(title)
                    parent.appendRow(t)
                self.root.appendRow(parent)