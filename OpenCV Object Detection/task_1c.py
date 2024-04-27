import cv2
import numpy as np

image = cv2.imread('.//test images//Image-1.jpg')

image=cv2.resize(image, (500,500))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)


center = []
rad = []


for i in range(len(contours)):
   (x, y), radius = cv2.minEnclosingCircle(contours[i])
   center.append((int(x), int(y)))
   rad.append(int(radius))
small = 0
large = 0
for i in range(len(rad)):
   if rad[i] < sum(rad)//len(rad):
      cv2.circle(image, center[i], rad[i], (0, 255, 255), -1)
      if rad[i] < 2*min(rad):
         small +=1
      else:
         large +=1
print("No of Large Circles: ", large)

print("No of Small Circles: ", small)


cv2.imshow('Minimum Enclosing Circle', image)
cv2.waitKey(0)