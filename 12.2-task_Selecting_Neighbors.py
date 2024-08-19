'''
task: user wants to select features neighbouring a farm of interest
soln: a qgis action

find instructions to create a new action here
    https://courses.spatialthoughts.com/pyqgis-masterclass.html#qgis-actions
'''
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

# Apply the selection
layer.selectByIds(first_degree_neighbors)