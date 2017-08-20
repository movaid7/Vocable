### Standard imports
##import cv2
##import numpy as np;
## 
### Read image
##im = cv2.imread("scenetext02.jpg", 0)
## 
### Set up the detector with default parameters.
##detector = cv2.SimpleBlobDetector_create()
##
### Detect blobs.
##keypoints = detector.detect(im)
## 
### Draw detected blobs as red circles.
### cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
##im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
## 
### Show keypoints
##cv2.imshow("Keypoints", im_with_keypoints)
##cv2.waitKey(0)

# test.py
import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from PIL import Image
import cv2
import numpy as np
import rect
from pytesseract import *


im = cv2.imread('C:/Users/Muhammad/Downloads/Design/1 Vocable/Images/OCR5.jpg',0)
cv2.imshow("SIZED", im)
cv2.waitKey(0)

# resize image so it can be processed
# choose optimal dimensions such that important content is not lost
r = 2000.0 / im.shape[1]
dim = (2000, int(im.shape[0] * r))
# perform the actual resizing of the image and show it
im = cv2.resize(im, dim, interpolation = cv2.INTER_LANCZOS4  )

thresh, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
##cv2.imshow("SIZED", im)
##cv2.waitKey(0)

img = Image.fromarray(im)

txt = image_to_string(img)
print(txt)
