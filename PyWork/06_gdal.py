from osgeo import gdal

workspaceRater = "/home/instructor/Desktop/Data/Landsat/";
inputFile = workspaceRater + 'B1-L-34-036.tif'
#inputFile = workspaceRater + 'L-34-035.tif'

dataset = gdal.Open(inputFile)
print "Metadata:", dataset.GetMetadata()
print "Bands:", dataset.RasterCount

print "Cols:", dataset.RasterXSize

#geoTrans = dataset.GetGeoTransform()
#ulX = geoTrans[0]
#ulY = geoTrans[3]
#xRez = geoTrans[1]
#yRez = geoTrans[5]
#rtnX = geoTrans[2] # rotation
#rtnY = geoTrans[4]

#print ulX, ulY
#print xRez, yRez

srcBand = dataset.GetRasterBand(1)
print "No Data Value:", srcBand.GetNoDataValue()


# close dataset
dataset = None
