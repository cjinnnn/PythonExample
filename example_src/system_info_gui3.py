import sys
import psutil
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPalette
from PyQt5.QtWidgets import QApplication, QWidget

class SystemMonitor(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("System Monitor")
        self.colors = [QColor(0, 255, 0), QColor(255, 0, 0), QColor(0, 0, 255)]
        self.disk_partitions = psutil.disk_partitions()
        self.num_partitions = len(self.disk_partitions)
        self.cpu_usage = [0.0] * psutil.cpu_count()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(90, 90, 90)) # 새로운 배경색 지정
        self.setPalette(palette)


        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(1000)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(Qt.white)

        # Draw CPU Usage
        for i, usage in enumerate(self.cpu_usage):
            painter.setBrush(self.colors[i % len(self.colors)])
            painter.drawRect(50 + i * 50, 150, 40, -usage * 50)

        painter.drawText(50, 130, "CPU Usage (%)")

        # Draw Disk Usage
        # for i, partition in enumerate(self.disk_partitions):
        #     usage = psutil.disk_usage(partition.mountpoint)
        #     percent = usage.percent
        #     painter.setBrush(self.colors[i % len(self.colors)])
        #     painter.drawRect(50 + i * 100, 350, 80, -percent * 3)
        #     painter.drawText(50 + i * 100, 340, f"{partition.mountpoint}: {percent}%")

        painter.drawText(50, 330, "Disk Usage (%)")

    def update(self):
        # Update CPU Usage
        cpu_percent = psutil.cpu_percent(percpu=True)
        for i, percent in enumerate(cpu_percent):
            self.cpu_usage[i] = percent / 100.0

        # Update Disk Usage
        # for i, partition in enumerate(self.disk_partitions):
        #     usage = psutil.disk_usage(partition.mountpoint)
        #     self.disk_partitions[i] = psutil.disk_partition_info(partition.mountpoint)

        self.repaint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor = SystemMonitor()
    monitor.show()
    sys.exit(app.exec_())
