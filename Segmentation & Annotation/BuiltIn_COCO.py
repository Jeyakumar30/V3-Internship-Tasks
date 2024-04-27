import cv2 as cv
from pycocotools.coco import COCO
import numpy as np
import os
img_dir=r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations\barcode_poly_coco\images"
anno_file=r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations\barcode_poly_coco\result.json"
output_dir=r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations\barcode_poly_coco\Builtin COCO Output"
coco=COCO(anno_file)
def draw_polygons(img1,ann_ids):
    test = np.zeros_like(img1)
    for ann_id in ann_ids:
        ann = coco.loadAnns(ann_id)[0]
        segm=np.array(ann["segmentation"],np.int32).reshape(-1,1,2)
        cv.fillPoly(test, [segm],(0,222,0))
        image_new=cv.addWeighted(img1,0.7,test,1-0.7,0)
        cv.imwrite(output_dir+"\\"+imgname,image_new)
image_info = None
for filename in os.listdir(img_dir):
    imgname=filename
    for img in coco.dataset['images']:
        newfile=img['file_name'].split("/")
        newfileimg=newfile[1]
        if newfileimg == imgname:
            image_info = img
            break
    if image_info:
        image_path = img_dir + "\\" + imgname
        image = cv.imread(image_path)
        ann_ids = coco.getAnnIds(imgIds=image_info['id'])
        draw_polygons(image, ann_ids)
    else:
        print("Image not found in the dataset.")