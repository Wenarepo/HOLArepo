from SimpleCV import Camera, Display, Image
import numpy as N
from matplotlib import pylab

c = Camera()

def foto(c):
    img = c.getImage()
    img.show()
    return img

#img.show()

#img2=N.array(img)

#img2=img.getNumpy()

a=foto(c)
##a=Image("hola3.png")
imgGray=a.grayscale()
imgGray.save("hola4Gray.png")
a.save("hola4.png")

def histograma(hist):
    
    hist=imgGray.histogram()
##    hist.save("hola4Hist.txt")
    pylab.plot(hist)
    pylab.draw()
    pylab.pause(0.0001)


b=histograma(imgGray)
