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
a = imgGray.binarize(100)
a=a.__invert__()

b.show()
##pylab.figure(1)
##pylab.subplot(311), a.show(), pylab.title('Imagen Original')
##a.show()

##histograma(imgGray)
##pylab.subplot(312), b.show(), pylab.title('Imagen Invertida')
##b.show()
a.save("a.png")
b.save("b.png")

a = cv2.imread("a.png")
b = cv2.imread("b.png")
c=cv2.add(a,b)

pylab.imshow(c)
pylab.show()





   # histResta=histB-histA
    

