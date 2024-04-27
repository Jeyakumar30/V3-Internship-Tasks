import cv2
import os
import xml.etree.ElementTree as ET

# Loading Images and XML files
images_dir = 'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\Image'
xml_dir = 'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\XML'
output_dir = 'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\Output'

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    objects = root.findall('object')
    annotations = []
    for obj in objects:
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)
        class_name = obj.find('name').text
        annotations.append((xmin, ymin, xmax, ymax, class_name))
       
    return annotations

def draw_bounding_boxes(image_path, xml_file, output_dir):
    image = cv2.imread(image_path)
    bboxes = parse_xml(xml_file)
    for bbox in bboxes:
        xmin, ymin, xmax, ymax, class_name = bbox
        cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        cv2.putText(image, class_name, (xmin, ymin - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    output_path = os.path.join(output_dir, os.path.basename(image_path))
    cv2.imwrite(output_path, image)
    print(f"Image with bounding boxes saved at: {output_path}")

# Processing each image with corresponding XML file
for filename in os.listdir(images_dir):
    if filename.endswith('.jpg'):
        image_path = os.path.join(images_dir, filename)
        xml_file = os.path.join(xml_dir, os.path.splitext(filename)[0] + '.xml')
        if os.path.exists(xml_file):
            draw_bounding_boxes(image_path, xml_file, output_dir)
        else:
            print(f"No XML file found for image: {filename}")