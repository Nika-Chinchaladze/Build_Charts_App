from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QFrame, QComboBox, QHBoxLayout
from PyQt5.QtGui import QIntValidator
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
from PyQt5 import uic

class CaptainAmerica(QMainWindow):
    def __init__(self):
        super(CaptainAmerica, self).__init__()

        uic.loadUi("sub_plot.ui", self)

        # define content:
        self.sub_label = self.findChild(QLabel, "sub_label")
        self.st_label = self.findChild(QLabel, "st_label")
        self.first_label = self.findChild(QLabel, "first_label")
        self.second_label = self.findChild(QLabel, "second_label")
        self.third_label = self.findChild(QLabel, "third_label")
        self.fourth_label = self.findChild(QLabel, "fourth_label")
        self.fifth_label = self.findChild(QLabel, "fifth_label")
        self.sixth_label = self.findChild(QLabel, "sixth_label")
        self.q_label = self.findChild(QLabel, "q_label")
        self.color_label = self.findChild(QLabel, "color_label")
        self.marker_label_1 = self.findChild(QLabel, "marker_label_1")
        self.marker_label_2 = self.findChild(QLabel, "marker_label_2")
        self.marker_label_3 = self.findChild(QLabel, "marker_label_3")
        self.marker_label_4 = self.findChild(QLabel, "marker_label_4")
        self.dq_label = self.findChild(QLabel, "dq_label")

        self.st_line = self.findChild(QLineEdit, "st_line")
        self.first_line = self.findChild(QLineEdit, "first_line")
        self.second_line = self.findChild(QLineEdit, "second_line")
        self.third_line = self.findChild(QLineEdit, "third_line")
        self.fourth_line = self.findChild(QLineEdit, "fourth_line")
        self.fifth_line = self.findChild(QLineEdit, "fifth_line")
        self.sixth_line = self.findChild(QLineEdit, "sixth_line")
        self.q_line = self.findChild(QLineEdit, "q_line")

        self.color_box = self.findChild(QComboBox, "color_box")
        self.marker_box_1 = self.findChild(QComboBox, "marker_box_1")
        self.marker_box_2 = self.findChild(QComboBox, "marker_box_2")
        self.marker_box_3 = self.findChild(QComboBox, "marker_box_3")
        self.marker_box_4 = self.findChild(QComboBox, "marker_box_4")
        self.dq_box = self.findChild(QComboBox, "dq_box")

        self.display_button = self.findChild(QPushButton, "display_button")
        self.back_button = self.findChild(QPushButton, "back_button")

        self.down_f = self.findChild(QFrame, "down_f")
        self.up_f = self.findChild(QFrame, "up_f")

        # Only Int: --------------------------------------
        Only_Int = QIntValidator()
        self.first_line.setValidator(Only_Int)
        self.second_line.setValidator(Only_Int)
        self.third_line.setValidator(Only_Int)
        self.fourth_line.setValidator(Only_Int)
        self.fifth_line.setValidator(Only_Int)
        self.sixth_line.setValidator(Only_Int)
        self.q_line.setValidator(Only_Int)
        
        # define diagramm: -------------------------------
        self.sub_plot = QHBoxLayout(self.up_f)
        self.sub_plot.setObjectName("sub_plot")
        self.figure = plt.figure()
        self.diagramm = FigureCanvas(self.figure)
        self.sub_plot.addWidget(self.diagramm)

        # call defined methods from here:
        self.back_button.clicked.connect(self.GoBackToFirst)
        self.display_button.clicked.connect(self.Draw_Subplot)



        self.show()

# ----------------------------------- start -------------------------------- #
    # define method for back button:
    def GoBackToFirst(self):
        from First_window import SpiderMan
        self.window1 = QMainWindow()
        self.spider = SpiderMan()
        self.close()

    # define method for display button:
    def Draw_Subplot(self):
        self.figure.clear()
        cont_text = self.dq_box.currentText()
        sup_title = self.st_line.text()
        #---------------------------------------#
        color_type = self.color_box.currentText()
        mark_type = self.marker_box_1.currentText()
        mark_size = int(self.marker_box_2.currentText())
        mark_out = self.marker_box_3.currentText()
        mark_in = self.marker_box_4.currentText()
        #---------------------------------------#
        first_num = self.first_line.text()
        second_num = self.second_line.text()
        third_num = self.third_line.text()
        fourth_num = self.fourth_line.text()
        fifth_num = self.fifth_line.text()
        sixth_num = self.sixth_line.text()
        q_num = self.q_line.text()
        if len(first_num) > 0 and len(second_num) > 0 and len(third_num) > 0 and len(fourth_num) > 0 and len(fifth_num) > 0 and len(sixth_num) > 0 and len(q_num) > 0:
            first_num = int(first_num)
            second_num = int(second_num)
            third_num = int(third_num)
            fourth_num = int(fourth_num)
            fifth_num = int(fifth_num)
            sixth_num = int(sixth_num)
            q_num = int(q_num)
            # create arrays:
            first_array_1 = np.random.randint(first_num, size = (q_num))
            first_array_2 = 10 * np.random.randint(first_num, size = (q_num))
            second_array_1 = np.random.randint(second_num, size = (q_num))
            second_array_2 = 10 * np.random.randint(second_num, size = (q_num))
            third_array_1 = np.random.randint(third_num, size = (q_num))
            third_array_2 = 10 * np.random.randint(third_num, size = (q_num))
            fourth_array_1 = np.random.randint(fourth_num, size = (q_num))
            fourth_array_2 = 10 * np.random.randint(fourth_num, size = (q_num))
            fifth_array_1 = np.random.randint(fifth_num, size = (q_num))
            fifth_array_2 = 10 * np.random.randint(fifth_num, size = (q_num))
            sixth_array_1 = np.random.randint(sixth_num, size = (q_num))
            sixth_array_2 = 10 * np.random.randint(sixth_num, size = (q_num))
            # draw diagrams:
            if cont_text == "1:2":
                plt.subplot(1,2,1)
                plt.plot(first_array_1, first_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(1,2,2)
                plt.plot(second_array_1, second_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.suptitle(f"{sup_title}")
                self.diagramm.draw()
            
            elif cont_text == "2:1":
                plt.subplot(2,1,1)
                plt.plot(first_array_1, first_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,1,2)
                plt.plot(second_array_1, second_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.suptitle(f"{sup_title}")
                self.diagramm.draw()
            
            elif cont_text == "2:2":
                # draw:
                plt.subplot(2,2,1)
                plt.plot(first_array_1, first_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,2,2)
                plt.plot(second_array_1, second_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,2,3)
                plt.plot(third_array_1, third_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,2,4)
                plt.plot(fourth_array_1, fourth_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.suptitle(f"{sup_title}")
                self.diagramm.draw()
            
            elif cont_text == "2:3":
                plt.subplot(2,3,1)
                plt.plot(first_array_1, first_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,3,2)
                plt.plot(second_array_1, second_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,3,3)
                plt.plot(third_array_1, third_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,3,4)
                plt.plot(fourth_array_1, fourth_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,3,5)
                plt.plot(fifth_array_1, fifth_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.subplot(2,3,6)
                plt.plot(sixth_array_1, sixth_array_2, color = f"{color_type}", marker = f"{mark_type}", ms = mark_size, mec = f"{mark_out}", mfc = f"{mark_in}")
                plt.suptitle(f"{sup_title}")
                self.diagramm.draw()
        else:
            None

# ------------------------------------ end -------------------------------- #


if __name__ == "__main__":
    import sys
    app  = QApplication(sys.argv)
    captain = CaptainAmerica()
    sys.exit(app.exec_())