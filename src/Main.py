import sys
from modules.VideoPlayer import VideoPlayer
from modules.Detector import Detector
from modules.Tracker import Tracker


detector = Detector
video_player = VideoPlayer(sys.argv[1])


print(sys.argv[1])
video_player.play()
