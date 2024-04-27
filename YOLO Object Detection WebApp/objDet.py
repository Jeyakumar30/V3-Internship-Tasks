import streamlit as st
from streamlit_image_select import image_select
import cv2
from new import main
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_paste_button import paste_image_button as pbutton
import pyautogui
 
# Use PIL for reading image from the user as an object instead of cv2 -> reads img using path as an array

def user_selection(image_file, paste_btn):
        try:
            if image_file is not None:
                left, right = st.columns(2)
                left.image(image_file,"Input")
                if st.button("Detect Objects", key = 1):
                    image_file = Image.open(image_file)
                    output = main(image_file)
                    right.image(output[0],"Output")
                
            elif paste_btn.image_data is not None:
                left, right = st.columns(2)
                left.image(paste_btn.image_data,"Input")
                if st.button("Detect Objects", key = 2):
                    image_file = np.array(paste_btn.image_data)
                    output = main(image_file)
                    right.image(output[0],"Output")
            return output

        except FileNotFoundError as AE:
            st.write("Please Upload an Image to detect Objects")
        except:
            print()

def default():
    try:
        images = ["image.png", "image copy 8.png", "image copy 4.png"]
        clicked = image_select("Select an Image", images, key = "k1")
        left1, right1 = st.columns(2)
        left1.image(clicked,"Input")
        if st.button("Detect Objects", key = "1"):
            clicked = Image.open(clicked)
            output = main(clicked)
            right1.image(output[0],"Output")
        return output
    except:
        print()

def postprocessing(output):
    try:
        classes =  output[1]
        st.subheader("Total Number of Objects Detected: "+ str(len(classes)))
        st.subheader("List of Objects Detected: ")
        color = output[2]
        col_dic = {}
        for i in color.keys():
            i = int(i)
            if color[i] == (255, 0, 0):
                col_dic[i] = "Red"
            elif color[i] == (0, 255, 0):
                col_dic[i] = "Green"
            elif color[i] == (0, 0, 255):
                col_dic[i] = "Blue"
            elif color[i] == (0,255,255):
                col_dic[i] = "Cyan"
            elif color[i] == (255,255,0):
                col_dic[i] = "Yellow"
            elif color[i] == (255,0,255):
                col_dic[i] = "Magenta" 
        cls_inverted = {value.capitalize(): key for key, value in output[3].items()}
        cls_dict = {}
        col_map = {}
        # col_dic
        # cls_inverted
        for i in np.unique(classes):
            cls_dict[i] = classes.count(i)
            col_map[i] = col_dic[cls_inverted[i]]
        # cls_dict

        # st.write(col_map)    

    
        if len(cls_dict) == 0:
            st.write("No Objects Detected")
        else:
            st.dataframe({"No": list(range(1, len(cls_dict)+1)), "Class Name" : list(cls_dict.keys()), "Count" : list(cls_dict.values()),"Color": list(col_map.values())})
    except:
        print("")

def start():
    st.title("Object Detection using YOLO")

    sidebar_action = 0

    with st.sidebar:
        st.subheader("Upload Your Image")
        image_file = st.sidebar.file_uploader("", type=["png","jpg","jpeg"])
    
        # st.subheader("Or")
        st.subheader("Paste an Image")
        paste_btn = pbutton(
        label="📋 Paste an image",
        text_color="#ffffff",
        background_color="#FF0000",
        hover_background_color="#380909",
    )

        if (image_file is None) and (paste_btn.image_data is None):
            sidebar_action = 1        
        # paste_btn
    
        if paste_btn.image_data is not None:
            if st.button("Predefined Images", type="primary"):
                pyautogui.hotkey("ctrl","F5")
               
    if (sidebar_action == 0):
        postprocessing(user_selection(image_file, paste_btn))
    elif (sidebar_action == 1):
        postprocessing(default())

start()
