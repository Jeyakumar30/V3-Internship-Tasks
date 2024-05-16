from table import main
import streamlit as st
import numpy as np
from PIL import Image
from streamlit_paste_button import paste_image_button as pbutton
import pyautogui
# import time



# tab1, tab2 = st.tabs(["Home", "About"])
# tab1.write("this is tab 1")
# tab2.write("this is tab 2")

# # You can also use "with" notation:
# with tab1:
#   st.radio('Select one:', [1, 2])
# # with tab2:

# Use PIL for reading image from the user as an object instead of cv2 -> reads img using path as an array
def detect(image_file = None, paste_btn = None):
    try:
        if (image_file is not None) and (st.button("Start", key = "1")):
            image = np.array(Image.open(image_file))
            
        elif (paste_btn.image_data is not None) and (st.button("Start", key = 2)):
            image = np.array(paste_btn.image_data)
        
        with st.spinner(text='In progress'):
            output = main(image) # Header, Result, BBox, RoI, df
            st.image(output[2],"Bounding Box Information")
            st.image(output[3],"Region of Interest")
            st.markdown("## Tabular Form")
            if output[0] is not None:
                st.write(output[0])
            st.dataframe(output[4])
            st.success("Hope You Liked this..")


    except UnboundLocalError or AttributeError :
        st.write("Stay cool! Your image is being processed...")

    

try:
    st.markdown("## Extracting Table Content from an Image")
    st.subheader("Upload Your Image")
    placeholder = st.empty()
    with st.sidebar:
        st.subheader("Copy & Paste an Image")
    
        paste_btn = pbutton(
        label="📋 Paste an image",
        text_color="#ffffff",
        background_color="#FF0000",
        hover_background_color="#380909",
        key="paste"
    )



    img_file = st.file_uploader("", type=["png","jpg","jpeg"])
    
    sidebar_action = 0
    button_clicked = False
    
    if paste_btn.image_data is None:
        sidebar_action = 1
               
    if (sidebar_action == 0):
        placeholder.image(paste_btn.image_data, caption="Input Image")
        detect(paste_btn=paste_btn)
    elif (sidebar_action == 1):
        st.image(img_file, caption="Input Image")
        detect(image_file=img_file)

        

    if paste_btn.image_data is not None:
        if st.button("Clear Selection", type="primary") and (not button_clicked):
            pyautogui.hotkey("ctrl", "F5")
            # st.experimental_rerun()
            # st.session_state.pop("paste")
            # st.session_state.paste = None
            # paste_btn.image_data = None
            # paste_btn = None
            # st.cache_data = None
            # st.rerun()
            
            
except AttributeError:
    st.write("Make sure that you have uploaded an Image 🙄")
# except:
#     st.write("")