import sys
import modules.VideoPlayer as VideoPlayer

video_player = VideoPlayer.VideoPlayer(sys.argv[1])
print(sys.argv[1])
video_player.play()
