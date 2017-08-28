# test.py
import os
os.chdir('C:\Python27\Lib\site-packages\pytesser')
from PIL import Image
import cv2
import numpy as np
import rect
from pytesseract import *
from detect_blur import notBlurry
from getTextAreas import arrTextAreas
import pyttsx3
import re
from Spellcheck import correction, is_english_word


'''Initialise TTS Engine'''
engine = pyttsx3.init()
rate = int(engine.getProperty('rate'))
engine.setProperty('rate', rate-85)
engine.setProperty('voice', 'TTS_MS_EN-US_ZIRA_11.0')

'''Variables'''
pictureLocation = 'C:/Users/Muhammad/Downloads/Design/1 Vocable/Images/OCR4.jpg'

try:
    '''Read in an image'''
    im = cv2.imread(pictureLocation)
    if im is None:
        raise ValueError('Error locating picture', pictureLocation) #Image file was not found

    '''If the picture is a colour picture, convert it to grayscale'''
    try:
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    except cv2.error as e:
        print "Picture is already grayscale"

    print notBlurry(im)
    '''If the picture is not blurry, extract text from it'''
    if notBlurry(im):

        arr = arrTextAreas(im)
        imCopy = im.copy()

        for img in arr:

            thresh, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            cv2.imshow("contoured.jpg", img)
            # cv2.waitKey(0)

            img = Image.fromarray(img)
            txt = image_to_string(img)

            '''Remove line breaks'''
            tmp = txt.split()
            txt = ' '.join(tmp)

            # qwert = re.findall(r'\w+', txt)
            # OR
            # print(re.split("[^0-9a-zA-Z]*", a))
            # print qwert

            text_file = open("Output.txt", "w")
            text_file.write("%s" % txt)
            text_file.close()

            words = (re.split(" ", txt))
            tx = ""
            print txt

            for w in words:
                '''Check if word (with punctuation removed) is valid'''
                # print is_english_word(re.split("[^0-9a-zA-Z]*", w)[0])
                if is_english_word(re.split("[^0-9a-zA-Z]*", w)[0]):
                    tx += w + " "
                else:
                    w = re.split("[^0-9a-zA-Z]*", w)[0]
                    tx += correction(w) + " "

            print tx
            engine.say(tx)
            engine.runAndWait()

    else:
        raise ValueError('Picture is too blurry', pictureLocation) #Image file was not found

except ValueError as err:
    print(err.args)


'''Terminate Program'''
raise SystemExit("Program has terminated")