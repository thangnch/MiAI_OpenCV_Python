import cv2

detector = cv2.CascadeClassifier("media/haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(1)
while True:
    ret, frame = cam.read()
    if ret:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rects = detector.detectMultiScale(gray, scaleFactor=1.05,
                                          minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
        # loop over the bounding boxes
        for (x, y, w, h) in rects:
            # draw the face bounding box on the image
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow("Goc", frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            # Luu
            i = 0
            for (x, y, w, h) in rects:
                i = i + 1
                crop_face = frame[y:y+h,x: x+w]
                cv2.imwrite("faces/{}.png".format(i), crop_face)

cv2.destroyAllWindows()
cam.release()
