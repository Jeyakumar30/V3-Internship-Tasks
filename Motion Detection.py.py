import streamlit as st
import cv2
import numpy as np
import time

prev_mean = 0 # for finding difference in mean
previous = None # for drawing bounding box


st.title("Real Time Motion Detection")
run = st.toggle('I\'m Ready')
FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

def detection_algo(camera, previous, prev_mean):
    # count = 0
    while run:
        _, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result = np.abs(np.mean(gray) - prev_mean)
        prev_mean= np.mean(gray)

        
        if result > 0.2:
            cv2.putText(frame, "Movement Detected", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.9, (255, 0, 0), 2)
            # count += 1

            if previous is None:  
                previous = gray  
                continue
            differ_frame = cv2.absdiff(previous, gray)
            previous = gray
            thresh_frame = cv2.threshold(differ_frame, 30, 255, cv2.THRESH_BINARY)[1]
            dilate = cv2.dilate(thresh_frame, None, iterations = 2)  
            cont,_ = cv2.findContours(dilate.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            for c in cont:
                if cv2.contourArea(c) < 1700:
                    continue
                (x, y, w, h) = cv2.boundingRect(c)  
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3) 
        
        FRAME_WINDOW.image(frame)
        time.sleep(0.5)

        # print(gray.shape)

    else:
        # st.write("Number of times motion detected: " + str(count))
        st.write('Switch ON to detect motion')

detection_algo(camera, previous, prev_mean)