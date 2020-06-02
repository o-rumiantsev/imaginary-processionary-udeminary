from PIL import Image
from numpy import *
from matplotlib import pyplot

im = array(Image.open('image.jpg').convert('L'))
pyplot.gray()

neg_im = 255 - im
contr_im = 255.0 * (im / 255) ** 2

pyplot.subplot(1, 3, 1)
pyplot.imshow(im)
pyplot.title('Original')

pyplot.subplot(1, 3, 2)
pyplot.imshow(contr_im)
pyplot.title('Contrast')

pyplot.subplot(1, 3, 3)
pyplot.imshow(neg_im)
pyplot.title('Negative')

pyplot.show()


