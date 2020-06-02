import cv2
from matplotlib import pyplot

im = cv2.imread('image.jpg', 0)
lapl = cv2.Laplacian(im, -1)

pyplot.subplot(1, 2, 1)
pyplot.imshow(im)
pyplot.title('Original')

pyplot.subplot(1, 2, 2)
pyplot.imshow(lapl)
pyplot.title('Laplacian')

pyplot.show()





