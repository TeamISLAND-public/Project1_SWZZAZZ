import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from VideoPlayer.VideoList import VideoList
from VideoPlayer.VideoStreamer import VideoStreamer
from Recorder.RecordApp import RecordApp
from EffectBar.EffectBar import EffectBar
from EffectStatusBar.EffectstatusBar import EffectStatusBar
from Memory.Action import UndoList

class MyApp(QMainWindow):

    sent_video_name = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.commandList = UndoList.getInstance()
        self.videoPlayer = VideoStreamer()
        self.videoTable = VideoList(self.videoPlayer)
        self.effectBar = EffectBar()
        self.effectStatusBar = EffectStatusBar()
        self.effectStatusBar.effectbar_to_effectstatusbar(self.effectBar)       #effectstatusbar is getting information about effects
        self.effectBar.playbar_to_effectbar(self.videoPlayer.timeBox)           #effectbar is getting value of current frame
        self.effectBar.videobar_to_effectbar(self.videoPlayer)                  #effectbar is getting value of click position
        self.videoPlayer.effectbar_to_videostreamer(self.effectBar)             #videoplayer is getting result video
        self.videoPlayer.effectstatusbar_to_videostreamer(self.effectStatusBar) #videoplayer is getting fixing elements (e.g. delete)
        self.effectBar.main_to_effectbar(self)
        self.initUI()
        self.flag = True

    def initUI(self):
        self.resize(1280, 720)
        self.menu()
        self.statusBar()

        layout = QGridLayout()
        layout.setRowStretch(0, 2)
        layout.setRowStretch(1, 1)
        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 3)
        layout.addWidget(self.videoTable, 0, 0)
        layout.addWidget(self.effectBar, 1, 0)
        layout.addWidget(self.effectStatusBar, 1, 1)
        layout.addWidget(self.videoPlayer, 0, 1)
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.show()

    def open_video(self):
        filename = QFileDialog.getOpenFileName(self, "Open file", os.getcwd(), "Video files(*.mp4 *.mkv *.avi)")

        # if Video is already opened
        if filename[0] in self.videoTable.fileNameList:
            errorbox = QMessageBox()
            errorbox.warning(self, "Error Message", "Video is already opened", QMessageBox.Ok)
            return

        # if user doesn't select the video
        if not filename[0]:
            return

        self.videoPlayer.change_playButtonStatus()
        self.videoTable.setColumnCount(1)
        if self.flag:
            self.videoPlayer.set_video(filename[0])
            self.flag = False
        else:
            self.videoPlayer.change_video(filename[0])
        self.videoTable.add_video(filename[0])
        # when adding video video_name must be sent
        self.sent_video_name.emit(filename[0])
        self.videoTable.doubleClicked.connect(self.change_video)
        # self.videoPlayer.set_maxVolume()

        self.videoPlayer.videoPlayer()

    def change_video(self, row):
        for i in self.videoTable.selectedItems():
            self.videoPlayer.change_video(i.text())
            # Not only for adding but also when action was held for change video sent_video_name must emit
            self.sent_video_name.emit(i.text())

        # self.videoPlayer.set_maxVolume()
        self.videoPlayer.videoPlayer()

    def record_video(self):
        recordWindow = RecordApp.getInstance()
        recordWindow.show()
        recordWindow.start()

    def menu(self):
        menu = self.menuBar()
        menu_file = menu.addMenu("&File")
        menu_edit = menu.addMenu("&Edit")

        video_open = QAction("&Open", self)
        video_open.setShortcut("Ctrl+O")
        video_open.setStatusTip("Open the video file")
        video_open.triggered.connect(self.open_video)

        webCam_open = QAction("&Record", self)
        webCam_open.setShortcut("Ctrl+R")
        webCam_open.setStatusTip("Record with webcam")
        webCam_open.triggered.connect(self.record_video)

        video_new = QMenu("&New", self)
        video_new.addAction(video_open)
        video_new.addAction(webCam_open)

        file_exit = QAction("E&xit", self)
        file_exit.setShortcut("Ctrl+Q")
        file_exit.setStatusTip("Exit")
        file_exit.triggered.connect(QCoreApplication.instance().quit)

        file_save = QAction("&Save", self)
        file_save.setShortcut("Ctrl+S")
        file_save.setStatusTip("Save the video file")
        file_save.triggered.connect(self.videoPlayer.save_video)

        menu_file.addMenu(video_new)
        menu_file.addAction(file_save)
        menu_file.addAction(file_exit)

        undoList = QAction("Undo &List", self)
        undoList.setStatusTip("Show undo list")
        undoList.triggered.connect(self.commandList.show)

        undo = QAction("&Undo", self)
        undo.setShortcut("Ctrl+Z")
        undo.setStatusTip("Undo last action")
        undo.triggered.connect(self.commandList.stack.undo)

        redo = QAction("&Redo", self)
        redo.setStatusTip("Cancel undo action")
        redo.triggered.connect(self.commandList.stack.redo)

        menu_edit.addAction(undoList)
        menu_edit.addAction(undo)
        menu_edit.addAction(redo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
