import cv2
import numpy as np

img = cv2.imread(r"animal.jpg") # Use 0 to read an img in gray scale.

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
sh = img.shape
print(type(img))
print("Image Shape: ", sh)

features = np.reshape(img, np.prod(sh))
cv2.cvtColor
print("Shape of features: ",features.shape)
print("Features:", features)
cv2.imshow("Original", img)
cv2.imshow("Gray Scale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()