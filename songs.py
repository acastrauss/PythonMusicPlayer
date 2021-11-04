import os
import threading
import vlc
import time
from threading import *

class Songs():
    def __init__(self):
        self.songs = []
        self.currentSong = 0
        self.playing = False
        self.vlcInst = vlc.Instance()
        self.mediaPlayer = self.vlcInst.media_player_new()
        self.threadPlay = None

        self.FindSongs()

    def FindSongs(self):
        files = os.listdir('./songs')

        for f in files:
            songPath = os.path.join(os.path.abspath(os.curdir), 'songs', f)
            self.songs.append(songPath)
       
    def PlayThread(self):
        self.playing = True
        while self.playing:
            song = self.songs[self.currentSong]
            media = self.vlcInst.media_new(song)
            self.mediaPlayer.set_media(media)
            self.mediaPlayer.play()
            time.sleep(1.5)
            duration = self.mediaPlayer.get_length() / 1000
            time.sleep(duration)
            self.mediaPlayer.stop()
            self.currentSong = (self.currentSong + 1) % len(self.songs)

    def Play(self):
        if(len(self.songs) == 0 or self.playing):
            return
        else:
            self.threadPlay = Thread(target=self.PlayThread)
            self.threadPlay.start()

    def Stop(self):
        self.playing = False
        self.mediaPlayer.stop()
