import os
from osgeo import ogr

workspaceVector = "/home/instructor/Desktop/Data/Vector/";

daShapefile = workspaceVector + "02_Judete_centroid.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

layer = dataSource.GetLayer()

layerDefinition = layer.GetLayerDefn()


print "Name  -  Type  Width  Precision"
for i in range(layerDefinition.GetFieldCount()):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()

    print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)