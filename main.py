# got frames from here: https://github.com/Felixoofed/badapple-frames
# common factors for compression: 1, 2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 30, 40, 60, 120

from matplotlib.image import imread

# # OPTIONAL: writing to file in case it doesn't fit in terminal
# import sys
# sys.stdout = open('out.txt', 'w')

THRESHOLD = 100  # RBG needed to count a value as black
X = 480
Y = 360
CX_FACTOR = 6  # compression factor for horizontal
CY_FACTOR = 18  # compression factor for vertical
FRAMES = 6572  # 1-indexed


def print_frame(frame: int):
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
            compressed[i][j] = "&" if compressed[i][j] >= THRESHOLD else " "

    print(frame)
    print(*("".join(row) for row in compressed), sep="\n")  # prints the entire frame
    print("-" * (X // CX_FACTOR))  # separator


for i in range(2500, 4500, 2):
    print_frame(i)
#
# for i in range(1, FRAMES + 1, 1):
#     print_frame(i)