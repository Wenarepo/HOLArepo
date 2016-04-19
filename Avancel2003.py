Python 2.7.9 (default, Mar  8 2015, 00:52:26) 
[GCC 4.9.2] on linux2
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> a.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x7576bbe8)>
>>> (R,G,B)=a.splitChannels(False)
>>> R.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x6d113f30)>
>>> G.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x6d113f08)>
>>> B.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x6d0e4e68)>
>>> G.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x7576b580)>
>>> R.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x7576b5f8)>
>>> G.show()
<SimpleCV.Display Object resolution:((640, 480)), Image Resolution: (640, 480) at memory location: (0x6d113f08)>
>>> b=histograma(G)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    b=histograma(G)
  File "/home/pi/Desktop/cosa4.py", line 26, in histograma
    hist=imgGray.histogram()
NameError: global name 'imgGray' is not defined
>>> b=histograma(G)

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    b=histograma(G)
  File "/home/pi/Desktop/cosa4.py", line 26, in histograma
    hist=hist.histogram()
NameError: global name 'imgGray' is not defined
>>> 
