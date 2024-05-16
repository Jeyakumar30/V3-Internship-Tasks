import easyocr as oc
import cv2
import numpy as np
import pandas as pd
from PIL import Image
import streamlit as st


def main(image_file):
    header = None
    # image = cv2.imread('WhatsApp Image 2024-05-03 at 15.57.16_82fdd2a1.jpg')
    gray_image = cv2.cvtColor(image_file, cv2.COLOR_BGR2GRAY)
    # st.image(gray_image)
    kernel = np.array([ 
    [-1,-1,-1],
    [-1,10,-1],
    [-1,-1,-1]
    ])
    
    sharpened_image = cv2.filter2D(gray_image, -1, kernel)
    # st.image(sharpened_image)
    
    threshold = cv2.threshold(sharpened_image, 180, 255, cv2.THRESH_BINARY)[1]
    # st.image(threshold, "Threshold")
    
    canny = cv2.Canny(threshold, 180, 200, apertureSize = 7)
    # st.image(canny, "Canny")
    # dilate = cv2.dilate(canny, kernel = kernel, iterations = 3)
    # st.image(dilate)
    closing = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    # st.image(closing)
    contour = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    cv2.drawContours(image_file.copy(), contour, -1, (0, 0, 255), 1)

    largest_contour = None
    largest_bbox = None
    largest_area = 0

    for cnt in contour:
        area = cv2.contourArea(cnt)
    
        if area > largest_area:
            largest_contour = cnt
            largest_bbox = cv2.boundingRect(cnt)
            largest_area = area
    imgcontour = cv2.drawContours(image_file.copy(), [largest_contour], -1, (0, 0, 255), 1)

    x, y, w, h = largest_bbox
    img_with_bbox = cv2.rectangle(imgcontour, (x, y), (x+w, y+h), (0, 255, 0), 2)

    roi = image_file[y : y + h, x : x + w]
    # st.image(roi)

    def preprocessing(roi_img):
        # Noise Removal
        # roi_img = cv2.fastNlMeansDenoisingColored(roi_img, None, 10, 10, 7, 15)
        # st.image(roi_img)
        
        # Binarization
        gray_image = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY).astype(np.uint8)
        # st.image(gray_image)
        # img = cv2.adaptiveThreshold(gray_image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)

        # histogram equalization
        equ = cv2.equalizeHist(gray_image)
        # Gaussian blur
        equ = cv2.GaussianBlur(equ, (5, 5), 1)

        # manual thresholding
        # th2 = 10 # this threshold might vary!
        # equ[equ>=th2] = 255
        # equ[equ<th2]  = 0

        img = cv2.adaptiveThreshold(equ,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,13,2)

    
        return img
    
    # roi = preprocessing(roi)
    
    reader = oc.Reader(['en'], gpu=True)
    # result = reader.readtext('image copy 9.png', detail=0) #paragraph= True,

    result = reader.readtext(roi) #paragraph=True
    # print("Detected Test Results:", result)
    # st.write(result)
    reg = reader.recognize(roi)
    # st.write(reg)
    print(reg)

    for i in range(len(result)):
        top_left = tuple(map(int, result[i][0][0]))
        bottom_right = tuple(map(int, result[i][0][2]))
        # print(top_left, bottom_right)
        img = cv2.rectangle(roi,top_left,bottom_right,(0,255,255),1)


    def detect_columns(result, start = 0):
        cols = []
        col_ref = []
        x1 = []
        y1 = []

        try:
            for tup in range(len(result)):
                x, y = result[tup][0][0]
                x1.append(x)
                y1.append(y)

            beg = y1[start] - 10
            end = y1[start] + 10
            for i in range(start, len(result)):
                # st.write(i, y1[i])
                if (y1[i] >= beg) and (y1[i] <= end):
                    cols.append(result[i][1])
                    col_ref.append(x1[i])
        except IndexError:
            st.markdown("### Seems to be complex😟. But I'll try my best")

        return (x1, cols, col_ref)
    
    
    if result == []:
        st.markdown("## 🚫 No Detections")
    else:
        table = []
        counter = 0
        x1, cols, col_ref = detect_columns(result)
        
        # print(cols)
        if len(cols) < 2:
            # st.write("This block is about to execute..")
            header = cols[0]
            counter += 1
            x1, cols, col_ref = detect_columns(result, counter)

        for i in range(len(cols)):
            table.append([])
        # st.write(table)
        # print(result)
        # st.write(cols)
        # st.write(col_ref)

        for tup in range(len(cols)+counter, len(result)):
            x_val = int(x1[tup])
            beg = x_val - 30
            end = x_val + 30
            if (x_val >= beg) and (x_val <= end):
                for i in range(len(cols)):
                    if (x_val > (col_ref[i] - 100)) and (x_val < (col_ref[i] + 100)):
                        table[i].append(result[tup][1])


        df = pd.DataFrame(table).transpose()

        df = df.rename(columns = {i:cols[i] for i in range(len(cols))})

        st.download_button('On the dl', "results.xlxs")


        # df.to_excel("results.xlsx")
        # print(df)

    # cv2.imshow("BBox", img_with_bbox)
    # cv2.imshow("BBox Info",roi)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
        return (header, result, img_with_bbox, roi, df)

##  Testing
# main(np.array(Image.open("image copy 11.png")))



















# Old Code ✨
        # for i in range(len(result)):
        #     cnt_i += 1
        #     end = y1[start] + 10
        #     for j in range(y1[start]-10, end):
        #         cnt_j += 1
        #         if y1[i] == j:
        #             cols.append(result[i][1])
        #             col_ref.append(x1[i])
        #         if y1[i] > end:
        #             break
        #     else:
        #         continue
        #     break