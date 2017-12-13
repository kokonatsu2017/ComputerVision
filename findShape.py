import numpy as numpy
import cv2

img = cv2.imread('images/someshapes.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('find shapes', img)
cv2.waitKey(0)

r, thresh = cv2.threshold(gray, 127, 255, 1)
img1, con, hier = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for c in con:
    
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    
    if len(approx) == 3:
        shape = "Triangle"
        cv2.drawContours(img, [c],0, (0,255,0),-1)
        
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        
    elif len(approx) == 4:
        x,y,w,h = cv2.boundingRect(c)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        
        #Rectangule or Square 
        if abs(w -h) <= 3:
            shape = "Square"
            cv2.drawContours(img, [c],0, (0,255,0),-1)
            cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        else:
            shape ="Rectangle"
            cv2.drawContours(img, [c], 0, (0, 0, 255), -1)
            
            cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
            
    elif len(approx) == 10:
        shape = "Star"
        cv2.drawContours(img, [c], 0, (255, 255, 0), -1)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
    
    elif len(approx) >= 12:
        shape = "Circle"
        cv2.drawContours(img, [c], 0, (0, 0, 255), -1)
        M = cv2.moments(c)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.putText(img, shape, (cx-50, cy), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        
        
    cv2.imshow('find Shapes',img)
    cv2.waitKey(0)
    
cv2.destroyAllWindows()