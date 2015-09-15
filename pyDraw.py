#!/usr/bin/python


import sys, random
from PyQt4 import QtGui, QtCore

class Bundle(QtGui.QWidget):
    
   
    def __init__(self):
        super(Bundle, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        #self.setGeometry(0, 0, 100, 100)
        #self.setWindowTitle('Bundle')
        self.show()


    def mousePressEvent(self, mouse_evt):
        
        #super(Bundle, self).mousePressEvent(event)

        button = mouse_evt.button()
        #item = self.itemAt(event.x(), event.y())

        if button == 1:
            print 'SIMPLE LEFT CLICK!'
            print mouse_evt.x(), mouse_evt.y()
            self.drawsquare(mouse_evt.x(),mouse_evt.y())
        if button == 2:
            print 'SIMPLE RIGHT CLICK!'
            print mouse_evt.x(), mouse_evt.y()


    def drawsquare(self,x,y):
        print x,y
        return x,y

    def paintEvent(self, event):

        global s
        s = min(self.size().height(),self.size().width())  
        
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
        x1 = s*0.999

        #s = self.size()
        #x1 = s.height()*0.999
        #x2 = s.height()*0.999
        qp.drawRect(0,0,x1,x1)
        #qp.drawRect(0,0,600,600)

    def drawCRD(self, qp):
        # Paint crd
        pen = QtGui.QPen(QtCore.Qt.black, 8, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        x1 = s*0.025
        x2 = s*0.92
        #s = self.size()
        #x1 = s.height()*0.025
        #x2 = s.height()*0.92
        qp.drawLine(x1, x1, x2, x1)
        qp.drawLine(x1, x1, x1, x2)
        
        #qp.drawLine(20, 20, 555, 20)
        #qp.drawLine(20, 20, 20, 555) 

    def drawBox(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        x1 = s*0.05
        x2 = s*0.92
        
        #s = self.size()
        #x1 = s.height()*0.05
        #x2 = s.height()*0.92
        
        qp.drawRect(x1, x1, x2, x2)

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

        d = s*0.21 # Box size
        x1 = s*0.5
        x2 = s*0.35

        #s = self.size()
        #d = s.height()*0.21 # Box size
        
        #x1 = s.height()*0.5
        #x2 = s.height()*0.35
        qp.translate(x1, x2)
        qp.rotate(45)
        qp.drawRect(0,0,d,d)

    def paintCorners(self, qp):
        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue

        x1 = s*0.4997
        d = s*0.044
        x2 = s*0.36
        x3 = s*0.64

        #s = self.size()
        #x1 = s.height()*0.4997
        #d = s.height()*0.044
        #c = 310
        #d = 28
        pen = QtGui.QPen(color, d, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        #x2 = s.height()*0.36
        #x3 = s.height()*0.64
        qp.drawPoint(x2,x1)
        qp.drawPoint(x3,x1)
        qp.drawPoint(x1,x2)
        qp.drawPoint(x1,x3)


    def drawChannels(self, qp):

        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)

        color = QtGui.QColor(0, 0, 0)
        color.setNamedColor('#BFEFFF') # light blue
        qp.setBrush(color)

        #d = 30
        #c = 310
        
        c = s*0.5
        d = s*0.05

        x1 = s*0.05
        x2 = s*0.92

        #s = self.size()

        #c = s.height()*0.5
        #d = s.height()*0.05

        #x1 = s.height()*0.05
        #x2 = s.height()*0.92
        qp.drawRect(x1,c-d/2,x2,d)
        qp.drawRect(c-d/2,x1,d,x2)

        #qp.drawRect(40,c-d/2,540,d)
        #qp.drawRect(c-d/2,40,d,540)

    def drawCircles(self, qp):
   
        pen = QtGui.QPen(QtCore.Qt.black, 1, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        
        r = s*0.06
        d = s*0.082
        x0 = s*0.07
        x1 = s*0.08


        #s = self.size()

        #r = s.height()*0.06

        #color = QtGui.QColor(0, 0, 0)
        
        #x0 = s.height()*0.07
        #x1 = s.height()*0.08
        # Quad 1
        for i in range(0,5):
            for j in range(0,5):
                if (i,j) == (4,4):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(x0+i*x1,x0+j*x1,r,r)

        #d = self.height()*0.082
        # Quad 2
        for i in range(5,10):
            for j in range(0,5):
                if (i,j) == (5,4):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(d+x0+i*x1,x0+j*x1,r,r)
        
        # Quad 3
        for i in range(0,5):
            for j in range(5,10):
                if (i,j) == (4,5):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(x0+i*x1,d+x0+j*x1,r,r)
        
        # Quad 4
        for i in range(5,10):
            for j in range(5,10):
                if (i,j) == (5,5):
                    continue
                else:
                    self.setColor(qp)
                    qp.drawEllipse(d+x0+i*x1,d+x0+j*x1,r,r)
        


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
