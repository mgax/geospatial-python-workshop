from osgeo import gdal

workspaceRater = "/home/instructor/Desktop/Data/Landsat/";

inputFile = workspaceRater + 'L-34-035.tif'

dataset = gdal.Open(inputFile)


print "[ RASTER BAND COUNT ]: ", dataset.RasterCount
for band in range( dataset.RasterCount ):
    band += 1
    print "[ GETTING BAND ]: ", band
    srcband = dataset.GetRasterBand(band)
    if srcband is None:
        continue

    stats = srcband.GetStatistics( True, True )
    if stats is None:
        continue

    print "[ STATS ] =  Minimum=%.3f, Maximum=%.3f, Mean=%.3f, StdDev=%.3f" % ( \
                stats[0], stats[1], stats[2], stats[3] )

# close dataset
dataset = None
