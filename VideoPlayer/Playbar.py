import sys
from PyQt5.QtWidgets import QWidget, QApplication, QSlider, QLabel, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSignal


class PlayBar(QWidget):
    sent_current_frame = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal)
        self.time = QLabel("00:00:00")

        self.initUI()

    def initUI(self):
        self.slider.setRange(0, 0)
        self.slider.valueChanged.connect(self.current_frame)

        layout = QHBoxLayout()
        layout.addWidget(self.time)
        layout.addWidget(self.slider)

        self.setLayout(layout)

    def current_frame(self):
        current_frame = self.slider.value()
        total_frame = self.total_frame
        self.sent_current_frame.emit(current_frame, total_frame)

    def changeRange(self, start, finish, fps):
        self.fps = fps
        self.slider.setRange(start, finish)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.total_frame = finish    # This was knowing value of finish
        if start == 0 and finish == 0:
            self.time.setText("00:00:00")
            return

        self.slider.setTickInterval(self.fps * 5)

    def controlVideo(self, position):
        self.slider.setValue(position)
        position = float(position / self.fps)
        m = position // 60
        s = int(position) - m * 60
        c = (position - m * 60 - s) * 100
        self.time.setText("{:02d}:{:02d}:{:02d}".format(int(m), int(s), int(c)))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    playBar = PlayBar()
    playBar.show()
    sys.exit(app.exec_())