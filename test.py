import numpy as np
import cv2 as cv

img = cv.imread('30.png', 0)
img = cv.medianBlur(img, 5)
print(img.shape)

cimg = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
# print(f"img: \n {img}")
# print(f"cimg: \n {cimg}")
# print(f"length of cimg array? {len(cimg)}")

print(cimg.shape)
print(cimg.size)

circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,200,
                            param1=50,param2=80,minRadius=400,maxRadius=0)

print('before uint')
circles = np.uint16(np.around(circles))
print('before for loop')
for i in circles[0,:]:
    # draw the outer circle
    cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv.imshow('detected circles',cimg)
cv.waitKey(0)
cv.destroyAllWindows()