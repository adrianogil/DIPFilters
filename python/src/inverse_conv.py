from scipy import misc
import numpy as np
from numpy import fft
import cv2

image_folder = '../images/'
renoir_01 = image_folder + '/Renoir/Frau-mi-Sonnenschirm-by-Pierre-Auguste-Renoir-OSA351_1.jpg'
orig = misc.imread(renoir_01)
orig = cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY)
blur = misc.imread('conv_img.jpg')
orig_f = fft.fft2(orig)
blur_f = fft.fft2(blur)

kernel_f = blur_f / orig_f         # do the deconvolution
kernel = fft.ifft2(kernel_f)      # inverse Fourier transform
kernel = fft.fftshift(kernel)      # shift origin to center of image
kernel /= kernel.max()             # normalize gray levels
# kernel_range = kernel.max() - kernel.min()
# kernel = 255 * (kernel - kernel.min()) / kernel_range
# kernel = cv2.convertScaleAbs(kernel)
import pdb; pdb.set_trace() # Start debugger
cv2.imwrite('kernel.png', kernel)  # save reconstructed kernel
# misc.imsave('kernel.jpg', kernel)  # save reconstructed kernel
