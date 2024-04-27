import cv2
from sklearn.model_selection import train_test_split
import os
import numpy as np

dataset = [[],[]]
img_dir = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\Splitting Dataset\NEU-DET\train\images"
cat = []
for category in os.listdir(img_dir):
    cat.append(category)
    for image in os.listdir(img_dir+"\\"+category):
        img = cv2.imread(img_dir+"\\"+category+"\\"+image)
        dataset[0].append(img)
        dataset[1].append(cat.index(category)) 

print(dataset[0])
print("Images: " ,dataset[0])
print("Categories: " ,dataset[1])

for ind, cat in enumerate(cat):
    print(str(ind) + " : " + cat)

print("Total no of rows: " + str(len(dataset)))
print("Total no of Images & Categories (Column): "+ str(len(dataset[0])))
dataset = list(map(list, zip(*dataset)))
train_size = 0.8
train_imgs , test_imgs = train_test_split(dataset, random_state=50, train_size=train_size)

 
print(f"Splitting {int(train_size*100)} Percent of data in to Train Set: " + str(len(train_imgs)))
print(f"Splitting {int((1-train_size)*100)+1} Percent of data in to Test Set: " + str(len(test_imgs)))
print("""
      
      Images for Train Set:
      
      """)
print(train_imgs)

print("""
      
      Images for Test Set:
      
      """)

print(test_imgs)