'''TASK-1: delete an attribute table column'''

#access the currently selected layer
layer=iface.activeLayer()
#put the layer in editing mode
layer.startEditing()
#delete the column with index 1 i.e second column
layer.deleteAttribute(1)
#save the changes
layer.commitChanges()

#layer.rollBack() this line of code does not save your changes.works similar to "Don't Save"