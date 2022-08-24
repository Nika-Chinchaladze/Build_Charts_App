from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import pandas as pd
from PyQt5 import uic

class Witcher(QMainWindow):
    def __init__(self):
        super(Witcher, self).__init__()

        uic.loadUi("area_plot.ui", self)

        # define content:
        self.area_label = self.findChild(QLabel, "area_label")
        self.title_label = self.findChild(QLabel, "title_label")
        self.first_label = self.findChild(QLabel, "first_label")
        self.second_label = self.findChild(QLabel, "second_label")
        self.in_label = self.findChild(QLabel, "in_label")
        self.out_label = self.findChild(QLabel, "out_label")
        self.tran_label = self.findChild(QLabel, "tran_label")
        self.q_label = self.findChild(QLabel, "q_label")
        self.grid_label = self.findChild(QLabel, "grid_label")
        self.ord_label_1 = self.findChild(QLabel, "ord_label_1")
        self.ord_label_2 = self.findChild(QLabel, "ord_label_2")
        self.ord_label_3 = self.findChild(QLabel, "ord_label_3")
        self.ord_label_4 = self.findChild(QLabel, "ord_label_4")
        self.column_label = self.findChild(QLabel, "column_label")
        self.value_label = self.findChild(QLabel, "value_label")
        self.choose_label = self.findChild(QLabel, "choose_label")

        self.title_line = self.findChild(QLineEdit, "title_line")
        self.first_line = self.findChild(QLineEdit, "first_line")
        self.second_line = self.findChild(QLineEdit, "second_line")
        self.q_line = self.findChild(QLineEdit, "q_line")

        self.age_line = self.findChild(QLineEdit, "age_line")
        self.weight_line = self.findChild(QLineEdit, "weight_line")
        self.age_values = self.findChild(QLineEdit, "age_values")
        self.kg_values = self.findChild(QLineEdit, "kg_values")

        self.box_1 = self.findChild(QComboBox, "box_1")
        self.box_2 = self.findChild(QComboBox, "box_2")
        self.box_3 = self.findChild(QComboBox, "box_3")
        self.box_4 = self.findChild(QComboBox, "box_4")
        self.choose_box = self.findChild(QComboBox, "choose_box")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.fr_d = self.findChild(QFrame, "fr_d")
        self.fr_u = self.findChild(QFrame, "fr_u")
        self.line_one = self.findChild(QFrame, "line_one")
        self.line_two = self.findChild(QFrame, "line_two")
        self.line_three = self.findChild(QFrame, "line_three")

        # Only Int: --------------------------------------
        Only_Int = QIntValidator()
        self.first_line.setValidator(Only_Int)
        self.second_line.setValidator(Only_Int)
        self.q_line.setValidator(Only_Int)

        # define diagramm: -------------------------------
        self.area_chart = QHBoxLayout(self.fr_u)
        self.area_chart.setObjectName("area_chart")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.area_chart.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.ReturnBackToFirst)
        self.display_button.clicked.connect(self.Draw_area)

        # useful variable:
        self.numb = 1

        self.show()

# ----------------------------------- start ------------------------------- #
    # define method for back button:
    def ReturnBackToFirst(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()
    
    # define method for display button:
    def Draw_area(self):
        self.figure.clear()
        # ---------------------------------- #
        chosen = self.choose_box.currentText()
        in_color = self.box_1.currentText()
        line_color = self.box_2.currentText()
        transp = float(self.box_3.currentText())
        grid_type = self.box_4.currentText()
        area_title = self.title_line.text()

        if chosen == "with numpy array":
            first_num = self.first_line.text()
            second_num = self.second_line.text()
            q_num = self.q_line.text()
            if len(first_num) > 0 and len(second_num) > 0 and len(q_num) > 0:
                first_num = int(first_num)
                second_num = int(second_num)
                q_num = int(q_num)
                first_array = np.random.randint(first_num, size = (q_num))
                second_array = np.random.randint(second_num, size = (q_num))
                # sort: asc or desc [random choise]
                if self.numb % 2 == 1:
                    first_array = np.sort(first_array)
                    second_array = np.sort(second_array)
                elif self.numb % 2 == 0:
                    first_array = np.sort(first_array)
                    second_array = np.sort(second_array)[::-1]
                self.numb += 1
                # draw:
                plt.fill_between(first_array, second_array, color = f"{in_color}", alpha = transp)
                plt.plot(first_array, second_array, color = f"{line_color}")
                plt.title(f"{area_title}")

                if grid_type == "x and y":
                    plt.grid()
                elif grid_type == "x":
                    plt.grid(axis='x')
                elif grid_type == "y":
                    plt.grid(axis='y')

                self.diagramm.draw()
            else:
                None
        elif chosen == "with pandas DataFrame":
            # columns:-------------------- #
            column_1 = self.age_line.text()
            column_2 = self.weight_line.text()
            # ----------------------------- #
            ent_ages = self.age_values.text()
            ent_weight = self.kg_values.text()
            age_row = ent_ages.split(" ")
            weight_row = ent_weight.split(" ")
            # rows: --------------------------------------- #
            if len(column_1) > 0 and len(column_2) > 0 and len(age_row) > 0 and len(weight_row) > 0 and len(age_row) == len(weight_row):
                try:
                    age_row = [float(item) for item in age_row]
                    weight_row = [float(item) for item in weight_row]
                    # DataFrame:
                    df = pd.DataFrame({
                        f"{column_1}" : age_row,
                        f"{column_2}" : weight_row
                    })

                    plt.fill_between(df[f"{column_1}"], df[f"{column_2}"], color = f"{in_color}", alpha = transp)
                    plt.plot(df[f"{column_1}"], df[f"{column_2}"], color = f"{line_color}")
                    plt.title(f"{area_title}")

                    if grid_type == "x and y":
                        plt.grid()
                    elif grid_type == "x":
                        plt.grid(axis='x')
                    elif grid_type == "y":
                        plt.grid(axis='y')

                    self.diagramm.draw()
                except ValueError:
                    None
            else:
                None

# ------------------------------------ end -------------------------------- #

if __name__ == "__main__":
    import sys
    app  = QApplication(sys.argv)
    gerald = Witcher()
    sys.exit(app.exec_())