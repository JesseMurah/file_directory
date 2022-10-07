import sys
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QBoxLayout, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QListView, QListWidget, QListWidgetItem, QPushButton, QVBoxLayout, QWidget, QWidgetItem

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 300))
        self.initializeInterface()


    def initializeInterface(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        gbox = QGridLayout()
       
        self.setLayout(vbox)
        self.setLayout(hbox)
        vbox.addLayout(gbox)
        
    
        hbox = QHBoxLayout()
        self.name = QLineEdit()
        self.name.setPlaceholderText("input")
        

        n1 = QPushButton('7', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n1, 1, 1)
        
        n2 = QPushButton('8', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n2, 1, 2)
        
        n3 = QPushButton('9', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n3, 1, 3)
        
        n4 = QPushButton('/', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n4, 1, 4)

        n5 = QPushButton('4', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n5, 2, 1)

        n6 = QPushButton('5', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n6, 2, 2)
        
        n7 = QPushButton('6', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n7, 2, 3)

        n8 = QPushButton('*', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n8, 2, 4)

        n9 = QPushButton('1', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n9, 3, 1)
        
        n10 = QPushButton('2', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n10, 3, 2)

        n11 = QPushButton('3', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n11, 3, 3)

        n12 = QPushButton('-', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n12, 3, 4)
        
        n13 = QPushButton('0', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n13, 4, 1)

        n14 = QPushButton('.', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n14, 4, 2)

        n15 = QPushButton('=', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n15, 4, 3)
        
        n16 = QPushButton('+', self)
        #n1.setPlaceholderText("7")
        gbox.addWidget(n16, 4, 4)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

