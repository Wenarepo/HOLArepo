from SimpleCV import Camera, Display, Image
import numpy as np
#import sklearn as sk
from sklearn import *
#from scipy.sparse import *
#from scipy import *
from matplotlib import pylab
from matplotlib import pyplot as plt
import cv2


c = Camera()

def foto(c):
    img = c.getImage()
    img.show()
    return img


img = cv2.imread('L5bc.png',0)

sobelx = cv2.Scharr(img,cv2.CV_64F,1,0)

plt.subplot(1,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,2,2),plt.imshow(sobelx,cmap = 'gray')
plt.title('Scharr'), plt.xticks([]), plt.yticks([])

plt.show()
