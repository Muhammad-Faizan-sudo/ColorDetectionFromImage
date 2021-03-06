# -*- coding: utf-8 -*-
"""colorDetectionUsingOpenCv

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ks8AYZBtkStLQ4qnuBTvElMYRKe5IUOR
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/content/rose.JPG")

plt.figure(figsize=(20,8))
plt.imshow(img)

#conversion of BRG2RGB
grid_RGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(20,8))
plt.imshow(grid_RGB)

#conversion of RGB2HSV
grid_HSV = cv2.cvtColor(grid_RGB,cv2.COLOR_RGB2HSV)

#lOWER AND UPPER HSV range OF RED colour because i have to detect only red color from this image
lower = np.array( [0,150,50])
upper = np.array([10,255,255])

mask = cv2.inRange(grid_HSV,lower,upper)

plt.figure(figsize=(20,8))
plt.imshow(mask)

res = cv2.bitwise_and(grid_RGB,grid_HSV,mask=mask )

plt.figure(figsize=(20,8))
plt.imshow(res)