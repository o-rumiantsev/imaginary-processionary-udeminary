from PIL import Image, ImageFilter
from matplotlib import pyplot

im = Image.open('image.jpg')
pyplot.figure(figsize = (15, 15))

pyplot.gray()

pyplot.subplot(3, 3, 1)
pyplot.imshow(im)
pyplot.title('Original')

pyplot.subplot(3, 3, 2)
pyplot.imshow(im.filter(ImageFilter.CONTOUR))
pyplot.title('Contour')

pyplot.subplot(3, 3, 3)
pyplot.imshow(im.filter(ImageFilter.DETAIL))
pyplot.title('Detail')

pyplot.subplot(3, 3, 4)
pyplot.imshow(im.filter(ImageFilter.EMBOSS))
pyplot.title('Emboss')

pyplot.subplot(3, 3, 5)
pyplot.imshow(im.filter(ImageFilter.SMOOTH))
pyplot.title('Smooth')

pyplot.subplot(3, 3, 6)
pyplot.imshow(im.filter(ImageFilter.SMOOTH_MORE))
pyplot.title('Smooth more')

pyplot.subplot(3, 3, 7)
pyplot.imshow(im.filter(ImageFilter.EDGE_ENHANCE))
pyplot.title('Edge enhance')

# Custom

size = (3, 3)
kernel = [
  1,   0, -1, 
  0, 0.5,  0,
 -1,   0,  1
]
k1 = ImageFilter.Kernel(size, kernel, offset = 0)
pyplot.subplot(3, 3, 8)
pyplot.imshow(im.filter(k1))
pyplot.title('Custom 1')

size = (5, 5)
kernel = [
  1,  1,  1,  1,  1,
  1,  1,  1,  1,  0,
  1,  1,  1,  0, -1,
  1,  1,  0, -1, -1,
  1,  0, -1, -1, -1
]
k2 = ImageFilter.Kernel(size, kernel, offset = 0)
pyplot.subplot(3, 3, 9)
pyplot.imshow(im.filter(k2))
pyplot.title('Custom 2')

pyplot.show()
