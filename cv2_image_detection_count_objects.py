# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gPEfXj3mXLWUV8_3QScg8RE5ONzWkNVe
"""

import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
image1 = cv2.imread("/Users/f./Desktop/pic1_money.png")
image2 = cv2.imread("/Users/f./Desktop/pic1_money.png")
xcoordinate = []
ycoordinate = []
k = 0


while True:
   
    #_, frame = cap.read() #Set the frame
    #belt = frame[300:350, 200:500]
    #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Convert the frame to gray colour for better visibility
    #_, threshold = cv2.threshold(gray_frame, 120, 255, cv2.THRESH_BINARY)
    
   
   
    gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) #Convert it to gray colour for better visibility
    blurred_image1  = cv2.GaussianBlur(gray_image1, (15, 15), 0)
    canny_image1 = cv2.Canny(blurred_image1, 30, 100, 3)
    dilated_image1  = cv2.dilate(canny_image1, (1, 1), iterations=1)
    
    #_, threshold_gray_image1 = cv2.threshold(gray_image1, 170, 255, cv2.THRESH_BINARY)
        
    if k == 0:

# Detect object 
        contours, heirarchy = cv2.findContours(dilated_image1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)
    
        counter = 0
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if  area > 10000 and area < 20000:
                ellipse = cv2.fitEllipse(cnt)
                cv2.ellipse(image1,ellipse,(0,255,0),2)
                counter+=1
                k = 1
                print(counter)
            
    
    cv2.putText(image1, str(counter), (10,100), cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2,cv2.LINE_AA)
    cv2.imshow("Image1", image1)
    #cv2.imshow("threshold_gray_image1", threshold_gray_image1)
    #cv2.imshow("Image1", image1)
    #cv2.imshow("Frame", frame)
    #cv2.imshow("Belt", belt)
    #cv2.imshow("Gray_Frame", gray_frame)
    #cv2.imshow("Trashold", threshold)
    
    

    key = cv2.waitKey(1) # Wait 1 mlsec between each frame 
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
