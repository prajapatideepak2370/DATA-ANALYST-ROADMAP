import cv2
import os

folder = r"C:\Users\praja\Downloads\Resources\AI_project_image"
list_name = os.listdir(folder) #List of the all files and folders in the specified directory.---- 
# os.listdir()method is used to get the list of all files and directories in the specified directory.

for name in list_name: # iterating through the list of files and folders. (for loop is liye use kiya hai taki hum har ek file ko access kar sakein)
    img_path = os.path.join(folder, name)  # Joining the folder path with the file name to get the full path of the image file.
    img = cv2.imread(img_path)

    if img is None:
        print(f"❌ Could not load: {img_path}")
        continue  # skip this file if not a valid image

    re_img = cv2.resize(img, (500, 600))
    cv2.imshow("OS_top", re_img)
    cv2.waitKey(0)

cv2.destroyAllWindows()
