print("Hello")


# import cv2
# import os
# import json

# images_dir = r"D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\COCO\Images"
# json_file = r"D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\COCO\_annotations.coco.json"
# output_dir = r"D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\COCO\Output"

# def parse_coco_json(json_file):
#     with open(json_file) as f:
#         coco_data = json.load(f)
#     annotations = {}
#     for annotation in coco_data['annotations']:
#         image_id = annotation['image_id']
#         bbox = annotation['bbox']
#         xmin = int(bbox[0])
#         ymin = int(bbox[1])
#         xmax = int(bbox[0] + bbox[2])
#         ymax = int(bbox[1] + bbox[3])
#         class_id = annotation['category_id']
#         class_name = coco_data['categories'][class_id]['name']
#         if image_id in annotations:
#             annotations[image_id].append((xmin, ymin, xmax, ymax, class_name))
#         else:
#             annotations[image_id] = [(xmin, ymin, xmax, ymax, class_name)]
#     print("""
#           Annotations List:
#           """, annotations)
#     return annotations

# def draw_bounding_boxes(image_path, annotations, output_dir):
#     image = cv2.imread(image_path)
#     image_name = os.path.basename(image_path)
#     print("This is the name of image being displayed: ",image_name)
#     if image_name in annotations:
#         for annotation in annotations[image_name]:
#             xmin, ymin, xmax, ymax, class_name = annotation
#             cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
#             cv2.putText(image, class_name, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
#         output_path = os.path.join(output_dir, os.path.basename(image_path))
#         cv2.imwrite(output_path, image)
#         print(f"Image with bounding boxes saved at: {output_path}")
#     else:
#         print(f"No annotations found for image: {image_path}")


# # Ensure output directory exists
# os.makedirs(output_dir, exist_ok=True)

# # Parse JSON file
# annotations = parse_coco_json(json_file)

# # Process each image
# for filename in os.listdir(images_dir):
#     if filename.endswith('.jpg'):
#         image_path = os.path.join(images_dir, filename)
#         draw_bounding_boxes(image_path, annotations, output_dir)



