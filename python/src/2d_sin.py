import cv2
import numpy as np
from matplotlib import pyplot as plt

height = 128
width = 128

def cos2d(x,y):
    # wx = 3 * np.pi * 10;
    wx = 0;
    # wy = np.pi / 10;
    wy = 2 * np.pi * 10;
    return int(255 * (0.5 + np.sin(wx * x + wy * y)/2))

img = np.zeros((height, width), np.uint8)

for y in xrange(0, height):
    for x in xrange(0, width):
        img[y,x] = cos2d(x*1.0/width,y*1.0/height)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

import sys
if len(sys.argv) > 1:
    cv2.imwrite(sys.argv[1], img)

# plt.imshow(img, cmap = 'gray')
# plt.show()