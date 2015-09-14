#!/usr/bin/python


import sys, random
from PyQt4 import QtGui, QtCore

class Bundle(QtGui.QWidget):
    
    def __init__(self):
        super(Bundle, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.setGeometry(300, 300, 600, 600)
        self.setWindowTitle('Bundle')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()

        qp.begin(self)
        self.setBackground(qp)
        self.drawCRD(qp)
        self.drawBox(qp)
        qp.end()

        qp.begin(self)
        self.drawChannels(qp)
        qp.end()

        qp.begin(self)
        self.drawDiamond(qp)
        qp.end()

        qp.begin(self)
        self.paintCorners(qp)
        qp.end()

        qp.begin(self)
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
        s = self.size()
        qp.drawLine(20, 20, 555, 20)
        qp.drawLine(20, 20, 20, 555) 

    def drawBox(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawRect(40, 40, 540, 540)

    def drawQuad(self, qp):

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#B0E2FF')

        pen = QtGui.QPen(color, 40, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        chanLength = 140
        chanWidth = 40

        qp.drawLine(60, 310, 560, 310)
        qp.drawLine(310, 60, 310, 560)

        pen = QtGui.QPen(color, 140, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(310,310,312,312)

    def drawDiamond(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)

        s = self.size()
        d = 140 # Box size
        
        qp.translate(310, 210)
        qp.rotate(45)
        qp.drawRect(0,0,d,d)

    def paintCorners(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue

        c = 310
        d = 28
        pen = QtGui.QPen(color, d, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        qp.drawPoint(220,c)
        qp.drawPoint(400,c)
        qp.drawPoint(c,220)
        qp.drawPoint(c,400)


    def drawChannels(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)

        s = self.size()
        d = 30
        c = 310
        qp.drawRect(40,c-d/2,540,d)
        qp.drawRect(c-d/2,40,d,540)

    def drawCircles(self, qp):
        
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        r = 40

        color = QtGui.QColor(0, 0, 0)

        # Quad 1
        for i in range(5):
            for j in range(5):
                if (i,j) == (4,4):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(45+i*49,45+j*49,r,r)

        # Quad 2
        for i in range(5,10):
            for j in range(0,5):
                if (i,j) == (5,4):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(90+i*49,45+j*49,r,r)
        
        # Quad 3
        for i in range(0,5):
            for j in range(5,10):
                if (i,j) == (4,5):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(45+i*49,90+j*49,r,r)
        
        # Quad 4
        for i in range(5,10):
            for j in range(5,10):
                if (i,j) == (5,5):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(90+i*49,90+j*49,r,r)
        

    def setColor(self, qp):
        color = QtGui.QColor(0, 0, 0)
        r = random.random()
        if r < 0.1:
            color = QtGui.QColor(255, 0, 255) # purple
            qp.setBrush(color)
        elif r < 0.2:
            color = QtGui.QColor(200, 0, 255) # violet
                        #color.setNamedColor('#A020F0') # violet
            qp.setBrush(color)
                        #qp.setBrush(QtCore.Qt.blue)
        elif r < 0.3:
            color = QtGui.QColor(0, 0, 255) # blue
            qp.setBrush(color)
                        #qp.setBrush(QtCore.Qt.blue)
        elif r < 0.4:
            color = QtGui.QColor(0, 200, 255) # light blue
                        #color.setNamedColor('#63D1F4') # light blue
            qp.setBrush(color)
        elif r < 0.5:
            color = QtGui.QColor(0, 255, 0) # green
                        #qp.setBrush(QtCore.Qt.green) # green
            qp.setBrush(color)
        elif r < 0.6:
            qp.setBrush(QtCore.Qt.yellow) # yellow
        elif r < 0.7:
            color.setNamedColor('#E9C2A6') # orange
            qp.setBrush(color)
        elif r < 0.9:
            color.setNamedColor('#FF5333') # light red
            qp.setBrush(color)
        else:
            qp.setBrush(QtCore.Qt.red)



def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Bundle()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
