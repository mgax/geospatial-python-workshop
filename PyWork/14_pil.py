import os
from osgeo import ogr
import Image, ImageDraw

workspaceVector = "/home/instructor/Desktop/Data/Vector/";
daShapefile = workspaceVector + "02_Judete_centroid.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

layer = dataSource.GetLayer()
extent = layer.GetExtent();
print extent
xdist = extent[1] - extent[0]
ydist = extent[3] - extent[2]
print ydist
imgWidth = 800
imgHeight = 600

xratio = imgWidth/xdist
yratio = imgHeight/ydist

pixels = []
img = Image.new("RGB",(imgWidth,imgHeight), "white")
draw = ImageDraw.Draw(img)

for feature in layer:
    geom = feature.GetGeometryRef()
    px = int(imgWidth - ((extent[1] - geom.GetX()) * xratio))
    py = int((extent[3] - geom.GetY()) * yratio)

    draw.ellipse((px - 5 ,py - 5,px + 10,py + 10), fill = "red")




del draw
img.save("/home/instructor/Desktop/test.png")
