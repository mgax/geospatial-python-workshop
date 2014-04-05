import pyproj

import os
from osgeo import ogr

workspaceVector = "/home/instructor/Desktop/Data/Vector/";

daShapefile = workspaceVector + "02_Judete_centroid.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

layer = dataSource.GetLayer()
p1 = pyproj.Proj(init='epsg:31700')
p2 = pyproj.Proj(init='epsg:4326')

for feature in layer:
    geom = feature.GetGeometryRef()
    x1, y1 = geom.GetX(), geom.GetY()
    print x1, y1
    x2, y2 = pyproj.transform(p1,p2,x1,y1)
    print x2, y2
    geom = None

p1 = None
p2 = None
