import cv2
img1 = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png")
img1 = cv2.resize(img1, (500,600))

# Adding text to image using cv2.putText() function
txt = cv2.putText(img = img1,
                  text = "Hello Deepak Here", org= (60,70),
                  fontFace = cv2.FONT_HERSHEY_COMPLEX,
                  fontScale = 1,
                  color = (235,34,156),
                  thickness = 2,
                  lineType = cv2.LINE_AA,
                  bottomLeftOrigin = False) #bottomLeftOrigin = False means the origin is at the top-left corner of the image
                                            

txt = cv2.putText(img = img1,
                  text = "Hello Deepak Here", org= (60,80),
                  fontFace = cv2.FONT_HERSHEY_COMPLEX,
                  fontScale = 1,
                  color = (235,34,156),
                  thickness = 2,
                  lineType = cv2.LINE_AA,
                  bottomLeftOrigin = True) # and if we want to represent water image then we can use bottomLeftOrigin = True

cv2.imshow("text", txt)
cv2.waitKey(0)
cv2.destroyAllWindows()