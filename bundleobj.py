#!/usr/bin/python

import sys
from PyQt4 import QtGui

from pyDraw import Bundle

app = QtGui.QApplication(sys.argv)

bundleObj = Bundle()

sys.exit(app.exec_())

