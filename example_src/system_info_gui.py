"""
이 코드는 PyQT5 모듈을 사용하여 CPU, 메모리 및 디스크 사용량을 표시하는 간단한 GUI 프로그램을 만듭니다.
QTimer를 사용하여 1 초마다 업데이트합니다. QLabel을 사용하여 CPU, 메모리 및 디스크 사용량을 표시합니다.
모든 사용자 정의 위젯은 QVBoxLayout 내부에 배치되며, 이는 전체 위젯의 레이아웃으로 설정됩니다.
마지막으로, QApplication 클래스를 사용하여 프로그램을 실행합니다.
"""
import sys
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('System Monitor')
        self.setGeometry(300, 300, 400, 200)

        self.cpu_label = QLabel(self)
        self.mem_label = QLabel(self)
        self.disk_label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addWidget(self.cpu_label)
        vbox.addWidget(self.mem_label)
        vbox.addWidget(self.disk_label)
        self.setLayout(vbox)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_labels)
        self.timer.start(1000)  # 1초마다 업데이트

    def update_labels(self):
        cpu_percent = psutil.cpu_percent()
        mem_info = psutil.virtual_memory()
        mem_percent = mem_info.percent
        disk_info = psutil.disk_usage('/')
        disk_percent = disk_info.percent

        self.cpu_label.setText(f'CPU 사용률: {cpu_percent}%')
        self.mem_label.setText(f'메모리 사용률: {mem_percent}%')
        self.disk_label.setText(f'디스크 사용률: {disk_percent}%')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
