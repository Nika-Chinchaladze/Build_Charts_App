from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class BlackPanter(QMainWindow):
    def __init__(self):
        super(BlackPanter, self).__init__()

        uic.loadUi("barh_chart.ui", self)

        # define content:
        self.bar_label = self.findChild(QLabel, "bar_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.x_label = self.findChild(QLabel, "x_label")
        self.y_label = self.findChild(QLabel, "y_label")
        self.h_label = self.findChild(QLabel, "h_label")
        self.color_label = self.findChild(QLabel, "color_label")
        self.number_label = self.findChild(QLabel, "number_label")
        self.my_label = self.findChild(QLabel, "my_label")
        self.ans_label = self.findChild(QLabel, "ans_label")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.title_line = self.findChild(QLineEdit, "title_line")
        self.x_line = self.findChild(QLineEdit, "x_line")
        self.y_line = self.findChild(QLineEdit, "y_line")
        self.number_line = self.findChild(QLineEdit, "number_line")
        self.my_line = self.findChild(QLineEdit, "my_line")

        self.h_box = self.findChild(QComboBox, "h_box")
        self.color_box = self.findChild(QComboBox, "color_box")

        self.down_fr = self.findChild(QFrame, "down_fr")
        self.up_fr = self.findChild(QFrame, "up_fr")

        # define diagram:
        self.bar_chart = QHBoxLayout(self.up_fr)
        self.bar_chart.setObjectName("bar_chart")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.bar_chart.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.Return_Back)
        self.display_button.clicked.connect(self.Draw_Barh)

        self.show()

# ----------------------------------- start ------------------------------- #
    # define background color:
    def Red_Color(self):
        self.ans_label.setStyleSheet("background-color: rgb(255, 80, 83);")
    
    def White_Color(self):
        self.ans_label.setStyleSheet("background-color: rgb(240, 240, 240);")

    # define method for back button:
    def Return_Back(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define method for display button:
    def Draw_Barh(self):
        self.figure.clear()
        barh_title = self.title_line.text()
        x_name = self.x_line.text()
        y_name = self.y_line.text()
        color_type = self.color_box.currentText()
        bar_height = float(self.h_box.currentText())
        # ----------------------------- #
        Ent_lab = self.my_line.text()
        Ent_lab = Ent_lab.split(" ")
        Ent_nums = self.number_line.text()
        Ent_nums = Ent_nums.split(" ")
        try:
            Ent_list = [int(item) for item in Ent_nums]
            # ----------------------------- #
            number_array = np.array(Ent_list)
            label_array = np.array(Ent_lab)
            if len(number_array) == len(label_array):
                plt.barh(label_array, number_array, color = f"{color_type}", height = bar_height)
                plt.title(f"{barh_title}")
                plt.xlabel(f"{y_name}")
                plt.ylabel(f"{x_name}")
                self.diagramm.draw()
                self.ans_label.setText("")
                self.White_Color()
            else:
                self.ans_label.setText("Quantity of values in Number and Label must be Equal!")
                self.Red_Color()
        except ValueError:
            self.ans_label.setText("Enter Only Numbers!")
            self.Red_Color()

# ------------------------------------ end -------------------------------- #

if __name__ == "__main__":
    import sys
    app  = QApplication(sys.argv)
    panter = BlackPanter()
    sys.exit(app.exec_())
