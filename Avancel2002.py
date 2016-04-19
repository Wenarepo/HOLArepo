Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
a=Image("hola3.png")
imgGray=a.grayscale()
hist=imgGray.histogram()

pylab.plot(hist)
pylab.draw()
pylab.pause(0.0001)
