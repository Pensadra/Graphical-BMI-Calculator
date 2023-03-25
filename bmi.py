import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QApplication, QWidget, QMessageBox, QPushButton, QVBoxLayout
from PyQt5.QtCore import QSize, Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BMI Calculator")

        self.label_1 = QLabel("Enter your weight: ")
        w = self.weight_input = QLineEdit("kg")
        w.setFixedWidth(100)

        self.label_2 = QLabel("Enter your height: ")
        h = self.height_input = QLineEdit("m")
        h.setFixedWidth(100)

        button = QPushButton("calculate")
        button.clicked.connect(self.click)

        layout = QVBoxLayout()
        layout.addWidget(self.label_1)
        layout.addWidget(self.weight_input)
        layout.addWidget(self.label_2)
        layout.addWidget(self.height_input)
        layout.addWidget(button)

        con = QWidget()
        con.setLayout(layout)

        self.setFixedSize(QSize(250, 200))
        self.setCentralWidget(con)

    def click(self):
        v = float(self.weight_input.text())
        q = float(self.height_input.text())

        done = int(v / (q ** 2))

        if done < 18.5:
            o = QMessageBox(self)
            o.setWindowTitle("your BMI")
            o.setText(f"""Indicator: {done} kg/m^2
            You are underweight""")
            o.exec()

        elif 18.5 <= done < 25:
            o = QMessageBox(self)
            o.setWindowTitle("your BMI")
            o.setText(f"""Indicator: {done} kg/m^2
            Your weight is ideal""")
            o.exec()

        elif 25 <= done < 30:
            o: QMessageBox | QMessageBox = QMessageBox(self)
            o.setWindowTitle("your BMI")
            o.setText(f"""Indicator: {done} kg/m^2
            You are overweight""")
            o.exec()

