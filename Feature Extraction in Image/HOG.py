import cv2
from skimage.transform import resize
from skimage.feature import hog
from skimage import exposure
import matplotlib.pyplot as plt
img = cv2.imread("human.jpg", 0)
# cv2.imshow("Original Gray", img)
# plt.imshow(img)
# plt.show()
img = img[:, 270:988]
# plt.imshow(img)
# plt.show()
# resizing image
resized_img = resize(img, (128, 64))
# plt.axis("off")
# plt.imshow(resized_img)
# plt.show()
print(resized_img.shape)

#creating hog features
fd, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), visualize=True)
# cv2.imshow("HOG+img", hog_image)

exp = exposure.rescale_intensity(hog_image, (8,9))
cv2.imshow("HOG", exp)
cv2.waitKey(0)
cv2.destroyAllWindows()