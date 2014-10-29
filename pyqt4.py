#!/usr/bin/python

import sys
from PyQt4 import QtGui, QtCore

class GUI_Example(QtGui.QWidget):
    
    def __init__(self):
        super(GUI_Example, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        qbtn = QtGui.QPushButton('Quit', self)
        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(55, 55)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')
        self.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = GUI_Example()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
