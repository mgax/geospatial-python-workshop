import os
from osgeo import ogr

workspaceVector = "/home/instructor/Desktop/Data/Vector/";

daShapefile = workspaceVector + "02_Judete_centroid.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

layer = dataSource.GetLayer()

for feature in layer:
    geom = feature.GetGeometryRef()
    print geom.Centroid().ExportToWkt()