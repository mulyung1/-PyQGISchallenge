#inject the layer id and feature id into script
layer_id = '[%@layer_id%]'
fid = [% $id %]

#retrieve layer object corresponding to given layer id 
layer = QgsProject.instance().mapLayer(layer_id)

def get_neighbors(fid):
    f = layer.getFeature(fid)
    '''to get all intersecting features >>use list comprehension 
      use touches() mtd = if data is topologically correct. 
      supply the bounding box to iterator(getFeatures())to use spatial index
    '''
    neighbors = [
        x.id()
        for x in layer.getFeatures(f.geometry().boundingBox())
        if x.geometry().intersects(f.geometry()) and x.id() != f.id()
    ]
    return neighbors

#call the method and store it in a variable
first_degree_neighbors = get_neighbors(fid)

'''-----------Exercise 11 done-------
to add new selection to previous selection. 
add a behaviour to the selectByIds() mtd'''
# Apply the selection
layer.selectByIds(first_degree_neighbors, QgsVectorLayer.SelectBehavior.AddToSelection)

second_degree_neighbors=set()

for y in first_degree_neighbors:
    neighbors=get_neighbors(y)
    second_degree_neighbors.update(neighbors)

#remove all 1st degree neighbors from the set
second_degree_neighbors=second_degree_neighbors.difference(
    set(first_degree_neighbors))

'''-----------Exercise 11 done-------
to add new selection to previous selection. 
add a behaviour to the selectByIds() mtd'''
#remove the feature itself from the set if it exists
second_degree_neighbors.discard(fid)
#apply the selection
layer.selectByIds(list(second_degree_neighbors), QgsVectorLayer.SelectBehavior.AddToSelection)


