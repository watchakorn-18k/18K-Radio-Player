from threading import Thread
import vlc
import time

def one():
    p = vlc.MediaPlayer("http://112.121.151.133:8147/live")
    time.sleep(10)
one()