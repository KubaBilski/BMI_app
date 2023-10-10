from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QSpinBox
from PyQt5.QtGui import QFont
import sys


class AppBMI(QWidget):

    def __init__(self):
        super().__init__()
        self.BMI = None
        self.height_insert = QSpinBox(self)
        self.weight_insert = QSpinBox(self)
        self.result = QLabel(self)
        self.initUI()

    def initUI(self):
        main_font = QFont()
        main_font.setPointSize(20)
        self.result.setGeometry(10, 20, 400, 35)
        self.result.setText("Your BMI is ....")
        self.result.setFont(main_font)

        height_to_BMI = QLabel(self)
        font = QFont()
        font.setPointSize(10)
        height_to_BMI.setGeometry(10, 80, 400, 20)
        height_to_BMI.setText("Give a height [cm]:")
        height_to_BMI.setFont(font)
        self.height_insert.setMinimum(1)
        self.height_insert.setMaximum(9999)
        self.height_insert.setGeometry(10, 105, 80, 30)

        weight_to_BMI = QLabel(self)
        weight_to_BMI.setGeometry(10, 140, 400, 20)
        weight_to_BMI.setText("Give a weight [kg]:")
        weight_to_BMI.setFont(font)
        self.weight_insert.setMinimum(1)
        self.weight_insert.setMaximum(9999)
        self.weight_insert.setGeometry(10, 165, 80, 30)

        button_calc = QPushButton("Calculate BMI", self)
        button_calc.setGeometry(135, 220, 180, 80)
        font_for_button = QFont()
        font_for_button.setPointSize(15)
        button_calc.setFont(font_for_button)

        self.setGeometry(500, 500, 450, 320)
        self.setWindowTitle("Calculator BMI")

        self.show()

        button_calc.clicked.connect(self.calc_BMI)

    def calc_BMI(self):
        height_val = self.height_insert.value()
        weight_val = self.weight_insert.value()

        height_val_cm = height_val*0.01
        self.BMI = weight_val/(height_val_cm**2)

        self.update_BMI()

    def update_BMI(self):
        self.result.setText("Your BMI is {0}".format(self.BMI))
        self.weight_insert.setValue(1)
        self.height_insert.setValue(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppBMI()
    sys.exit(app.exec_())
