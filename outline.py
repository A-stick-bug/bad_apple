import cv2
import fpstimer
from pygame import mixer

FRAMES = 6572  # 1-indexed

mixer.init()
mixer.music.load("bad_apple.wav")
mixer.music.play()

timer = fpstimer.FPSTimer(30)
for frame in range(1, FRAMES):
    img = cv2.imread(f'frames/output_{str(frame).zfill(4)}.jpg', 0)
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    edges = cv2.Canny(blur, 50, 150)

    cv2.imshow('Edges', edges)
    cv2.waitKey(1)
    timer.sleep()

cv2.destroyAllWindows()
