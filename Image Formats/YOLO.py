import cv2 as cv
import yaml

def load_class_names(yaml_path):
    with open(yaml_path, 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
    return data['names']

def draw_boxes(image_path, annotation_path, class_names):
    image = cv.imread(image_path)
    
    with open(annotation_path, 'r') as file:
        annotations = file.readlines()
    
    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())
        
        image_height, image_width, _ = image.shape
        x_center *= image_width
        y_center *= image_height
        width *= image_width
        height *= image_height
        
        x_min = int(x_center - width / 2)
        y_min = int(y_center - height / 2)
        x_max = int(x_center + width / 2)
        y_max = int(y_center + height / 2)
        
        cv.rectangle(image, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
        
        class_name = class_names[int(class_id)]
        cv.putText(image, f'{class_name}', (x_min, y_min - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    cv.imshow('Image with Bounding Boxes', image)
    cv.imwrite(r"D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\Task\YOLO op\1.jpg",image)
    cv.waitKey(0)
    cv.destroyAllWindows()

image_path = r'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\shp1.v1i.combine.3.format\shp1.v1i.yolov8\test\images\2D-shape-_-pelmanism-game-202218_jpg.rf.674e201d0a10a8224ad1cdb402c80420.jpg'
annotation_path = r'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\shp1.v1i.combine.3.format\shp1.v1i.yolov8\test\labels\2D-shape-_-pelmanism-game-202218_jpg.rf.674e201d0a10a8224ad1cdb402c80420.txt'
yaml_path = r'D:\Data Science\V3 Python Tasks\OpenCV\Image Formats\shp1.v1i.combine.3.format\shp1.v1i.yolov8\data.yaml'

class_names = load_class_names(yaml_path)
draw_boxes(image_path, annotation_path, class_names)
