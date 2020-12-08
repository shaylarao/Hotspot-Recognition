# Shayla Rao
# Color detection of thermal image of a fire using OpenCV

# Imported cv2 and numpy
import cv2
import numpy as np

# Getting thermal image
img = cv2.imread( 'C:/Users/Shayla/Documents/Capstone_Class/image_proc/fire.jpg')

# Converting image colors from BGR format to HSV format
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defining lower and upper HSV ranges of colors
lower_red = np.array([161,155,84])
upper_red = np.array([179,255,255])

lower_red2 = np.array([161,155,84])
upper_red2 = np.array([161,155,84])

lower_orange = np.array([1,190,200])
upper_orange = np.array([18,255,255])

lower_yellow = np.array([20,100,100])
upper_yellow = np.array([30,255,255])

# Defining masks for colors using lower and upper ranges
red_mask = cv2.inRange(hsv, lower_red, upper_red)
red2_mask = cv2.inRange(hsv, lower_red2, upper_red2)
orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)
yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# Creating a mask with all colors extracted
mask = red_mask+red2_mask+orange_mask+yellow_mask

# Creating mask containing just the colors of the fire
colored_mask = cv2.bitwise_or(img, img, mask=mask)

# Outputting original image, image with white mask, and, image with colored mask
cv2.imshow('image', img)
cv2.imshow('mask', mask)
cv2.imshow('colored_mask', colored_mask)

# Handles windowing events and destroys all windows created
cv2.waitKey(0)
cv2.destroyAllWindows()
