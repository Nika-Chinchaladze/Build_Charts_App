from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class SheHulk(QMainWindow):
    def __init__(self):
        super(SheHulk, self).__init__()

        uic.loadUi("line_chart.ui", self)

        # define content:
        self.line_label = self.findChild(QLabel, "line_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")
        self.first_label = self.findChild(QLabel, "first_label")
        self.second_label = self.findChild(QLabel, "second_label")
        self.quantity_label = self.findChild(QLabel, "quantity_label")
        self.width_label_1 = self.findChild(QLabel, "width_label_1")
        self.width_label_2 = self.findChild(QLabel, "width_label_2")
        self.style_label_1 = self.findChild(QLabel, "style_label_1")
        self.style_label_2 = self.findChild(QLabel, "style_label_2")
        self.color_label_1 = self.findChild(QLabel, "color_label_1")
        self.color_label_2 = self.findChild(QLabel, "color_label_2")
        self.marker_label_1 = self.findChild(QLabel, "marker_label_1")
        self.marker_label_2 = self.findChild(QLabel, "marker_label_2")
        self.size_label_1 = self.findChild(QLabel, "size_label_1")
        self.size_label_2 = self.findChild(QLabel, "size_label_2")

        self.t_line = self.findChild(QLineEdit, "t_line")
        self.x_line = self.findChild(QLineEdit, "x_line")
        self.y_line = self.findChild(QLineEdit, "y_line")
        self.f_line = self.findChild(QLineEdit, "f_line")
        self.s_line = self.findChild(QLineEdit, "s_line")
        self.q_line = self.findChild(QLineEdit, "q_line")

        # Only Int:--------------------------------------
        Only_Int = QIntValidator()
        self.f_line.setValidator(Only_Int)
        self.s_line.setValidator(Only_Int)
        self.q_line.setValidator(Only_Int)
        #------------------------------------------------

        self.fr_down = self.findChild(QFrame, "fr_down")
        self.fr_up = self.findChild(QFrame, "fr_up")
        self.line_1 = self.findChild(QFrame, "line_1")
        self.line_2 = self.findChild(QFrame, "line_2")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.color_box_1 = self.findChild(QComboBox, "color_box_1")
        self.color_box_2 = self.findChild(QComboBox, "color_box_2")
        self.width_box_1 = self.findChild(QComboBox, "width_box_1")
        self.width_box_2 = self.findChild(QComboBox, "width_box_2")
        self.style_box_1 = self.findChild(QComboBox, "style_box_1")
        self.style_box_2 = self.findChild(QComboBox, "style_box_2")
        self.marker_box_1 = self.findChild(QComboBox, "marker_box_1")
        self.marker_box_2 = self.findChild(QComboBox, "marker_box_2")
        self.size_box_1 = self.findChild(QComboBox, "size_box_1")
        self.size_box_2 = self.findChild(QComboBox, "size_box_2")

        # define diagramm:
        self.line_chart = QHBoxLayout(self.fr_up)
        self.line_chart.setObjectName("line_chart")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.line_chart.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.Return_Back)
        self.display_button.clicked.connect(self.Draw_line)


        self.show()

# ------------------------------------ start ------------------------------ #
    # define method for back button:
    def Return_Back(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define method for display button:
    def Draw_line(self):
        self.figure.clear()
        chart_title = self.t_line.text()
        x_name = self.x_line.text()
        y_name = self.y_line.text()
        first_width = self.width_box_1.currentText()
        second_width = self.width_box_2.currentText()
        first_style = self.style_box_1.currentText()
        second_style = self.style_box_2.currentText()
        first_color = self.color_box_1.currentText()
        second_color = self.color_box_2.currentText()
        first_marker = self.marker_box_1.currentText()
        second_marker = self.marker_box_2.currentText()
        first_size = int(self.size_box_1.currentText())
        second_size = int(self.size_box_2.currentText())
        if len(self.f_line.text()) > 0 and len(self.s_line.text()) and len(self.q_line.text()) > 0:
            f_num = int(self.f_line.text())
            s_num = int(self.s_line.text())
            q_num = int(self.q_line.text())
            first_array = np.random.randint(f_num, size = (q_num))
            second_array = np.random.randint(s_num, size = (q_num))

            plt.plot(first_array, color = f"{first_color}", ls = f"{first_style}", lw = f"{first_width}", marker = f"{first_marker}", ms = first_size)
            plt.plot(second_array, color = f"{second_color}", ls = f"{second_style}", lw = f"{second_width}", marker = f"{second_marker}", ms = second_size)
            plt.title(f"{chart_title}")
            plt.xlabel(f"{x_name}")
            plt.ylabel(f"{y_name}")
            self.diagramm.draw()
        else:
            None

# ------------------------------------ end -------------------------------- #


if __name__ == "__main__":
    import sys
    app  = QApplication(sys.argv)
    hulk = SheHulk()
    sys.exit(app.exec_())