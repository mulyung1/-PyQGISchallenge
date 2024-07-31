'''Load the sf.gqz project and click the blocks layer'''
#get a reference to the block layer
layer=iface.activeLayer()

#querry layer for features
features=layer.getFeatures()

#get fields from attribute table
extract_fields=layer.fields()

'''=======LIST COMPREHENSION EXERCISE
    from left: the condition
    to right: the opearation'''

lis=[x.name() for x in extract_fields]
print(new_lis)
