import cv2
import numpy as np

img = cv2.imread( 'C:/Users/Shayla/Documents/Capstone_Class/image_proc/fire.jpg')
#window_name = 'image'
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([161,155,84])
upper_red = np.array([179,255,255])

lower_red2 = np.array([161,155,84])
upper_red2 = np.array([161,155,84])

lower_orange = np.array([1,190,200])
upper_orange = np.array([18,255,255])

lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])

red_mask = cv2.inRange(hsv, lower_red, upper_red)
red2_mask = cv2.inRange(hsv, lower_red2, upper_red2)
orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

mask = red_mask+red2_mask+orange_mask+yellow_mask

cv2.imshow('image', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()

#multiple colors: https://stackoverflow.com/questions/24892615/tracking-multiple-objects-by-color-opencv-2-x
