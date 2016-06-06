import cv2
import numpy as np

from SimpleCV import Camera, Display, Image

#import sklearn as sk
from sklearn import *
#from scipy.sparse import *
#from scipy import *
from matplotlib import pylab

a=Image("L (25).png")

import sys
import glob
import errno

path = '/home/pi/Desktop/DEMO L5/*.png'   
files = glob.glob(path)   
for name in files: # 'file' is a builtin type, 'name' is a less-ambiguous variable name.
    try:
        with open(name) as f: # No need to specify 'r': this is the default.
            sys.stdout.write(f.read())
    except IOError as exc:
        if exc.errno != errno.EISDIR: # Do not fail if a directory is found, just ignore it.
            raise # Propagate other kinds of IOError.




