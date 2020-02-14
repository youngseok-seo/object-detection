from PIL import Image
import cv2
import numpy as np
import imutils

def Contour(imagepath, number):
    img = cv2.imread(imagepath)

    im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(im_gray, (7,7), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    dilate = cv2.dilate(thresh, kernel, iterations=4)
    cv2.imwrite('imgray.jpeg', im_gray)

    imgray = cv2.imread('imgray.jpeg')

    lower = np.array([0, 0, 0])
    upper = np.array([100, 100, 100])
    shapeMask = cv2.inRange(img, lower, upper)

    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        cv2.drawContours(imgray, [c], -1, (0, 255, 0), 2)
        cv2.imshow("Image", imgray)
        
    cv2.imwrite('new'+str(number)+'.jpeg', imgray)
    return True

Contour('30.png', 1)
