from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class SuperMan(QMainWindow):
    def __init__(self):
        super(SuperMan, self).__init__()

        uic.loadUi("pie.ui", self)

        # define content:
        self.pie_label = self.findChild(QLabel, "pie_label")
        self.chart_title = self.findChild(QLabel, "chart_title")
        self.legend_title = self.findChild(QLabel, "legend_title")
        self.angle_label = self.findChild(QLabel, "angle_label")
        self.explode_label = self.findChild(QLabel, "explode_label")
        self.shadow_label = self.findChild(QLabel, "shadow_label")
        self.array_label = self.findChild(QLabel, "array_label")
        self.label_label = self.findChild(QLabel, "label_label")
        self.info_label = self.findChild(QLabel, "info_label")

        self.chart_line = self.findChild(QLineEdit, "chart_line")
        self.legend_line = self.findChild(QLineEdit, "legend_line")
        self.label_line = self.findChild(QLineEdit, "label_line")
        self.array_line = self.findChild(QLineEdit, "array_line")
        
        # define only ints:- -------------------------------------- #
        self.order_line = self.findChild(QLineEdit, "order_line")
        Only_Int = QIntValidator()
        self.order_line.setValidator(Only_Int)

        # ---------------------------------------------------------- #

        self.angle_box = self.findChild(QComboBox, "angle_box")
        self.size_box = self.findChild(QComboBox, "size_box")
        self.shadow_box = self.findChild(QComboBox, "shadow_box")

        self.down_frame = self.findChild(QFrame, "down_frame")
        self.up_frame = self.findChild(QFrame, "up_frame")

        self.back_button = self.findChild(QPushButton, "back_button")
        self.display_button = self.findChild(QPushButton, "display_button")

        # define diagramm layout:
        self.Background_Layout = QHBoxLayout(self.up_frame)
        self.Background_Layout.setObjectName("Background_Layout")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.Background_Layout.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.Go_Back)
        self.display_button.clicked.connect(self.Show_Diagramm)

        self.show()

# ----------------------------------------- start ------------------------------------- #
    # define background color:
    def Red_Color(self):
        self.info_label.setStyleSheet("background-color: rgb(255, 80, 83);")
    
    def White_Color(self):
        self.info_label.setStyleSheet("background-color: rgb(240, 240, 240);")

    # define method for back button:
    def Go_Back(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define method for display button:
    def Show_Diagramm(self):
        self.figure.clear()
        # basic values:
        entered_numbers = self.array_line.text()
        entered_labels = self.label_line.text()
        x_values = entered_numbers.split(" ")
        try:
            x_values = [int(item) for item in x_values]
            my_labels = entered_labels.split(" ")
            
            if len(x_values) == len(my_labels):
                # design values:
                shadow_format = self.shadow_box.currentText()
                angle = int(self.angle_box.currentText())
                chart_title = self.chart_line.text()
                legend_title = self.legend_line.text()
                # define explode:
                if self.order_line.text() != "":
                    pass
                elif self.order_line.text() == "":
                    self.order_line.setText(f"{1}")

                sz = float(self.size_box.currentText())

                wanted_item = int(self.order_line.text())
                if wanted_item == 0:
                    wanted_item = 1
                else:
                    wanted_item = wanted_item - 1

                my_explode = []
                for i in my_labels:
                    my_explode.append(0)
                
                if wanted_item < len(my_labels):
                    my_explode[wanted_item] = sz
                else:
                    my_explode[0] = sz
                    self.info_label.setText("Defined Number was too hign, so App replaced it with 1")
                    self.Red_Color()
                    self.order_line.setText("1")
                
                # draw pie chart
                if shadow_format == 'Yes':
                    plt.pie(x_values, labels = my_labels, startangle = angle, explode = my_explode, shadow = True)
                elif shadow_format == 'No':
                    plt.pie(x_values, labels = my_labels, startangle = angle, explode = my_explode, shadow = False)
                
                plt.title(f"{chart_title}")
                plt.legend(title = f"{legend_title}")
                self.diagramm.draw()
                self.info_label.setText("")
                self.White_Color()
            else:
                self.info_label.setText("The Quantity of items in Number and Label boxes must be EQUAL!")
                self.Red_Color()
        except ValueError:
            self.info_label.setText("All item in the Number's Box must be Integer!")
            self.Red_Color()


# ------------------------------------------ end -------------------------------------- #

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    human = SuperMan()
    sys.exit(app.exec_())