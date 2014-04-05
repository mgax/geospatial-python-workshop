import geojson

workspaceVector = "/home/instructor/Desktop/Data/Text/";
fileDownload = workspaceVector + "judete.geojson"

json_data=open(fileDownload)
data = geojson.load(json_data)
json_data.close()

geomData = data["features"][0]["geometry"]

print geomData
#print geomData.type
#print geomData.coordinates


#connect to shapely
#from shapely.geometry import asShape
#x = asShape(geomData)
#print x.wkt


import geojson.crs
#By default, no CRS information is present. One should assume WGS84.

#Including crs
#crs = geojson.crs.Named(properties=dict(name="urn:ogc:def:crs:EPSG::31700"))
#point = geojson.Point(geomData.coordinates, crs=crs)
#print point
