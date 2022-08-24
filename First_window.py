from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel
from PyQt5 import uic
from Hist_window import BatMan
from Pie_window import SuperMan
from Bar_window import IronMan
from Barh_window import BlackPanter
from Scatter_window import Deadpool
from Line_window import SheHulk
from Subplot_window import CaptainAmerica
from Area_Window import Witcher

class SpiderMan(QMainWindow):
    def __init__(self):
        super(SpiderMan, self).__init__()

        uic.loadUi("first.ui", self)

        # define content:
        self.line_button = self.findChild(QPushButton, "line_button")
        self.subplot_button = self.findChild(QPushButton, "subplot_button")
        self.scatter_button = self.findChild(QPushButton, "scatter_button")
        self.bar_button = self.findChild(QPushButton, "bar_button")
        self.barh_button = self.findChild(QPushButton, "barh_button")
        self.hist_button = self.findChild(QPushButton, "hist_button")
        self.pie_button = self.findChild(QPushButton, "pie_button")
        self.area_button = self.findChild(QPushButton, "area_button")
        self.exit_button = self.findChild(QPushButton, "exit_button")
        self.welcome_label = self.findChild(QLabel, "welcome_label")

        # call defined methods from here:
        self.exit_button.clicked.connect(lambda: self.close())
        self.pie_button.clicked.connect(self.GoToPie)
        self.hist_button.clicked.connect(self.GoToHistogram)
        self.bar_button.clicked.connect(self.GoToBar)
        self.barh_button.clicked.connect(self.GoToBarh)
        self.scatter_button.clicked.connect(self.GoToScatter)
        self.line_button.clicked.connect(self.GoToLine)
        self.subplot_button.clicked.connect(self.GoToSubPlot)
        self.area_button.clicked.connect(self.GoToArea)


        self.show()

# ----------------------------------------- start ------------------------------------- #
    def GoToPie(self):
        self.window_pie = QMainWindow()
        self.human = SuperMan()
        self.close()
    
    def GoToHistogram(self):
        self.window_hist = QMainWindow()
        self.bat = BatMan()
        self.close()
    
    def GoToBar(self):
        self.window_bar = QMainWindow()
        self.iron = IronMan()
        self.close()
    
    def GoToBarh(self):
        self.window_barh = QMainWindow()
        self.panter = BlackPanter()
        self.close()
    
    def GoToScatter(self):
        self.window_scatter = QMainWindow()
        self.pool = Deadpool()
        self.close()
    
    def GoToLine(self):
        self.window_line = QMainWindow()
        self.hulk = SheHulk()
        self.close()
    
    def GoToSubPlot(self):
        self.window_sub = QMainWindow()
        self.captain = CaptainAmerica()
        self.close()
    
    def GoToArea(self):
        self.window_area = QMainWindow()
        self.gerald = Witcher()
        self.close()
# ------------------------------------------ end -------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    spider = SpiderMan()
    sys.exit(app.exec_())