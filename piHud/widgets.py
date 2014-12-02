from PyQt4 import QtCore, QtGui, QtSvg
import obd
import pygal
from pygal.style import Style
from SVGWidget import SVGWidget

class Gauge(SVGWidget):
    def __init__(self, parent, command):
        super(Gauge, self).__init__(parent)
        super(Gauge, self).setFixedWidth(350)
        super(Gauge, self).setFixedHeight(400)

        self.command = command
        self.style = Style(
            background='black',
            plot_background='transparent',
            foreground='#53B9E8',
            foreground_light='#53A0E8',
            foreground_dark='transparent',
            colors=('#53B9E8', '#53B9E8'))

    def get_command(self):
        return self.command

    def render(self, value):
        gauge_chart = pygal.Gauge(human_readable=True, width=200, height=250, style=self.style)
        
        gauge_chart.show_legend = False
        gauge_chart.title = self.command.name
        gauge_chart.range = [0, 8000]

        gauge_chart.add(self.command.name, value)
        chart = QtCore.QByteArray(gauge_chart.render())
        super(Gauge, self).load(chart)
