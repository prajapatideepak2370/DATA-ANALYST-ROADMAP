#now we show multiple photos in one window
import cv2
import numpy as np
import os # this lib is in-built lib in python to work with files and directories

img = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png")
re_img = cv2.resize(img, (300,300))

#image having a different no. of RGB arrays stack to get merging fo array
H = np.hstack([re_img, re_img, re_img]) #we use hstack for horizontal stacking of images to show multiple images in one window.
V = np.vstack([H, H, H]) #we use vstack for vertical stacking of images to show multiple images in one window.

cv2.imshow("arr", V)
cv2.waitKey(0)
cv2.destroyAllWindows()