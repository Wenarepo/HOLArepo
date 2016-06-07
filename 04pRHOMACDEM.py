from SimpleCV import Camera, Display, Image
from sklearn import *
from matplotlib import pylab

import cv2
import numpy as np
from matplotlib import pyplot as plt

##c = Camera()
##
##def foto(c):
##    img = c.getImage()
####    img.show()
##    return img
##
##a=foto(c)
##a.save("foto.png")

######### Se inicializan Valores ######### 
Rsl=0
Gsl=0
Bsl=0
Rsn=0
Gsn=0
Bsn=0
l=0
n=0
t=1      ## Tamano de M 
######### Carga y Filtro de la imagen #########
path='L (35).png'
Fcom=1
im = cv2.imread(path,0)
[fil,col] = im.shape
fil=fil/Fcom
col=col/Fcom
a=Image(path)
b=a.resize(col,fil)
b.save("IMT.png")

path='IMT.png'

imgc = cv2.imread(path,1)
img = cv2.imread(path,0)
B,G,R=cv2.split(imgc)
R=R+1.0
G=G+1.0
B=B+1.0
img = cv2.medianBlur(img,5)
 
######### Identificacion, Mapeo y Promedio de Lunar/no Lunar  #########
[fil,col] = img.shape
P=np.zeros((fil,col))
RTVv=np.zeros((fil,col))
RTHv=np.zeros((fil,col))
RPRM=np.load('PRM.npy')
print "Carga de Rho Referencial"

Gm=np.min(G)
Th=Gm+10 

for i in xrange(t+1,fil-t):
    for j in xrange(t+1,col-t):
        RRV=np.matrix([float(R[i,j-t])/float(R[i,j+t]),float(R[i,j-t])/float(G[i,j+t]),float(R[i,j-t])/float(B[i,j+t]),float(G[i,j-t])/float(R[i,j+t]),float(G[i,j-t])/float(G[i,j+t]),float(G[i,j-t])/float(B[i,j+t]),float(B[i,j-t])/float(R[i,j+t]),float(B[i,j-t])/float(G[i,j+t]),float(B[i,j-t])/float(B[i,j+t])])
        RRH=np.matrix([float(R[t-1,j])/float(R[i+t,j]),float(R[i-t,j])/float(G[i+t,j]),float(R[i-t,j])/float(B[i+t,j]),float(G[i-t,j])/float(R[i+t,j]),float(G[i-t,j])/float(G[i+t,j]),float(G[i-t,j])/float(B[i+t,j]),float(B[i-t,j])/float(R[i+t,j]),float(B[i-t,j])/float(G[i+t,j]),float(B[i-t,j])/float(B[i+t,j])])
        RTV=np.linalg.norm(RRV-RPRM)
        RTH=np.linalg.norm(RRH-RPRM)
        
        if G[i,j]<=Th:
            print "              Lunar"
            print RTV
            print RTH
            RTVv[i,j]=RTV
            RTHv[i,j]=RTH
        
print "Calculando Borde"

for i in xrange(t+1,fil-t):
    for j in xrange(t+1,col-t):
        RRV=np.matrix([float(R[i,j-t])/float(R[i,j+t]),float(R[i,j-t])/float(G[i,j+t]),float(R[i,j-t])/float(B[i,j+t]),float(G[i,j-t])/float(R[i,j+t]),float(G[i,j-t])/float(G[i,j+t]),float(G[i,j-t])/float(B[i,j+t]),float(B[i,j-t])/float(R[i,j+t]),float(B[i,j-t])/float(G[i,j+t]),float(B[i,j-t])/float(B[i,j+t])])
        RRH=np.matrix([float(R[t-1,j])/float(R[i+t,j]),float(R[i-t,j])/float(G[i+t,j]),float(R[i-t,j])/float(B[i+t,j]),float(G[i-t,j])/float(R[i+t,j]),float(G[i-t,j])/float(G[i+t,j]),float(G[i-t,j])/float(B[i+t,j]),float(B[i-t,j])/float(R[i+t,j]),float(B[i-t,j])/float(G[i+t,j]),float(B[i-t,j])/float(B[i+t,j])])
        RTV=np.linalg.norm(RRV-RPRM)
        RTH=np.linalg.norm(RRH-RPRM)

        UMv=np.max(RTVv)
        UMv=UMv*0.8
        UMh=np.max(RTHv)
        UMh=UMh*0.8
        if RTV>=UMv:
            P[i,j]=255
        if RTH>=UMh:
            P[i,j]=255
        else:
            P[i,j]=0

######### Ploteo de la imagen #########
titles = ['Imagen Original', 'Mapa de bordes']
images = [imgc, P]

for i in xrange(2):
    plt.subplot(1,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()            
 



