import cv2

image = cv2.imread("media/balloon.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 230,255,cv2.THRESH_BINARY)
cv2.imshow("B", thresh)
contours, _ = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

AREA = image.shape[0]*image.shape[1]/150
dem = 0
for cnt in contours[:-1]:
    if cv2.contourArea(cnt) >= AREA:
        dem+=1
        cv2.drawContours(image, [cnt], -1, (0,255,0), 2, cv2.LINE_AA)
# cv2.drawContours(image, contours,-1, (0,255,0),2)# vẽ lại ảnh contour vào ảnh gốc 
print(dem)
cv2.imshow("A", image)
cv2.waitKey()
cv2.destroyAllWindows()