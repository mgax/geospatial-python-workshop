import fiona
workspaceVector = "/home/instructor/Desktop/Data/Vector/";
daShapefile = workspaceVector + "02_Judete_centroid.shp"

with fiona.open(daShapefile, 'r') as source:
    meta = source.meta
    print meta['schema']
    print meta['schema']['geometry']

    #print source.crs
    #for f in source.filter(bbox=(360000,630000,424000,687000)):
    #    print f['properties']['JUD_CODE']
    #    print f['geometry']['coordinates']
