from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont
import sys


class BMI:

    def __init__(self, weight, height):
        self.weight = weight
        self.height = height
        self.BMI = None

    def calculate(self):
        self.BMI = self.weight/self.height**2

        return self.BMI


class AppBMI(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.result = QLabel(self)
        main_font = QFont()
        main_font.setPointSize(20)
        self.result.setGeometry(10, 20, 400, 35)
        self.result.setText("Your BMI is ....")
        self.result.setFont(main_font)

        height_to_BMI = QLabel(self)
        font = QFont()
        font.setPointSize(10)
        height_to_BMI.setGeometry(10, 60, 400, 20)
        height_to_BMI.setText("Give a height:")
        height_to_BMI.setFont(font)

        self.setGeometry(500, 500, 500, 400)
        self.setWindowTitle("Calculator BMI")

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AppBMI()
    sys.exit(app.exec_())