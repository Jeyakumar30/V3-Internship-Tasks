import cv2
import numpy as np
import os

img_dir = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_YOLO\images"
labels = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_YOLO\labels"
output_dir = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_YOLO\output"


def draw_polylines(image_path, label_file, output_dir):
    image = cv2.imread(image_path)
    transparent = np.zeros_like(image)
    width = image.shape[1]
    height = image.shape[0]
    alpha = 0.7
    with open(label_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            list1 = list(map(float, line.split(" ")[1:]))
            list2 = []
            for i in range(len(list1)):
                if i % 2 == 0:
                    list2.append(list1[i]*width)
                else:
                    list2.append(list1[i]*height)

            arr = np.array(list2)
            arr=arr.reshape(-1,1,2).astype(np.int32)

            cv2.fillPoly(transparent,[arr], (0,255,0))
            image = cv2.addWeighted(image, alpha, transparent, 1 - alpha, 0)
            
            output_path = os.path.join(output_dir, os.path.basename(image_path))
            cv2.imwrite(output_path, image)
            
            
        

for filename in os.listdir(img_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(img_dir, filename)
        label_file = os.path.join(labels, os.path.splitext(filename)[0] + '.txt')
        if os.path.exists(label_file):
            draw_polylines(image_path, label_file, output_dir)
        else:
            print(f"No Label file found for image: {filename}")