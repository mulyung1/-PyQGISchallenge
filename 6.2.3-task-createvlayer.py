'''
see: 'https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/vector.html#creating-vector-layers'


create a temporary memory layer using QgsVectorLayer() classAttributes
these are: ->>not stored on disc
           ->> suitable to store intermidiate data/results
           ->> used by plugin/3rd party developers
           ->> used as a backend for temporary layers
           ->> support spatial indexing.
    -----importance of spatial indexing??-------
           ->>allows iterating over features by calling the createSpatialIndex() mtd. 
           ->>adva?? - fast because we iterate over features in a small region i.e specified rectangle 
    ----params---
        1. 'memory' - memory provider string 
        2. uri - -defines 
                    1.geometry i.e '(Multi)Polygon', '(Multi)Point', '(Multi)Line' etc
                    2.crs=coord ref sys
                    3.field=name (of layer)'attributes of a layer'
                    4.index=yes 'provider will use a spatial index'

    -> extent of our vector file will be the map canvas
'''
import os
from qgis.PyQt.QtCore import QVariant

mc=iface.mapCanvas()
extent=mc.extent()

#get an instance of current project
proj=QgsProject.instance()

#create layer
vlayer=QgsVectorLayer('Polygon', 'temp-layer', 'memory')

#get the crs of project
crs=proj.crs()
print(crs)
#set the crs to the vlayer
vlayer.setCrs(crs)


prov=vlayer.dataProvider()


#create a feature
feat=QgsFeature()
geom=QgsGeometry.fromRect(extent)
feat.setGeometry(geom)

#append feature via the dataProvider
prov.addFeature(feat)

vlayer.updateExtents()

#add layer to project
proj.addMapLayer(vlayer)



