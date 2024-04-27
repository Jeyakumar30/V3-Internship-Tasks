import cv2
from sklearn.metrics.pairwise import euclidean_distances

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

def calculate_distance(image1, image2, method):

  features1 = get_features(image1, method)
  features2 = get_features(image2, method)

  if features1 is None or features2 is None:
    return None

  features1 = features1.reshape(1, -1)
  features2 = features2.reshape(1, -1)

  distance = euclidean_distances(features1, features2)[0][0]

  return distance

image1 = cv2.imread("image.jpg")
image2 = cv2.imread("human.jpg")

hog_distance = calculate_distance(image1, image2, "hog")

sift_distance = calculate_distance(image1, image2, "sift")

print("Euclidean Distance (HOG):", hog_distance)
print("Euclidean Distance (SIFT):", sift_distance)

if hog_distance < 0.5 and sift_distance < 0.5:
  print("Both the Images are highly simliar")
else:
  print("Both Images differ greatly")

