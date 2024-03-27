import cv2
import numpy as np

image = cv2.imread('F:/Computer Vision/Image/picture11.png')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gradient_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.magnitude(gradient_x, gradient_y)
gradient_magnitude_normalized = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
gradient_x = cv2.convertScaleAbs(gradient_x)
gradient_y = cv2.convertScaleAbs(gradient_y)
sharpened_image = cv2.addWeighted(gray_image, 1, gradient_magnitude_normalized, 1, 0)
cv2.imshow('Original Image', gray_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
