"""
이전 코드와의 차이점은 다음과 같습니다.

CPU 코어 수를 나타내는 core_label와 디스크 파티션 정보를 나타내는 partition_label를 추가했습니다.
update_labels() 메서드에서 CPU 코어 수와 디스크 파티션 정보를
"""
import psutil
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
import sys
from PyQt5.QtCore import QTimer

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()

        # GUI 설정
        self.setWindowTitle("System Monitor")
        self.setGeometry(300, 300, 400, 200)
        layout = QGridLayout()
        self.setLayout(layout)

        # CPU 정보 라벨
        cpu_label = QLabel()
        layout.addWidget(QLabel("CPU Usage:"), 0, 0)
        layout.addWidget(cpu_label, 0, 1)

        # CPU 코어 수 라벨
        core_label = QLabel()
        layout.addWidget(QLabel("CPU Cores:"), 1, 0)
        layout.addWidget(core_label, 1, 1)

        # 메모리 정보 라벨
        mem_label = QLabel()
        layout.addWidget(QLabel("Memory Usage:"), 2, 0)
        layout.addWidget(mem_label, 2, 1)

        # 디스크 정보 라벨
        disk_label = QLabel()
        layout.addWidget(QLabel("Disk Usage:"), 3, 0)
        layout.addWidget(disk_label, 3, 1)

        # 디스크 파티션 정보 라벨
        partition_label = QLabel()
        layout.addWidget(QLabel("Disk Partitions:"), 4, 0)
        layout.addWidget(partition_label, 4, 1)

        # 정보 업데이트
        self.update_labels(cpu_label, core_label, mem_label, disk_label, partition_label)

    def update_labels(self, cpu_label, core_label, mem_label, disk_label, partition_label):
        # CPU 정보 업데이트
        cpu_percent = psutil.cpu_percent(interval=None)
        cpu_label.setText(str(cpu_percent) + "%")

        # CPU 코어 수 업데이트
        core_count = psutil.cpu_count(logical=True)
        core_label.setText(str(core_count))

        # 메모리 정보 업데이트
        mem = psutil.virtual_memory()
        mem_percent = mem.percent
        mem_label.setText(str(mem_percent) + "%")

        # 디스크 정보 업데이트
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        disk_label.setText(str(disk_percent) + "%")

        # 디스크 파티션 정보 업데이트
        partitions = psutil.disk_partitions()
        partition_info = ""
        for partition in partitions:
            partition_info += f"Device: {partition.device} Mount Point: {partition.mountpoint}\n"
        partition_label.setText(partition_info)

        # 1초마다 업데이트
        QTimer.singleShot(1000, lambda: self.update_labels(cpu_label, core_label, mem_label, disk_label, partition_label))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
