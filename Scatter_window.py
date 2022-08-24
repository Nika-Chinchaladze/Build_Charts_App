from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class Deadpool(QMainWindow):
    def __init__(self):
        super(Deadpool, self).__init__()

        uic.loadUi("scatter_plot.ui", self)

        # define content:
        self.scatter_label = self.findChild(QLabel, "scatter_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")
        self.first_label = self.findChild(QLabel, "first_label")
        self.second_label = self.findChild(QLabel, "second_label")
        self.quantity_label = self.findChild(QLabel, "quantity_label")
        self.color_label = self.findChild(QLabel, "color_label")
        self.size_label = self.findChild(QLabel, "size_label")

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

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.color_box = self.findChild(QComboBox, "color_box")
        self.size_box = self.findChild(QComboBox, "size_box")

        # define diagramm:
        self.scatter_chart = QHBoxLayout(self.fr_up)
        self.scatter_chart.setObjectName("scatter_chart")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.scatter_chart.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.Come_Back)
        self.display_button.clicked.connect(self.Draw_scatter)


        self.show()

# ------------------------------------ start ------------------------------ #
    # define method for back button:
    def Come_Back(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define method for display button:
    def Draw_scatter(self):
        self.figure.clear()
        chart_title = self.t_line.text()
        x_name = self.x_line.text()
        y_name = self.y_line.text()
        map_type = self.color_box.currentText()
        size_type = int(self.size_box.currentText())
        if len(self.f_line.text()) > 0 and len(self.s_line.text()) and len(self.q_line.text()) > 0:
            f_num = int(self.f_line.text())
            s_num = int(self.s_line.text())
            q_num = int(self.q_line.text())
            first_array = np.random.randint(f_num, size = (q_num))
            second_array = np.random.randint(s_num, size = (q_num))
            
            if f_num > s_num:
                colors = np.random.randint(f_num, size = (q_num))
                sizes = size_type * np.random.randint(f_num, size = (q_num))
            else:
                colors = np.random.randint(s_num, size = (q_num))
                sizes = size_type * np.random.randint(s_num, size = (q_num))

            plt.scatter(first_array, second_array, c = colors, s = sizes, alpha = 0.5, cmap = f"{map_type}")
            plt.title(f"{chart_title}")
            plt.xlabel(f"{x_name}")
            plt.ylabel(f"{y_name}")
            plt.colorbar()
            self.diagramm.draw()
        else:
            None

# ------------------------------------ end -------------------------------- #


if __name__ == "__main__":
    import sys
    app  = QApplication(sys.argv)
    pool = Deadpool()
    sys.exit(app.exec_())