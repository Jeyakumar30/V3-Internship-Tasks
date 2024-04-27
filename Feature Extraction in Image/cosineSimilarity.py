# # tes = numpy.load(r"D:/Jeyakumar N K/Data Science/Data Sets/Body Measurements/NP Arr/w00/w00_eb_l_acc.npy")
# # print(tes.shape)

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity

def get_features(image, method):

  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  if method == "hog":
    hog = cv2.HOGDescriptor()
    return hog.compute(gray)
  elif method == "sift":
    sift = cv2.SIFT_create()
    _, descriptors = sift.detectAndCompute(gray, None)
    return descriptors
  else:
    print("Kindly opt a correct method to find similarity bewteen your input images")

def calculate_similarity(image1, image2, method):

  features1 = get_features(image1, method)
  features2 = get_features(image2, method)

  if features1 is None or features2 is None:
    return None

  features1 = features1.reshape(1, -1)
  features2 = features2.reshape(1, -1)
#   print(f"""
#         Feature 1: {features1.shape}, 
#         Feature 2: {features2.shape}""")
#   h1 = features1.shape[1]
#   print("Shape 1: ", h1)
#   h2 = features2.shape[1]
#   print("Shape 2: ", h2)
#   if h1 != h2:
#     if h1 < h2:
#       features2 = features2[:h1]
#       print(features1, features2)
#     elif h2 < h1:
#       features1 = features1[:h2]
#       print(features1)


  similarity = cosine_similarity(features1, features2)[0][0]

#   print("Testing: ", cosine_similarity(features1, features2))

  return similarity


img1 = cv2.imread("Tajmahal.jpg")
img2 = cv2.imread("human.jpg")

img1 = cv2.resize(img1, (500,500))
img2 = cv2.resize(img2,(500,500))

plt.subplot(1,2,1)
plt.imshow(img1, cmap = "gray")
plt.subplot(1,2,2)
plt.imshow(img2, cmap = "gray")
plt.show()

hog_similarity = calculate_similarity(img1, img2, "hog")


sift_similarity = calculate_similarity(img1, img2, "sift")

print("Cosine Similarity (HOG):", hog_similarity)
print("Cosine Similarity (SIFT):", sift_similarity)

if hog_similarity > 0.5 and sift_similarity > 0.5:
  print("Both the Images seems to be simliar")
else:
  print("Both are different Images")
