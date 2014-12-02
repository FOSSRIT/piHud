
import obd
import math
from widgets import *
from PyQt4 import QtCore, QtGui


class MainScreen(QtGui.QWidget):

    def __init__(self, parent, connection):
        super(MainScreen, self).__init__(parent)
        self.draggables = []
        self.initUI()

        self.connection = connection

        self.timer = QtCore.QBasicTimer()
        self.timer.start(1000/30, self)

        self.makeChart(obd.commands.RPM)
        self.makeChart(obd.commands.COOLANT_TEMP)
        self.theta = 0;


    def initUI(self):
        self.setAcceptDrops(True)

    def makeChart(self, command):
        self.connection.watch(command)
        self.draggables.append(Gauge(self, command))

    def timerEvent(self, event):
        """ main event loop """
        #for w in self.draggables:
            
        self.draggables[0].render((math.sin(self.theta) * 4000) + 4000)
        self.draggables[1].render((math.cos(self.theta) * 4000) + 4000)
        
        self.theta += 0.01


    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        e.source().move(position)

        e.setDropAction(QtCore.Qt.MoveAction)
        e.accept()
