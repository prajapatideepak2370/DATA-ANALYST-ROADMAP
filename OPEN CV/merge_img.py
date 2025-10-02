import cv2

x = cv2.imread(r"C:\Users\praja\Downloads\Resources\CV_photo.png")
x = cv2.resize(x, (500,600))
img = cv2.imread(r"C:\Users\praja\Downloads\Resources\AI_project_image\ChatGPT Image Aug 16, 2025, 06_08_56 PM.png")
img = cv2.resize(img, (500,600))


#cv2.addWeighted(src1, alpha, src2, beta, gamma)
mer_img = cv2.addWeighted(x, 1, img, 1, 1)

# mer_img = cv2.subtract(img , x)
cv2.imshow("merge", mer_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
