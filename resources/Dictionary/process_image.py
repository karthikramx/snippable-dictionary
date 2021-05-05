import cv2
import numpy as np

image = cv2.imread("img.png",1)
image = cv2.flip(image,1)
image = cv2.flip(image,0)
image = cv2.flip(image,1)

cv2.imshow("qw",image)
cv2.imwrite('ocr.png', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
