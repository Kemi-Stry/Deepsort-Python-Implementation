import sys
from modules.VideoPlayer import VideoPlayer
from modules.Detector import Detector
from modules.Tracker import Tracker
from modules.File import File

file = File()
detector = Detector()
video_player = VideoPlayer(sys.argv[1])

video_player.play(detector)
