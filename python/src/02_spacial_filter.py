import cv2
import numpy as np
from matplotlib import pyplot as plt

from sympy import *

image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
renoir_02 = image_folder + '/Renoir/pierre-auguste-renoir.jpg'

img = cv2.imread(renoir_01)



gray_scale_transform_matrix = (1.0/3.0) * np.array(
                                [[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]]
                              );

sepia_transform_matrix = np.array(
                             [[0.272, 0.534, 0.131],
                              [0.349, 0.686, 0.168],
                              [0.393, 0.769, 0.189]]
                              );

def show_RGB_values_after_spatial_transform(transform_matrix):

    R = Symbol('R')
    G = Symbol('G')
    B = Symbol('B')

    rgb_array = Matrix(
                    [[R],
                     [G],
                     [B]]
                        );

    new_rgb_values = transform_matrix * rgb_array

    print("R = " + str(new_rgb_values[0]))
    print("G = " + str(new_rgb_values[1]))
    print("B = " + str(new_rgb_values[2]))


show_RGB_values_after_spatial_transform(sepia_transform_matrix)
sepia_img = cv2.transform(img, sepia_transform_matrix)

plt.subplot(121),plt.imshow(img)
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(sepia_img)
plt.title('Sepia'), plt.xticks([]), plt.yticks([])
plt.show()

import sys
if len(sys.argv) > 1:
    cv2.imwrite(sys.argv[1], sepia_img)