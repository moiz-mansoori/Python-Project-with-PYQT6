
import sys   #pip install sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout
from PyQt6.QtGui import QFont

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 350, 300)

        grid = QGridLayout()
        self.setLayout(grid)

        self.result_label = QLabel('', self)
        self.result_label.setStyleSheet("QLabel { background-color : grey; color : white; }")
        self.result_label.setFont(QFont('Verdana', 30, QFont.Weight.Bold))
        grid.addWidget(self.result_label, 0, 0, 1, 4)

        buttons = [
            ('7', 1, 0), 
            ('8', 1, 1), 
            ('9', 1, 2), 
            ('+', 1, 3),
            ('4', 2, 0), 
            ('5', 2, 1), 
            ('6', 2, 2), 
            ('-', 2, 3),
            ('1', 3, 0), 
            ('2', 3, 1), 
            ('3', 3, 2), 
            ('*', 3, 3),
            ('Clear', 4, 0), 
            ('0', 4, 1), 
            ('=', 4, 2), 
            ('/', 4, 3)
        ]

        for text, row, col in buttons:
            button = QPushButton(text, self)
            button.setStyleSheet("QPushButton { background-color : black; color : white; }")
            button.setFont(QFont('Verdana', 14))
            button.clicked.connect(lambda state, text=text: self.buttonClicked(text))
            grid.addWidget(button, row, col)

        self.show()

    def buttonClicked(self, text):
        if text.isdigit() or text == 'Clear':
            current = self.result_label.text()
            if text == 'Clear':
                self.result_label.setText('')
            else:
                new = current + text
                self.result_label.setText(new)
        elif text == '=':
            self.get_result()
        else:
            self.get_operator(text)

    def get_operator(self, op):
        self.first_number = int(self.result_label.text())
        self.operator = op
        self.result_label.setText('')

    def get_result(self):
        second_number = int(self.result_label.text())

        if self.operator == '+':
            self.result_label.setText(str(self.first_number + second_number))
        elif self.operator == '-':
            self.result_label.setText(str(self.first_number - second_number))
        elif self.operator == '*':
            self.result_label.setText(str(self.first_number * second_number))
        else:
            if second_number == 0:
                self.result_label.setText('Error')
            else:
                self.result_label.setText(str(round(self.first_number / second_number, 2)))

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
