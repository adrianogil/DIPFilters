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

blur_kernel = cv2.getGaussianKernel(20, 1.2)
filtered_img = cv2.filter2D(img, -1, blur_kernel)
filtered_img = cv2.filter2D(filtered_img, -1, blur_kernel)
filtered_f = np.fft.fft2(filtered_img)
filtered_fshift = np.fft.fftshift(filtered_f)
filtered_magnitude_spectrum = 20*np.log(np.abs(filtered_fshift))

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(filtered_img, cmap = 'gray')
plt.title('Blur Image'), plt.xticks([]), plt.yticks([])
plt.subplot(224),plt.imshow(filtered_magnitude_spectrum, cmap = 'gray')
plt.title('Blur Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()