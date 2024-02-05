import cv2
import os

# change the path to where you wish to save the image
path = "C:/Users/HP/Desktop/JL/OpenCV/Lesson1/lesson2/"

img = cv2.imread("C:/Users/HP/Desktop/JL/OpenCV/Lesson1/pika.png", 0)
cv2.imshow("Pikachu in Black and White", img)

# write image to this directory
cv2.imwrite("blackandWhite.png", img)

print("Successfully Saved")

cv2.waitKey(delay = 5000)

os.chdir(path)

cv2.destroyAllWindows()