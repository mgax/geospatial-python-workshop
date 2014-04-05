import os
from osgeo import ogr

workspaceVector = "/home/instructor/Desktop/Data/Vector/";

daShapefile = workspaceVector + "02_Judete.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')

dataSource = driver.Open(daShapefile, 0) # 0 means read-only. 1 means writeable.

# Check to see if shapefile is found.
if dataSource is None:
    print 'Could not open %s' % (daShapefile)
else:
    print 'Opened %s' % (daShapefile)
    layer = dataSource.GetLayer()
    featureCount = layer.GetFeatureCount()
    print "Number of features in %s: %d" % (os.path.basename(daShapefile),featureCount)
    
    for feature in layer:
        print feature.GetField("JUD_CODE")