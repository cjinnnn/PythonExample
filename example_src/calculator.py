from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class Calculator(QWidget):

    def __init__(self):
        super().__init__()

        # UI 초기화
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 300)
        self.setFixedSize(300, 300)

        # 레이아웃 초기화
        self.layout = QVBoxLayout()
        self.display_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        # 텍스트 박스 초기화
        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(30)
        self.display.setReadOnly(True)
        self.display.setText('0')
        self.display_layout.addWidget(self.display)

        # 버튼 초기화
        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+', '=']
        ]
        for row in self.buttons:
            row_layout = QHBoxLayout()
            for button in row:
                button_widget = QPushButton(button)
                button_widget.setFixedSize(50, 50)
                button_widget.clicked.connect(self.button_click)
                row_layout.addWidget(button_widget)
            self.button_layout.addLayout(row_layout)

        # 레이아웃 설정
        self.layout.addLayout(self.display_layout)
        self.layout.addLayout(self.button_layout)
        self.setLayout(self.layout)

    def button_click(self):
        button = self.sender()
        text = button.text()
        current = self.display.text()

        # 숫자 버튼 처리
        if text.isdigit() or text == '.':
            if current == '0' and text != '.':
                self.display.setText(text)
            else:
                self.display.setText(current + text)
        # 연산 버튼 처리
        elif text in ['+', '-', '*', '/']:
            self.display.setText(current + text)
        # 리셋 버튼 처리
        elif text == 'C':
            self.display.setText('0')
        # 계산 버튼 처리
        elif text == '=':
            try:
                result = eval(current)
                self.display.setText(str(result))
            except ZeroDivisionError:
                self.display.setText('Error')

if __name__ == '__main__':
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec_()
