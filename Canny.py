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
edges = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()
