import numpy as np
import cv2

# color range
lower_red = np.array([0,100,100])
upper_red = np.array([10,255,255])
lower_green = np.array([40,50,50])
upper_green = np.array([90,255,255])
lower_yellow = np.array([15,150,150])
upper_yellow = np.array([35,255,255])


image = cv2.imread("media/t_light_green.png")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
mask_green = cv2.inRange(hsv, lower_green, upper_green)


contour_red, _ = cv2.findContours(mask_red,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contour_green, _ = cv2.findContours(mask_green,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
contour_yellow, _ = cv2.findContours(mask_yellow,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("A", image)

if len(contour_red)>0 :
    print("Red")

if len(contour_green)>0:
    print("Green")

if len(contour_yellow)>0 :
    print("Yellow")

cv2.waitKey()
cv2.destroyAllWindows()