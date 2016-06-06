from SimpleCV import Camera, Display, Image
from sklearn import *
from matplotlib import pylab

import cv2
import numpy as np
from matplotlib import pyplot as plt
######### Se inicializan Valores ######### 
Rsl=0
Gsl=0
Bsl=0
Rsn=0
Gsn=0
Bsn=0
l=0
n=0
######### Carga y Filtro de la imagen #########
import sys
import glob
import errno

path = '/home/pi/Desktop/DEMO L5/DEMO5.1/*.png'   
files = glob.glob(path)   
for fn in xrange(len(files)):
    imgc = cv2.imread(files[fn],1)
    img = cv2.imread(files[fn],0)
    img = cv2.medianBlur(img,5)

    ######### Binarización de la imagen #########
    ret,th1 = cv2.threshold(img,60,255,cv2.THRESH_BINARY)

    B,G,R=cv2.split(imgc)

    ######### Identificacion, Mapeo y Promedio de Lunar/no Lunar  #########
    [fil,col] = img.shape

    for i in xrange(fil):
        for j in xrange(col):
            if th1[i,j]==0:
                Rsl=Rsl+R[i,j]
                Gsl=Gsl+G[i,j]
                Bsl=Bsl+B[i,j]
                l=l+1  
            else:
                Rsn=Rsn+R[i,j]
                Gsn=Gsn+G[i,j]
                Bsn=Bsn+B[i,j]
                n=n+1

    RPL=Rsl/l
    GPL=Gsl/l
    BPL=Bsl/l
    RPN=Rsn/n
    GPN=Gsn/n
    BPN=Bsn/n
    print [RPL,GPL,BPL,RPN,GPN,BPN]
    rho=np.matrix([[float(RPL)/float(RPN),float(RPL)/float(GPN),float(RPL)/float(BPL)],[float(GPL)/float(RPN),float(GPL)/float(GPN),float(BPL)/float(BPN)],[float(BPL)/float(RPN),float(BPL)/float(GPN),float(BPL)/float(BPN)]])
    print rho

    ######### Ploteo de la imagen #########
    titles = ['Imagen Original', 'Binarizada']
    images = [imgc, th1]

    for i in xrange(2):
        plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    plt.show()            
        
 



