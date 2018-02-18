import cv2
import numpy as np
from matplotlib import pyplot as plt
 
image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
renoir_02 = image_folder + '/Renoir/pierre-auguste-renoir.jpg'

img = cv2.imread(renoir_02)
cv2.imshow('Test image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()