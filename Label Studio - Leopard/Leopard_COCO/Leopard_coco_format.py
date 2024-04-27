import cv2
import numpy as np
import os
import json

img_dir = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_COCO\images"
output_dir = r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_COCO\output"
json_file = json.load(open(r"D:\Jeyakumar N K\Data Science\V3 Python Tasks\OpenCV\Annotations-II Leopard Dataset\Leopard_COCO\result.json"))


# def draw_polygons(img1,ann_ids,seg):

#     test = np.zeros_like(img1)
#     for segm in seg:
#         segm=np.array(seg,np.int32).reshape(-1,1,2)
#         cv2.fillPoly(test, [segm],(0,222,0))
#     image_new=cv2.addWeighted(img1,0.7,test,1-0.7,0)
#     out = os.path.join(output_dir, filename)
#     cv2.imwrite(out,image_new)


# for filename in os.listdir(img_dir):
#     if filename.endswith('.jpg'):
#         image_path = os.path.join(img_dir, filename)
#         seg = []
#         ann_ids = []
#         for i in json_file["images"]:
#             img_name = i["file_name"].split("/")[1]
#             if img_name == filename:
#                 index = json_file["images"].index(i)
#                 img_info = json_file["images"][index]
#                 img_id = img_info['id']

#         for i in json_file["annotations"]:
#             if i["image_id"] == img_id:
#                 ann_ids.append(i["id"])
#                 seg.append(i["segmentation"])
#             if img_info:
#                 image = cv2.imread(image_path)
#                 draw_polygons(image, ann_ids, seg)
#             else:
#                 print("Image not found in the dataset.")


def draw_polygons(img1, ann_ids, seg):

    test = np.zeros_like(img1)
    for segm in seg:
        seg_array = np.array(segm, np.int32).reshape(-1, 1, 2)
        cv2.fillPoly(test, [seg_array], (0, 222, 0))
    image_new = cv2.addWeighted(img1, 0.7, test, 1 - 0.7, 0)
    return image_new

for filename in os.listdir(img_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(img_dir, filename)
        ann_ids = []
        seg = []
        for i in json_file["images"]:
            
            img_name = i["file_name"].split("\\")[1]
            if img_name == filename:
                index = json_file["images"].index(i)
                img_info = json_file["images"][index]
                img_id = img_info['id']
        for annotation in json_file["annotations"]:
            if annotation["image_id"] == img_id:
                ann_ids.append(annotation["id"])
                seg.append(annotation["segmentation"])
        
        if ann_ids:
            image = cv2.imread(image_path)
            image_new = draw_polygons(image, ann_ids, seg)
            out = os.path.join(output_dir, filename)
            cv2.imwrite(out, image_new)
        else:
            print("No annotations found for image:", filename)
