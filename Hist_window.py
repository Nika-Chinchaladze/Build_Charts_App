from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class BatMan(QMainWindow):
    def __init__(self):
        super(BatMan, self).__init__()

        uic.loadUi("histogram.ui", self)

        # define content:
        self.hist_label = self.findChild(QLabel, "hist_label")
        self.choose_label = self.findChild(QLabel, "choose_label")
        self.quantity_label = self.findChild(QLabel, "quantity_label")
        self.central_label = self.findChild(QLabel, "central_label")
        self.deviation_label = self.findChild(QLabel, "deviation_label")
        self.number_label = self.findChild(QLabel, "number_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")
        self.color_label = self.findChild(QLabel, "color_label")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.quantity_line = self.findChild(QLineEdit, "quantity_line")
        self.central_line = self.findChild(QLineEdit, "central_line")
        self.deviation_line = self.findChild(QLineEdit, "deviation_line")
        self.number_line = self.findChild(QLineEdit, "number_line")
        self.title_line = self.findChild(QLineEdit, "title_line")
        self.x_line = self.findChild(QLineEdit, "x_line")
        self.y_line = self.findChild(QLineEdit, "y_line")

        # define only ints:- -------------------------------------- #
        Only_Int = QIntValidator()
        self.quantity_line.setValidator(Only_Int)
        self.central_line.setValidator(Only_Int)
        self.deviation_line.setValidator(Only_Int)
        # ---------------------------------------------------------- #

        self.fr_down = self.findChild(QFrame, "fr_down")
        self.fr_up = self.findChild(QFrame, "fr_up")

        self.choose_box = self.findChild(QComboBox, "choose_box")
        self.color_box = self.findChild(QComboBox, "color_box")

        # define diagram:
        self.chart_layout = QHBoxLayout(self.fr_up)
        self.chart_layout.setObjectName("chart_layout")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.chart_layout.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.ReturnToFirst)
        self.display_button.clicked.connect(self.Draw_Histogram)


        self.show()

# ----------------------------------------- start ------------------------------------- #
    # define method for back button:
    def ReturnToFirst(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define methof for display button:
    def Draw_Histogram(self):
        self.figure.clear()
        # variables:
        build_type = self.choose_box.currentText()
        hist_title = self.title_line.text()
        x_name = self.x_line.text()
        y_name = self.y_line.text()
        color_type = self.color_box.currentText()

        if build_type == "with random elements":
            if len(self.quantity_line.text()) > 0 and len(self.central_line.text()) > 0 and len(self.deviation_line.text()) > 0:
                quantity = int(self.quantity_line.text())
                cent_number = int(self.central_line.text())
                stand_dev = int(self.deviation_line.text())
                defined_values = np.random.normal(cent_number, stand_dev, quantity)

                plt.hist(defined_values, color = color_type)
                plt.title(f"{hist_title}")
                plt.xlabel(f"{x_name}")
                plt.ylabel(f"{y_name}")
                self.diagramm.draw()
            else:
                None

        elif build_type == "with entered elements":
            entered_string = self.number_line.text()
            List = entered_string.split(" ")
            if len(entered_string) > 0:
                try:
                    number_list = [int(item) for item in List]
                    number_array = np.array(number_list)
                    
                    plt.hist(number_array, color = color_type)
                    plt.title(f"{hist_title}")
                    plt.xlabel(f"{x_name}")
                    plt.ylabel(f"{y_name}")
                    self.diagramm.draw()
                except ValueError:
                    self.number_line.setText("Delete this and enter only Numbers!")
            else:
                None


# ------------------------------------------ end -------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    bat = BatMan()
    sys.exit(app.exec_())