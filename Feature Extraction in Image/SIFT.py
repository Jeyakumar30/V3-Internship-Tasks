import cv2
import matplotlib.pyplot as plt

# Load input image
input_image = cv2.imread('temple1.jpg', 0)
shape1 = input_image.shape
# Create SIFT object
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors
keypoints, descriptors = sift.detectAndCompute(input_image, None)

# Load another image for matching
other_image = cv2.imread('temple2.jpg', 0)
other_image = cv2.resize(other_image, shape1[::-1])

# Detect keypoints and compute descriptors in the other image
other_keypoints, other_descriptors = sift.detectAndCompute(other_image, None)

# Create Brute-Force matcher
bf_matcher = cv2.BFMatcher(cv2.NORM_L2,crossCheck=True)

# Match descriptors
matches = bf_matcher.match(descriptors, other_descriptors)

# Sort matches by distance
matches = sorted(matches, key=lambda x: x.distance)

# Draw matches on input image
output_image = cv2.drawMatches(input_image, keypoints, other_image, other_keypoints, matches[:50],other_image, flags=2)
# cv2.imshow("SIFT", output_image)
plt.imshow(output_image)
plt.axis("off")
plt.show()
# cv2.waitKey(0)
# cv2.destroyAllWindows()