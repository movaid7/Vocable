# USAGE
# python detect_blur.py --images images

# import the necessary packages
from imutils import paths
##import argparse
import cv2

def notBlurry(im):
    image = im.copy() #Copies image to prevent original from being altered
    '''Resize'''
    ##    # resize image so it can be processed
    # choose optimal dimensions such that important content is not lost
    r = 1000.0 / image.shape[1]
    dim = (1000, int(image.shape[0] * r))
    # perform the actual resizing of the image and show it
    gray = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(gray)
    text = "Not Blurry"

    # if the focus measure is less than the supplied threshold,
    # then the image should be considered "blurry"
    if fm < 10:
        return False

    # show the image
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    # cv2.imshow("Image", image)
    # key = cv2.waitKey(0)
    
    return True


def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()