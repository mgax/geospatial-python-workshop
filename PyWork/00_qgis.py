from qgis.core import *
import qgis.utils

layer = qgis.utils.iface.activeLayer()
provider = layer.dataProvider()


for feature in layer.getFeatures():
    attr_list =[]
    for attr in feature.attributes():
        attr_list.append(attr)
    geom = feature.geometry()

    print "Name:", attr_list[3]
    print "Area:", geom.area() / 10000
    print "Perimeter:", geom.length() /1000
  



