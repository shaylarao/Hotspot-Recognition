import cv2
import numpy as np

img = cv2.imread( 'C:/Users/Shayla/Documents/Capstone_Class/image_proc/new_shapes.png')
#window_name = 'image'
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower = np.array([161,155,84])
upper = np.array([179,255,255])

mask = cv2.inRange(hsv, lower, upper)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
