from SimpleCV import Camera, Display, Image
import numpy as N
#import sklearn as sk
from sklearn import *
#from scipy.sparse import *
#from scipy import *
from matplotlib import pylab

#from sklearn.utils.validation import check_arrays
#from skimage import data
#from skimage import filters # 




c = Camera()

def foto(c):
    img = c.getImage()
    img.show()
    return img


#a=foto(c)


a=Image("hola42AGray.png")
imgGray=a.grayscale()
#imgGray.save("hola42AGray.png")
#a.save("holaA42.png")

def histograma(hist):
    
    hist=hist.histogram(255)
##    hist.save("hola4Hist.txt")
    pylab.plot(hist)
    pylab.draw()
    pylab.pause(0.0001)


b=histograma(imgGray)

(R,G,B)=a.splitChannels(False)
##B.show()
##b=histograma(G)


def histogramac(histc):
    
    histc=histc.histogram(255)
    B.show()
    pylab.plot(histc)
    pylab.draw()
    pylab.pause(0.0001)

##b=histogramac(B)

### ACTIVIDAD 2
### La mascara para la letra se genera a partir del umbral 50 del histograma:
holaBin = imgGray.binarize(50)
#holaBin.show()

### La mascara para la cuadricula, lo mejor posible con la funcion binarize seria en 135:
#holaBin = imgGray.binarize(135)
#holaBin.show()

d=ImageOps.invert(holaBin)
d.show()



#lb = preprocessing.LabelBinarizer()
#lb.fit([1, 2])
#array([1, 2])




#holaMasc = holaBin*a
#holaMasc.show()

#def restaHist(hist):
 #   histA=hist.histogram(100)
  #  histB=hist.histogram(255)

   # histResta=histB-histA
    

