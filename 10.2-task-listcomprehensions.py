'''Load the sf.gqz project and click the blocks layer'''
#get a reference to the block layer
layer=iface.activeLayer()

#querry layer for features
features=layer.getFeatures()

'''list comprehension 
    stores to a list
    starts from left to right
    from left: condition
    to right: what to do'''
lis=[feat.id() for feat in features]

print(lis)