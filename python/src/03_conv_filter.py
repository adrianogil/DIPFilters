import cv2
import numpy as np
from matplotlib import pyplot as plt

image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
renoir_02 = image_folder + '/Renoir/pierre-auguste-renoir.jpg'

img = cv2.imread(renoir_01)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

custom_kernel = np.array([[1,1,1,1,1],
                          [1,0,0,0,1],
                          [1,0,1,0,1],
                          [1,0,0,0,1],
                          [1,1,1,1,1]]) * (1.0/13.0)
mean_kernel = np.ones((5,5),np.float32)/25
blur_kernel = cv2.getGaussianKernel(10, 1.2)
filtered_img = cv2.filter2D(img, -1, custom_kernel)

plt.subplot(121),plt.imshow(img, cmap = 'viridis')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(filtered_img, cmap = 'viridis')
plt.title('Filtered image'), plt.xticks([]), plt.yticks([])
plt.show()

import sys
if len(sys.argv) > 1:
    cv2.imwrite(sys.argv[1], filtered_img)