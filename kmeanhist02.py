from __future__ import print_function
from SimpleCV import Camera, Display, Image

##import arcpy
##arcpy.CheckOutExtension("Spatial")

import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.segmentation import quickshift

# The input 4-band NAIP image
river = r'C:\path\to\naip_image.tif'

# Convert image to numpy array
img = io.imread(river)

# Run the quick shift segmentation
segments = quickshift(img, kernel_size=3, convert2lab=False, max_dist=6, ratio=0.5)
print("Quickshift number of segments: %d" % len(np.unique(segments)))

# View the segments via Python
plt.imshow(segments)

### Get raster metrics for coordinate info
##myRaster = arcpy.sa.Raster(river)
##
### Lower left coordinate of block (in map units)
##mx = myRaster.extent.XMin
##my = myRaster.extent.YMin
##sr = myRaster.spatialReference
##
### Note the use of arcpy to convert numpy array to raster
##seg = arcpy.NumPyArrayToRaster(segments, arcpy.Point(mx, my),
##                               myRaster.meanCellWidth,
##                               myRaster.meanCellHeight)
##
##outRaster = r'C:\path\to\segments.tif'
##seg_temp = seg.save(outRaster)
##arcpy.DefineProjection_management(outRaster, sr)
##
### Calculate NDVI from bands 4 and 3
##b4 = arcpy.sa.Raster(r'C:\path\to\naip_image.tif\Band_4')
##b3 = arcpy.sa.Raster(r'C:\path\to\naip_image.tif\Band_3')
##ndvi = arcpy.sa.Float(b4-b3) / arcpy.sa.Float(b4+b3)
##
### Extract NDVI values based on image object boundaries
##zones = arcpy.sa.ZonalStatistics(outRaster, "VALUE", ndvi, "MEAN")
##zones.save(r'C:\path\to\zones.tif')
##
### Classify the segments based on NDVI values
##binary = arcpy.sa.Con(zones < 20, 1, 0)
##binary.save(r'C:\path\to\classified_image_objects.tif')
