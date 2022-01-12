#importing modules
import cv2
import numpy as np

#capturing video through webcam
cap= cv2.VideoCapture(0)

while(1):
    _, img= cap.read()

    #converting frame (img i.e BGR) to HSV (hue-saturation-value)

    hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    #defining the range of red color
    red_lower= np.array([136,87,111], np.uint8)
    red_upper= np.array([180,255,255], np.uint8)

    #defining the range of Green color
    Green_lower= np.array([50,60,60], np.uint8)
    Green_upper= np.array([80,255,255], np.uint8)

    #defining the range of yellow color
    yellow_lower= np.array([22,100,200], np.uint8)
    yellow_upper= np.array([40,255,255], np.uint8)

    #finding the range of red, Green and yellow color in the img
    red= cv2.inRange(hsv, red_lower, red_upper)
    Green= cv2.inRange(hsv, Green_lower, Green_upper)
    yellow= cv2.inRange(hsv, yellow_lower, yellow_upper)

    #morphological tranfromation, dilation
    kernal= np.ones((5,5), "uint8")

    red= cv2.dilate(red, kernal)
    res= cv2.bitwise_and(img, img, mask= red)

    Green= cv2.dilate(Green, kernal)
    res1= cv2.bitwise_and(img, img, mask= Green)

    yellow= cv2.dilate(yellow, kernal)
    res2= cv2.bitwise_and(img, img, mask= yellow)

    #tracking the RED color
    (contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area= cv2.contourArea(contour)
        if (area> 300):
            x,y,w,h = cv2.boundingRect(contour)
            img= cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
            cv2.putText(img, "RED color", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))

    #tracking the Green color
    (contours,hierarchy)=cv2.findContours(Green,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area= cv2.contourArea(contour)
        if (area> 300):
            x,y,w,h = cv2.boundingRect(contour)
            img= cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(img, "Green color", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0))

    #tracking the yellow color
    (contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area= cv2.contourArea(contour)
        if (area> 300):
            x,y,w,h = cv2.boundingRect(contour)
            img= cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,255), 2)
            cv2.putText(img, "yellow color", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0))


            #cv2.imshow("Redcolour", red)
            cv2.imshow("Color Tracking", img)
            #cv2.imshow("red", res)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllwindows()
                break

cv2.destroyAllWindows();
cap.release();
