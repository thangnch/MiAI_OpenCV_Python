import cv2

image = cv2.imread("media/plate.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127,255,cv2.THRESH_BINARY)
cv2.imshow("B", thresh)
contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

WIDTH = image.shape[1]*0.1
HEIGHT = image.shape[0]*0.5
dem = 0
for cnt in contours[:-1]:
    x, y, w, h = cv2.boundingRect(cnt)
    if w <= WIDTH and h>=HEIGHT:
        dem+=1
        cv2.drawContours(image, [cnt], -1, (0,255,0), 2, cv2.LINE_AA)
        crop_face = image[y:y + h, x: x + w]
        cv2.imwrite("numbers/{}.png".format(dem), crop_face)
# cv2.drawContours(image, contours,-1, (0,255,0),2)# vẽ lại ảnh contour vào ảnh gốc 
print(dem)
cv2.imshow("A", image)
cv2.waitKey()
cv2.destroyAllWindows()