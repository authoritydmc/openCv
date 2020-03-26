#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 15:03:55 2020

@author: beast
"""

import cv2
import numpy as np
print("Starting")
img=np.ones((1024,768,3))
img2=np.zeros((1024,768,3))


is_drawing=False
ix,iy=-1,-1


def draw_rectangle(event,x,y,flags,params):
    global ix,iy,is_drawing
    global img2,img
    if event==cv2.EVENT_LBUTTONDOWN:
        img2=img.copy()
        is_drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if is_drawing:
            img2=img.copy()
            cv2.rectangle(img2,(ix,iy),(x,y),(0,0,0),1)
    elif event==cv2.EVENT_LBUTTONUP:
        is_drawing=False
        cv2.rectangle(img,(ix,iy),(x,y),(0,0,255),-1)
        


cv2.namedWindow(winname="img")
cv2.setMouseCallback("img",draw_rectangle)


while True:
    if is_drawing==False:
        cv2.imshow("img",img)
        # print("original_img")
    else:
        cv2.imshow("img",img2)
        print("draw_canvas")
    if cv2.waitKey(1) & 0xFF==27:
        print("Exiting")
        break
    
cv2.destroyAllWindows()