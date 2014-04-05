from osgeo import gdalnumeric

workspaceRater = "/home/instructor/Desktop/Data/Landsat/";
#inputFile = workspaceRater + 'B1-L-34-036.tif'
inputFile = workspaceRater + 'L-34-035.tif'

srcArray = gdalnumeric.LoadFile(inputFile)
print "Metadata:", srcArray.shape

band1 = srcArray[0]

gdalnumeric.SaveArray (band1, "/home/instructor/Desktop/band1.jpg", format = "JPEG")

# close dataset
srcArray = None

