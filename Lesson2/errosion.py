##### Erosion of an image, corners are trimmed in erosion

import cv2
import numpy as np
  
img = cv2.imread("pika.png",1)
cv2.imshow("Original Image", img) 
  

# kernel is used for erosion as an input
kernel = np.ones((5, 5), np.uint8)
print(kernel)
image = cv2.imread("pika.png", 1)
image = cv2.erode(image, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()