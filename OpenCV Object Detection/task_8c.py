import cv2 as cv
import numpy as np

img=cv.imread("test Images/Image-8.jpg")
img2=img.copy()


gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
_,thresholded=cv.threshold(gray,200,255,cv.THRESH_BINARY)

(contours, hierarchy) = cv.findContours(thresholded, cv.RETR_EXTERNAL,  cv.CHAIN_APPROX_SIMPLE)
print(len(contours))
largest_contour = None
largest_bbox = None
largest_area = 0
for cnt in contours:
    area = cv.contourArea(cnt)
    
    if area > largest_area:
        largest_contour = cnt
        largest_bbox = cv.boundingRect(cnt)
        largest_area = area

imgcontour=cv.drawContours(img,[largest_contour],-1,(255,0,0),2)
x, y, w, h = largest_bbox
img_with_bbox = cv.rectangle(imgcontour, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv.imshow("cont",img_with_bbox)

roi = img2[y:y+h, x:x+w]
gray=cv.cvtColor(roi,cv.COLOR_BGRA2GRAY)
_,th=cv.threshold(gray,90,255,cv.THRESH_BINARY)
cv.imshow("rect",th)


cv.waitKey(0)
cv.destroyAllWindows()