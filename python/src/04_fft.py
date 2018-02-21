import cv2
import numpy as np
from matplotlib import pyplot as plt

image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
renoir_02 = image_folder + '/Renoir/pierre-auguste-renoir.jpg'

img = cv2.imread(renoir_01,0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()