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

# Output dtype = cv2.CV_8U
sobelx8u = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=3)
# Output dtype = cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U 
sobelx64f = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
abs_sobel64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobel64f)

plt.subplot(1,3,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()