from SimpleCV import Camera, Display, Image
import numpy as N
#import sklearn as sk
from sklearn import *
#from scipy.sparse import *
#from scipy import *
from matplotlib import pylab
import cv2

#from sklearn.utils.validation import check_arrays
#from skimage import data
#from skimage import filters # 




c = Camera()

def foto(c):
    img = c.getImage()
    img.show()
    return img


#a=foto(c)


a=Image("hola5Gray.png")
imgGray=a
##imgGray=a.grayscale()
#imgGray.save("hola42AGray.png")
#a.save("holaA42.png")

def histograma(hist):
    
    hist=hist.histogram(255)
##    hist.save("hola4Hist.txt")
    pylab.plot(hist)
    pylab.draw()
    pylab.pause(0.0001)


##b=histograma(imgGray)

b = imgGray.binarize(50)
ainv = imgGray.binarize(100)
a=ainv.__invert__()

##b.show()
##pylab.figure(1)
##pylab.subplot(311), a.show(), pylab.title('Imagen Original')
##a.show()

##histograma(imgGray)
##pylab.subplot(312), b.show(), pylab.title('Imagen Invertida')
##b.show()
a.save("a.png")
b.save("b.png")
ainv.save("ainv.png")

orig = cv2.imread("hola5Gray.png")
ainv = cv2.imread("ainv.png")
h=imgGray.histogram(255)
a = cv2.imread("a.png")
b = cv2.imread("b.png")
c=cv2.add(a,b)

pylab.subplot(2,2,1)
pylab.imshow(orig)
pylab.title('Imagen Original')

pylab.subplot(2,2,2)
pylab.imshow(a)
pylab.title('Im Bin(100) e invertida')

pylab.subplot(2,2,3)
pylab.imshow(b)
pylab.title('Imagen Binarizada (50)')

pylab.subplot(2,2,4)
pylab.imshow(c)
pylab.title('Imagen Segmentada Sustraida')

pylab.show()












   # histResta=histB-histA
    

