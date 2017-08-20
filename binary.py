import cv2
import numpy as np

img = cv2.imread("page.jpg", 0)
ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)

print "Threshold selected : ", ret
cv2.imwrite("debug.png", img)
