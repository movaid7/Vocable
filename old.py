import cv2
import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from PIL import Image
from pytesseract import *
import re
import time
from Spellcheck import correction,is_english_word



image = cv2.imread("C:/Users/Muhammad/Downloads/Design/1 Vocable/Images/OCR2.jpg")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # grayscale
_,thresh = cv2.threshold(gray,120,255,cv2.THRESH_BINARY_INV) # threshold
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(4,4))
dilated = cv2.dilate(thresh,kernel,iterations = 12) # dilate
_, contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) # get contours

arr = []



# for each contour found, draw a rectangle around it on original image
for contour in contours:
    # get rectangle bounding contour
    [x,y,w,h] = cv2.boundingRect(contour)
    # # discard areas that are too large
    # if h>400 and w>400:
    #     continue
    # discard areas that are too small
    if h<20 or w<20:
        continue

    roi = gray[y:y + h, x:x + w]
    arr.append(roi)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)

cv2.imshow("contoured.jpg", image)
cv2.waitKey(0)

tx = ""
arr = arr[::-1]
t0 = time.time()


for im in arr:


    thresh, im = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    r = 1000.0 / im.shape[1]
    dim = (1000, int(im.shape[0] * r))
    # perform the actual resizing of the image and show it
    im = cv2.resize(im, dim, interpolation=cv2.INTER_AREA )

    cv2.imshow("pic.jpg", im)
    cv2.waitKey(0)

    im = Image.fromarray(im)
    txt = image_to_string(im)
    words = (re.split("[^0-9a-zA-Z]*", txt))


    for w in words:
        if is_english_word(w):
            tx += w + " "
        else:
            tx += correction(w) + " "
print(tx)
t1 = time.time()
print t1 - t0