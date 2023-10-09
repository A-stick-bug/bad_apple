import cv2
import fpstimer
from pygame import mixer

FRAMES = 2776

# play music
mixer.init()
mixer.music.load("opening1.wav")
mixer.music.play()

timer = fpstimer.FPSTimer(30)
for frame in range(FRAMES):
    img = cv2.imread(f'frames/frame_{frame}.jpg', 0)
    blur = cv2.GaussianBlur(img, (3, 3), 0)
    edges = cv2.Canny(blur, 50, 150)

    cv2.imshow('Edges', edges)
    cv2.waitKey(1)
    timer.sleep()

cv2.destroyAllWindows()
