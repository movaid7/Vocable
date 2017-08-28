import cv2

def arrTextAreas(im):
    image = im.copy()
    #image = cv2.imread("C:/Users/Muhammad/Downloads/Design/1 Vocable/Images/OCR8.jpg")
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # grayscale
    _, thresh = cv2.threshold(image, 120, 255, cv2.THRESH_BINARY_INV)  # threshold
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (4, 4))
    dilated = cv2.dilate(thresh, kernel, iterations=12)  # dilate
    _, contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # get contours

    arr = []

    # for each contour found, draw a rectangle around it on original image
    for contour in contours:
        # get rectangle bounding contour
        [x, y, w, h] = cv2.boundingRect(contour)
        # # discard areas that are too large
        # if h>400 and w>400:
        #     continue
        # discard areas that are too small
        if h < 20 or w < 20:
            continue

        roi = im[y:y + h, x:x + w]
        arr.append(roi)

        # draw rectangle around contour on original image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 0), 2)

    r = 1000.0 / image.shape[1]
    dim = (1000, int(image.shape[0] * r))
    # perform the actual resizing of the image and show it
    image = cv2.resize(image, dim, interpolation=cv2.INTER_LANCZOS4)

    # cv2.imshow("contoured.jpg", image)
    # cv2.waitKey(0)
    return arr[::-1]



    # for each contour found, draw a rectangle around it on original image
    # for contour in contours:
    #     # get rectangle bounding contour
    #     [x, y, w, h] = cv2.boundingRect(contour)
    #
    #     # # discard areas that are too large
    #     # if h>500 and w>500:
    #     #     continue
    #     #
    #     # discard areas that are too small
    #     if h < 20 or w < 20:
    #         continue
    #
    #     # draw rectangle around contour on original image
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 255), 2)

    # # write original image with added contours to disk
    # cv2.imshow("contoured.jpg", image)
    # cv2.waitKey(0)


