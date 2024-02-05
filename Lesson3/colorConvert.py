
# Python program to explain cv2.cvtColor() method

import cv2

image = cv2.imread('C:/Users/HP/Desktop/JL/OpenCV/Lesson3/pika.png')
hsvImage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV )

cv2.imshow("window_name", image)
cv2.waitKey(0)
cv2.destroyAllWindows()