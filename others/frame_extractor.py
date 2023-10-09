import cv2


def extract_frames(path):
    """extracts frames form a video using cv2"""
    vid = cv2.VideoCapture(path)
    frame = 0
    success = 1
    while success:
        success, image = vid.read()
        cv2.imwrite(f"frames/frame_{frame}.jpg", image)
        frame += 1


if __name__ == '__main__':
    path = "C:\\Users\\l27se\\PycharmProjects\\bad_apple\\others\\opening1.mp4"
    extract_frames(path)
