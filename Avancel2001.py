Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> foto(c)
<SimpleCV.Image Object size:(640, 480), filename: (None), at memory location: (0x756e9530)>
>>> 
>>> foto(c)
<SimpleCV.Image Object size:(640, 480), filename: (None), at memory location: (0x756e9bc0)>
>>> foto(c)
<SimpleCV.Image Object size:(640, 480), filename: (None), at memory location: (0x6d6e43f0)>
>>> a=foto(c)
>>> a.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x756e9788)>
>>> a.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x6d6e4530)>
>>> a.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x756e9788)>
>>> b=foto(c)
>>> a.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x756e95a8)>
>>> a.save("hola1.png")
1
>>> b.save("hola2.png")
1
>>> imgGray=a.greyscale()

Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    imgGray=a.greyscale()
AttributeError: Image instance has no attribute 'greyscale'
>>> imgGray=hola1.greyscale()

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    imgGray=hola1.greyscale()
NameError: name 'hola1' is not defined
>>> imgGray=a.grayscale()
>>> hist=imgGray.histogram()
>>> imgGray.save("hola1Gray")

Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    imgGray.save("hola1Gray")
  File "/Code/SimpleCV/SimpleCV/ImageClass.py", line 2382, in save
    cv.SaveImage(filename, saveimg.getBitmap())
error: could not find a writer for the specified extension
>>> imgGray.save("hola1Gray.png")
1
>>> plot(histogram)

Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    plot(histogram)
NameError: name 'plot' is not defined
>>> imgGray=a.grayscale()
>>> hist=imgGray.histogram()
>>> plot(hist)

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    plot(hist)
NameError: name 'plot' is not defined
>>> plot(histogram)

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    plot(histogram)
NameError: name 'plot' is not defined
>>> 
