from SimpleCV import Camera, Display, Image
#import numpy as N
#import sklearn as sk
from sklearn import *
#from scipy.sparse import *
#from scipy import *
from matplotlib import pylab


import cv2
import numpy as np
from matplotlib import pyplot as plt

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

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('hola5Gray.png',0)
img = cv2.medianBlur(img,5)

ret,th1 = cv2.threshold(img,60,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in xrange(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()





