import cv2
# Load the cascade
# face_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_Classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
# To capture video stream from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')


while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    faces = face_classifier.detectMultiScale(
    gray, scaleFactor=1.05, minNeighbors=5
)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_classifier.detectMultiScale(roi_gray, 1.05,5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 255), 2)
        smile = smile_Classifier.detectMultiScale(roi_gray, 1.05,5)
        for (sx, sy, sw, sh) in smile:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
    cv2.putText(img, "Face", (10,30), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
    cv2.putText(img, "Eye", (10,80), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), 2)
    cv2.putText(img, "Lip", (10,130), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)

    # Display
    cv2.imshow('img', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()