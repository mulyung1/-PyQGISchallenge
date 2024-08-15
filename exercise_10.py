'''find instructions to create a new action here
    https://courses.spatialthoughts.com/pyqgis-masterclass.html#qgis-actions

    copy paste this code to the editor as per the steps.

    this QGIS action saves a new vector layer 
    when user selects on the active layer
'''

from qgis.utils import iface 

#get these
feature_name='[%NAME%]'
feature_id=[%$id%]
layer_id='[%@layer_id%]'

#get the qgis layer object with the exctracted id
layer=QgsProject.instance().mapLayer(layer_id)

#materialize() creates a new layer
new_layer=layer.materialize(
    QgsFeatureRequest().setFilterFids([feature_id]))

#set name for new_layer
new_layer.setName(feature_name)

#add the layer to project
QgsProject.instance().addMapLayer(new_layer)

'''------EXERCISE-------
display an info message that: New layer is created bearing the layers name 
'''
iface.messageBar().pushInfo('Very Good', f'New Layer created:{feature_name}')


#set active layer back to our layer of interest 'the world'
iface.setActiveLayer(layer)
