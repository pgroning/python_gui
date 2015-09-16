#! /usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import pyqtSlot

from pyDraw import Bundle

#class mainGUI(QtGui.QWidget):
class mainGUI(QtGui.QMainWindow):
    
    def __init__(self):
        super(mainGUI, self).__init__()
        self.initUI()

        
    def initUI(self):
        

        # Layout buttons with layout classes
        #okButton = QtGui.QPushButton("OK")
        #cancelButton = QtGui.QPushButton("Cancel")

        #hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        #hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)

        #vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)
        #vbox.addLayout(hbox)
        
        #self.setLayout(vbox)   


        # Set window size and position
        #self.setGeometry(300, 300, 800, 600)
        self.resize(600,600)
        #self.setMinimumWidth(600)
        #self.setMinimumHeight(600)
        #self.center()
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        # Set window title
        self.setWindowTitle("Bundle Inspector")

        # Set window icon
        self.setWindowIcon(QtGui.QIcon('bird-icon_32x32.png'))

        # Create status bar
        self.statusBar().showMessage('Ready')

        # Create menu bar
        menuBar = self.menuBar()
        # Add file menu to menubar
        fileMenu = menuBar.addMenu('&File')

        # Create file open action
        openFile = QtGui.QAction(QIcon('doc-icon_32x32.png'), 'Open file...', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open file...')
        openFile.triggered.connect(self.fileDialog)

        # Add file choice action to file menu
        fileMenu.addAction(openFile)

        # Create exit action
        fileMenu.addSeparator()
        exitAction = QAction(QIcon('exit-icon_32x32.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)
        exitAction.triggered.connect(self.close)
        
        # Add exit action to file menu
        fileMenu.addAction(exitAction)

        # Add toolbar
        #self.toolbar = self.addToolBar('Exit')
        #self.toolbar.addAction(exitAction)

        #cw = self.centralWidget
        #cw = QtGui.QWidget()
        cw = QtGui.QFrame()
        self.setCentralWidget(cw)


        #self.centralWidget = QtGui.QWidget()
        #self.setCentralWidget(self.centralWidget)

        #cw.btn = QtGui.QPushButton('Quit!', cw)
        #self.centralWidget.btn = QtGui.QPushButton('Quit!', self.centralWidget)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        cw.setLayout(grid)

        b = Bundle()
        grid.addWidget(b,1,0,10,10)

        print b.click_x, b.click_y

        # Add text frames
        self.lineEdit = QtGui.QLineEdit()
        #grid.addWidget(self.lineEdit, 1, 1, 1, 2)
        
        self.textEdit = QtGui.QTextEdit()
        #grid.addWidget(self.textEdit, 5, 0, 2, 3)
        self.textEditLabel = QtGui.QLabel('<b>Text string enters here</b>')
        font = self.textEditLabel.font()
        font.setPointSize(16)
        self.textEditLabel.setFont(font)
        grid.addWidget(self.textEditLabel, 0, 5, 1, 1)

        
        self.btn = QtGui.QPushButton('button', cw)
            #title = QtGui.QLabel('Title')
        grid.addWidget(self.btn, 10, 10)
            #grid.addWidget(title,1,1)

        #cw.btn = QtGui.QPushButton('Quit!', cw)



        #self.centralWidget = QtGui.QWidget()
        #cw = self.centralWidget

        # Add a button
        #cw.btn = QtGui.QPushButton('Quit!', cw)
        #cw.btn.


        #self.centralWidget.btn = QtGui.QPushButton('Quit!', self)
        #self.centralWidget.btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #self.centralWidget.btn.resize(self.btn.sizeHint())
        #self.centralWidget.btn.move(155, 155)
        #cw.btn.setToolTip('Click here!')



        #qbtn = QtGui.QPushButton('Quit', self)
        #qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #qbtn.resize(qbtn.sizeHint())
        #qbtn.move(55, 55)
        
        # Add a button
        #self.btn = QtGui.QPushButton('Quit!', self)
        #self.btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        #self.btn.resize(self.btn.sizeHint())
        #self.btn.move(155, 155)
        #self.btn.setToolTip('Click here!')

        # Create some actions 
        #@pyqtSlot()
        #def on_click():
        #    print('clicked')
 
        #@pyqtSlot()
        #def on_press():
        #    print('pressed')
 
        #@pyqtSlot()
        #def on_release():
        #    print('released')

        # connect the signals to the slots
        #self.btn.clicked.connect(on_click)
        #self.btn.pressed.connect(on_press)
        #self.btn.released.connect(on_release)

        # Layout buttons with layout classes
        #okButton = QtGui.QPushButton("OK")
        #cancelButton = QtGui.QPushButton("Cancel")

        #hbox = QtGui.QHBoxLayout()
        #hbox.addStretch(1)
        #hbox.addWidget(okButton)
        #hbox.addWidget(cancelButton)

        #vbox = QtGui.QVBoxLayout()
        #vbox.addStretch(1)
        #vbox.addLayout(hbox)
        
        #self.setLayout(vbox)    


        # Add text frame
        #self.le = QtGui.QLineEdit(self)
        #self.le.move(130, 200)

        #self.centralWidget.show()

        self.show()

    """
    # Fetch  mouse press events
    def mousePressEvent(self, mouse_evt):
        
        #super(Bundle, self).mousePressEvent(event)
            
        button = mouse_evt.button()
        #item = self.itemAt(mouse_evt.x(), mouse_evt.y())
        
        if button == 1:
            print 'SIMPLE LEFT CLICK!'
            print mouse_evt.x(), mouse_evt.y()
            #self.drawsquare(mouse_evt.x(),mouse_evt.y())
            if button == 2:
                print 'SIMPLE RIGHT CLICK!'
                print mouse_evt.x(), mouse_evt.y()
    """         
        

    def fileDialog(self):

        fileName = QtGui.QFileDialog.getOpenFileName(self, "Open Data File", "/", "Text files (*.txt)") 
        if fileName:
            f = open(fileName, 'r')
            data = f.read()
            self.textEdit.setText(data)
        

    def closeEvent(self, event):
        
        reply = QtGui.QMessageBox.question(self, 'Message',
             "Are you sure to quit?", QtGui.QMessageBox.Yes | 
             QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   


        
def main():
    # Create an PyQT4 application object.
    app = QtGui.QApplication(sys.argv)
    
    w = mainGUI()

    #b = Bundle()

    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()

