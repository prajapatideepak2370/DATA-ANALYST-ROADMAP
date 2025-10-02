#now study about imread function flags (-1,0,1)  [ 1 :- imread_color, 0 :- imread_grayscale, -1 :- imread_unchanged(default)]
import cv2

# -1 means to load the image as is (including alpha channel if present)
img1 = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png", -1)
img1 = cv2.resize(img1, (500,600))
# 0 means to load the image in grayscale mode
img2 = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png", 0)
img2 = cv2.resize(img2, (500,600))
# 1 means to load the image in color mode (default)
img3 = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png", 1)
img3 = cv2.resize(img3, (500,600))
cv2.imshow("Flags", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()