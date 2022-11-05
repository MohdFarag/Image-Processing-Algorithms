# importing Qt widgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class TableView(QTableWidget):
    def __init__(self,*args):
        QTableWidget.__init__(self, *args)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(['Frequency','Magnitude','Phase'])
 
    def addData(self, frequency, magnitude, phase): 
        rowPosition = self.rowCount()

        self.insertRow(rowPosition)
        self.setItem(rowPosition , 0, QTableWidgetItem(f"{frequency}Hz"))
        self.setItem(rowPosition , 1, QTableWidgetItem(f"{magnitude}"))
        self.setItem(rowPosition , 2, QTableWidgetItem(f"{phase}°"))

    def clearAllData(self):
        self.setRowCount(0)


class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class QVLine(QFrame):
    def __init__(self):
        super(QVLine, self).__init__()
        self.setFrameShape(QFrame.VLine)
        self.setFrameShadow(QFrame.Sunken)
