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

import sys, random
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
        self.setBackground(qp)
        #qp.setBrush(QtCore.Qt.white)
        self.drawCRD(qp)
        self.drawBox(qp)
        self.drawQuad(qp)
        #self.Background(qp)
        self.drawChannel(qp)
        self.drawCircles(qp)
        qp.end()

    def setBackground(self, qp):
        qp.setBrush(QtCore.Qt.white)
        s = self.size()
        qp.drawRect(0,0,s.width(),s.height())
        
    def drawCRD(self, qp):
        # Paint crd
        pen = QtGui.QPen(QtCore.Qt.black, 8, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(20, 20, 540, 20)
        qp.drawLine(20, 20, 20, 540) 

    def drawBox(self, qp):

        #qp.setBrush(QtCore.Qt.white)
        # Paint box
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(40, 40, 540, 540)

    def drawQuad(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#B0E2FF')
        #qp.setPen(color)

        pen = QtGui.QPen(color, 40, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        chanLength = 140
        chanWidth = 40

        qp.drawLine(60, 310, 560, 310)
        qp.drawLine(310, 60, 310, 560)

        pen = QtGui.QPen(color, 140, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(310,310,312,312)

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

    def Background(self, qp):
        pen = QtGui.QPen(QtCore.Qt.blue, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.blue)

        # Background color
        c = 310
        w = 40
        qp.drawRect(c-w/2,40,w,540)
        #qp.rotate(-45)

    def drawCircles(self, qp):
        # Paint circles
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.setBrush(QtCore.Qt.green)

        # Quad 1
        for i in range(5):
            for j in range(5):
                if (i,j) == (4,4):
                    continue
                else:
                    r = random.random()
                    if r < 0.25:
                        qp.setBrush(QtCore.Qt.blue)
                    elif r < 0.5:
                        qp.setBrush(QtCore.Qt.yellow)
                    elif r < 0.75:
                        qp.setBrush(QtCore.Qt.green)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(45+i*49,45+j*49,42,42)

        # Quad 2
        for i in range(5,10):
            for j in range(0,5):
                if (i,j) == (5,4):
                    continue
                else:
                    r = random.random()
                    if r < 0.25:
                        qp.setBrush(QtCore.Qt.blue)
                    elif r < 0.5:
                        qp.setBrush(QtCore.Qt.yellow)
                    elif r < 0.75:
                        qp.setBrush(QtCore.Qt.green)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(90+i*49,45+j*49,42,42)
        
        # Quad 3
        for i in range(0,5):
            for j in range(5,10):
                if (i,j) == (4,5):
                    continue
                else:
                    r = random.random()
                    if r < 0.25:
                        qp.setBrush(QtCore.Qt.blue)
                    elif r < 0.5:
                        qp.setBrush(QtCore.Qt.yellow)
                    elif r < 0.75:
                        qp.setBrush(QtCore.Qt.green)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(45+i*49,90+j*49,42,42)
        
        # Quad 4
        for i in range(5,10):
            for j in range(5,10):
                if (i,j) == (5,5):
                    continue
                else:
                    r = random.random()
                    if r < 0.25:
                        qp.setBrush(QtCore.Qt.blue)
                    elif r < 0.5:
                        qp.setBrush(QtCore.Qt.yellow)
                    elif r < 0.75:
                        qp.setBrush(QtCore.Qt.green)
                    else:
                        qp.setBrush(QtCore.Qt.red)
                    qp.drawEllipse(90+i*49,90+j*49,42,42)
        


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
