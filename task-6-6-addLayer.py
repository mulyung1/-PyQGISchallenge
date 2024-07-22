'''
-----------ADD LAYERS USING PYQGIS-----------
use the addVectorLayer mtd
takes 3 arguments
1. the path to file
2. the name of the layer
3. the provide gdal/ogr

different layers have different syntax for loading
seethe PYQGIS DEVELOPER COOKBOOK: 'https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/loadlayer.html#vector-layers'

'''
#add a shapefile
layer=r'C:\Users\hp\jupyter\QGISCHALLENGE\data\seismic_zones.shp'
iface.addVectorLayer(layer, 'seismic_zones', 'ogr')

#add a zoning layer from a geopackage
gpkglayer=r'C:\Users\hp\jupyter\QGISCHALLENGE\data\sf.gpkg|layername=zoning'
iface.addVectorLayer(gpkglayer,'zoning', 'ogr')

#check for currently selected layer
laye_r=iface.activeLayer()
name=laye_r.name()
print(name)

#change name of layer
laye_r.setName('san_francisco-'+ name)


