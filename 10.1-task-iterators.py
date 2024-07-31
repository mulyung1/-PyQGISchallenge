#get a reference to the layer
layer=iface.activeLayer()

#querry layer for features
features=layer.getFeatures()

#empty list to stor extracted ids
extracted_ids=[]

#create a loop to iterate over the features
for feat in features:
    id=feat.id()
    extracted_ids.append(id)

print(extracted_ids)


