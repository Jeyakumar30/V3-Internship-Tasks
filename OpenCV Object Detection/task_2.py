import cv2
import numpy as np

image = cv2.imread(r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\V3 Task\OpenCV Object Detection\test-2\Image-22.jpg") 

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Gray", gray_image)

threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# cv2.imshow("Threshold", threshold)


kernel = np.array([
    [-1,-1,-1],
    [-1,1,1],
    [-1,1,1]
])

closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)
# cv2.imshow("Closing", closing)

opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)
# cv2.imshow("Opening", opening)

contours, _ = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    cv2.drawContours(threshold, cnt, -1, (0,0,255), 2)

cv2.imshow("Image", threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()