import cv2 as cv
import numpy as np

img=cv.imread("test images\Image-11.jpg")
cv.imshow("original",img)
width=img.shape[1]
height=img.shape[0]
# for clustering 
# height*width --> to get all pixels ; 3 --> to get 3 color channels
data=np.reshape(img,(height*width,3))
data=np.float32(data)
# K-means  --> finds centers of clusters and groups input samples around the custers
# K --> no of clusters (in this case : no of colors)
# criteria --> no of iterations and accuracy criteria
# criteria_epsilon --> desired accuracy
# as soon as centers of clusters moves by less than criteria_epsilon on some iteration, the algorithm stops
# centers --> returns the centers where the colors are dominant in BGR format
K=5  
criteria=(cv.TERM_CRITERIA_EPS+cv.TERM_CRITERIA_MAX_ITER,10,1.0)
flags=cv.KMEANS_RANDOM_CENTERS
compactness,lebelness,centers=cv.kmeans(data,K,None,criteria,10,flags)
print(centers)

cv.waitKey(0)
cv.destroyAllWindows()