import cv2

cam = cv2.VideoCapture(1)
while True:
    ret, frame = cam.read()
    if ret:
        cv2.imshow("Goc", frame)
        w = frame.shape[1]
        h = frame.shape[0]
        print(w, h)

        cw = w//2
        ch = h//2

        w1 = int(w*0.2)
        h1 = int(h*0.2)

        frame1 = frame[ch-h1//2:ch+h1//2,cw-w1//2:cw+w1//2]
        cv2.imshow("Crop", frame1)
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
cam.release()
