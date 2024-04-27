# Required libraries 
import cv2 as cv
import numpy as np 
import matplotlib.pyplot as plt 

#Reading Images:
#For Test Images:  9

image4 = cv.imread('test images/Image-9.jpg') 
gray4 = cv.cvtColor(image4, cv.COLOR_BGR2GRAY) 
cv.imshow("Gray 4", gray4)

blur4 = cv.GaussianBlur(gray4, (7, 7), 0)
cv.imshow("Blurred 4", blur4)


canny4 = cv.Canny(blur4, 50, 150, 3)
cv.imshow("Canny Edges 4",  canny4)

dilated4 = cv.dilate(canny4, (11, 11), iterations=3) 
cv.imshow("Dilated 4", dilated4)

(count, hierarchy) = cv.findContours( dilated4.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE) 
rgb = cv.cvtColor(image4, cv.COLOR_BGR2RGB) 
cv.drawContours(rgb, count, -1, (255, 0, 0), 2) 

plt.imshow(rgb)
plt.show()

print("Number of objects present in Image-9:", len(count))

cv.waitKey(0)
cv.destroyAllWindows()