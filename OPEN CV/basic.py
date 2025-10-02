import cv2 
import numpy as np
# first wr studey about image how to read and how to display it..------let's work on it 
img = cv2.imread("C:\\Users\\praja\\Downloads\\Resources\\AI_project_image\\CareerSetu_AI_Architecture.png") 
# Provide the correct path of image file in your system that you want to display 
print(img)
reimg = cv2.resize(img, (700,500)) # Resize the image to fit in the window if needed

# cv2.imshow("yoyi",reimg) # Display the image in a window named "yoyi"
# cv2.imshow("yoyi2",img) # Display multiple windows with the same image if 

cv2.waitKey(0) # Wait for 8000 milliseconds (8 seconds) before closing the window or 0 means wait indefinitely until a key is pressed
cv2.destroyAllWindows() # Close all OpenCV windows after the wait time is over 

