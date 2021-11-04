from PyQt5 import QtGui
from PyQt5.QtCore import QEvent
from PyQt5.QtWidgets import *
import sys
import songs

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.songs = songs.Songs()
        
        self.buttons = []
        self.grid = QGridLayout()
        self.setWindowTitle("Music player")
        self.setLayout(self.grid)

        # buttons
        # back btn
        self.buttonBack = QPushButton()
        self.buttonBack.setIcon(QtGui.QIcon('./images/back.png'))
        self.grid.addWidget(self.buttonBack, 0, 0)
        # play btn
        self.buttonPlay = QPushButton()
        self.buttonPlay.setIcon(QtGui.QIcon('./images/play.png'))
        self.buttonPlay.clicked.connect(self.PlaySong)
        self.grid.addWidget(self.buttonPlay, 0, 1)
        # pause btn
        self.buttonPause = QPushButton()
        self.buttonPause.setIcon(QtGui.QIcon('./images/pause.png'))
        self.buttonPause.clicked.connect(self.StopSong)
        self.grid.addWidget(self.buttonPause, 0, 2) 
        # skip btn
        self.buttonPause = QPushButton()
        self.buttonPause.setIcon(QtGui.QIcon('./images/skip.png'))
        self.grid.addWidget(self.buttonPause, 0, 3) 

    def PlaySong(self):
        self.songs.Play()

    def StopSong(self):
        self.songs.Stop()
        
def RunApp():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
