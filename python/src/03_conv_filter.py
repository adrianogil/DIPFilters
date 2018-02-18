import cv2
import numpy as np
from matplotlib import pyplot as plt
 
image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
renoir_02 = image_folder + '/Renoir/pierre-auguste-renoir.jpg'

img = cv2.imread(renoir_01)

mean_kernel = np.ones((5,5),np.float32)/25
blur_kernel = cv2.getGaussianKernel(10, 1.2)
filtered_img = cv2.filter2D(img, -1, blur_kernel)

cv2.imshow('Filtered image',filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()