#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial 

In this example we draw 6 lines using
different pen styles. 

author: Jan Bodnar
website: zetcode.com 
last edited: September 2011
"""

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Bundle')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        #qp.setBrush(QtCore.Qt.white)
        self.drawCRD(qp)
        self.drawBox(qp)
        self.drawQuad(qp)
        self.drawChannel(qp)
        qp.end()

        
    def drawCRD(self, qp):
      
        # Paint crd
        pen = QtGui.QPen(QtCore.Qt.black, 8, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(20, 20, 540, 20)
        qp.drawLine(20, 20, 20, 540) 

    def drawBox(self, qp):

        qp.setBrush(QtCore.Qt.white)
        # Paint box
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(40, 40, 540, 540)

    def drawQuad(self, qp):

        # Paint channel
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        chanLength = 140
        chanWidth = 40

        qp.drawLine(0, 310, 600, 310)
        qp.drawLine(310, 0, 310, 600)

    def drawChannel(self, qp):

        # Paint channel
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        cLength = 140
        cWidth = 40

        c = 310
        z = 80
        z1 = 70;
        #
        qp.drawLine(40, c-cWidth/2, 300-z1, c-cWidth/2)
        qp.drawLine(40, c+cWidth/2, 300-z1, c+cWidth/2)

        qp.drawLine(c+z, c-cWidth/2, 600-20, c-cWidth/2)
        qp.drawLine(c+z, c+cWidth/2, 600-20, c+cWidth/2)
        #
        qp.drawLine(c-cWidth/2, 40, c-cWidth/2, c-z)
        qp.drawLine(c+cWidth/2, 40, c+cWidth/2, c-z)
        
        qp.drawLine(c-cWidth/2, 600-20, c-cWidth/2, c+z)
        qp.drawLine(c+cWidth/2, 600-20, c+cWidth/2, c+z)


        qp.drawLine(300-z1, c-cWidth/2, c-cWidth/2, c-z)
        qp.drawLine(300-z1, c+cWidth/2, c-cWidth/2, c+z)
        qp.drawLine(c+cWidth/2, c-z, c+z, c-cWidth/2)
        qp.drawLine(c+z, c+cWidth/2, c+cWidth/2, c+z)


        '''
        # Q1
        x11 = 40
        y11 = 260 - chanWidth/2
        x12 = x11 + chanLength
        y12 = y11
        qp.drawLine(x11, y11, x12, y12)

        x21 = y11
        y21 = x11
        x22 = x21
        y22 = x12
        qp.drawLine(x21, y21, x22, y22)
        
        qp.drawLine(x12, y12, x22, y22)

        x11 = 40
        y11 = 260 + chanWidth/2
        x12 = x11 + chanLength
        y12 = y11
        qp.drawLine(x11, y11, x12, y12)

        x21 = 260 - chanWidth/2
        y21 = 480 + 40
        x22 = x21
        y22 = y21 - chanLength
        qp.drawLine(x21, y21, x22, y22)
        
        qp.drawLine(x12, y12, x22, y22)

        # Q2
        x11 = y21
        y11 = x21
        x12 = y22
        y12 = y11
        qp.drawLine(x11, y11, x12, y12)

        x21 = 260 + chanWidth/2
        y21 = 40
        x22 = x21
        y22 = 40 + chanLength
        qp.drawLine(x21, y21, x22, y22)

        qp.drawLine(x12, y12, x22, y22)


        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#d4d4d4')
        qp.setBrush(QtGui.QColor(255, 80, 0, 160))



        #pen.setStyle(QtCore.Qt.DashLine)
        #qp.setPen(pen)
        #qp.drawLine(20, 80, 250, 80)

        #pen.setStyle(QtCore.Qt.DashDotLine)
        #qp.setPen(pen)
        #qp.drawLine(20, 120, 250, 120)

        #pen.setStyle(QtCore.Qt.DotLine)
        #qp.setPen(pen)
        #qp.drawLine(20, 160, 250, 160)

        #pen.setStyle(QtCore.Qt.DashDotDotLine)
        #qp.setPen(pen)
        #qp.drawLine(20, 200, 250, 200)

        #pen.setStyle(QtCore.Qt.CustomDashLine)
        #pen.setDashPattern([1, 4, 5, 4])
        #qp.setPen(pen)
        #qp.drawLine(20, 240, 250, 240)
        '''      
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
