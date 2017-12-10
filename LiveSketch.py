import cv2
import numpy as np

def sketch(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    
    canny_edges = cv2.Canny(blurred, 10, 70)
    
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)

    return mask


#Initialize webcam
live = cv2.VideoCapture(0)

while True:
    ret, frame = live.read()
    cv2.imshow('Our Live Sketcher', sketch(frame))

    if cv2.waitKey(1) == 13:#Enter key
        break
        
live.release()
cv2.destroyAllWindows()