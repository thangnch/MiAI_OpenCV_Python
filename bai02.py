import cv2
import imutils
filename = "media/sample.mp4"
video = cv2.VideoCapture(filename)

chieu = 0

while True:
    ret, frame = video.read()
    if ret:
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('a'):
            # Quay trai
            chieu = 90
        elif key == ord('d'):
            # Quay phai
            chieu  = -90
        elif key == ord(' '):
            chieu = 0
        if chieu != 0:
            frame = imutils.rotate(frame, chieu)
        cv2.imshow("Video", frame)

cv2.destroyAllWindows()
video.release()