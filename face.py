import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")




img = cv2.imread("madhvi.jpg")
gray_img  = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img , scaleFactor = 1.05 , minNeighbors = 5)

for x , y , wid , hei in faces:
    img = cv2.rectangle(img , (x,y) , (x+wid , y+hei) , (0 , 255 , 0) , 3)

resized = cv2.resize(img , (int(img.shape[1]/2) , int(img.shape[0]/2)))

cv2.imshow("YO" , resized)
cv2.waitKey(0)
cv2.destroyAllWindows()