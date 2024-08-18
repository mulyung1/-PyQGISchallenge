#access the ids of active layer
layer_id='[%layer_id%]'
field_id=[%$id%]

#make a layer object of specified layer(right-clicked layer) 
layer=QgsProject.instance().mapLayer(layer_id)

def get_neighbors(field_id):
    #get our iterator
    feat=layer.getFeature(field_id)
    '''to get all intersecting features >>use list comprehension 
       use touches() mtd = if data is topologically correct. 
       supply the bounding box to iterator(getFeatures())to use spatial index
    '''
    neighbors_list=[x.id() for x in layer.getFeatures(feat.geometry().boundingBox()) if x.geometry().intersects(feat.geometry()) and x.id() != feat.id()]
    return neighbors_list
#call the method and store it in a variable
first_degree_neighbors=get_neighbors(field_id)

#apply the selection
layer.selectByIds(first_degree_neighbors)


