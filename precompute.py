# got frames from here: https://github.com/Felixoofed/badapple-frames
# common factors for compression: 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120

from matplotlib.image import imread
import json
import fpstimer
from pygame import mixer
import sys

X = 480
Y = 360
CX_FACTOR = 4  # compression factor for horizontal
CY_FACTOR = 12  # compression factor for vertical
FRAMES = 6572  # 1-indexed
ascii = "@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|(1{}]?-_+~>i!lI;:,\"^'."
print(len(ascii))
all_frames = []


def precompute(frame: int):
    # converting image into matrix of pixels
    image = imread(f"frames/output_{str(frame).zfill(4)}.jpg")  # use zfill to fill left side with 0
    full = [[None] * X for _ in range(Y)]
    for i, row in enumerate(image):
        for j, cell in enumerate(row):
            full[i][j] = cell[0]  # grayscale, so we only need one value (R = G = B)

    # compress image by taking average of sub matrices
    compressed = [[0] * (X // CX_FACTOR) for _ in range(Y // CY_FACTOR)]
    for r in range(Y):
        for c in range(X):
            cr = r // CY_FACTOR
            cc = c // CX_FACTOR
            compressed[cr][cc] += full[r][c]

    # take average
    for i in range(len(compressed)):
        for j in range(len(compressed[0])):
            compressed[i][j] //= (CX_FACTOR * CY_FACTOR)

    # determine whether a cell is black using threshold
    for i in range(len(compressed)):
        for j in range(len(compressed[0])):
            compressed[i][j] = ascii[compressed[i][j] // (256 // len(ascii))]

    seperator = "-" * (X // CX_FACTOR)
    all_frames.append(
        str(frame) + "\n" +
        "\n".join("".join(row) for row in compressed) +
        "\n" + seperator)  # the entire frame


if __name__ == '__main__':
    # # precompute frames
    # for i in range(1, FRAMES + 1):
    #     print(f"GENERATING FRAME {i}")
    #     precompute(i)
    #     print(all_frames[-1])
    # print("FINISHED GENERATING FRAMES")
    #
    # with open("frame_data.json", "w") as fd:
    #     json.dump(all_frames, fd)
    # print("SUCCESSFULLY SAVED FRAMES")

    with open("frame_data_contrast.json", "r") as fd:
        all_frames = json.load(fd)
    start = input("Enter anything to begin: ")

    # play music
    mixer.init()
    mixer.music.load("bad_apple.wav")
    mixer.music.play()

    timer = fpstimer.FPSTimer(30)
    for f in all_frames:
        print(f)
        timer.sleep()
