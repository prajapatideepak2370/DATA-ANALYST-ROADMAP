import cv2

x = cv2.imread(r"C:\Users\praja\Downloads\Resources\CV_photo.png")
x = cv2.resize(x, (500,600))

x = cv2.putText(img=x,
                text= "DOG FACE",
                fontFace= 2,
                org= (100,90),
                fontScale=1,
                color= (83,63,172),
                thickness= 2,
                bottomLeftOrigin= False)

#now make a line on image using cv2.line() function 
y = cv2.line(img = x, 
             pt1 = (98,97), 
             pt2 = (370,97),
             color=(0,255,0),
             thickness= 4,
             lineType= cv2.LINE_AA)

#now make a rectancle on image using cv2.rectangle() function 
z = cv2.rectangle(img = x,
                  pt1 = (87,97), # pt1 is a coordinate of (x1, y1)
                  pt2 = (400,340), # pt2 is a coordinate of (x2, y2)
                  color = (255,0,0),
                  thickness = 3,
                  lineType = cv2.LINE_AA)

#now make a circle on image using cv2.circle() function
c = cv2.circle(img = x, 
               center= (245,230),
               radius= 150,
               color=(0,255,0),
               thickness= 2,
               lineType= 4)

cv2.imshow("imagge", c)
cv2.waitKey(0)
cv2.destroyAllWindows()