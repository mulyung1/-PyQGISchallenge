'''This is A script that saves the attributes of selected features in a 
layer  to a csv file'''
import os
import pandas as pd

dir=os.path.join(os.path.expanduser('~'), 'Downloads','pyqgis-masterclass','data')
name='output2.csv'
output_path=os.path.join(dir, name)
#get the selected layer
layer=iface.activeLayer()

msg=QgsMessageBar()

#add checks
if not layer:
    msg.pushCritical('Bruuh!','Select a layer please')
  
if layer.type() != QgsMapLayer.VectorLayer:
    msg.pushCritical('Yo!','Please select a vector layer')

#get the header=fields
fieldNames=[y.name() for y in layer.fields()]

if not layer.selectedFeatures():
    msg.pushCritical('Mzae...!','hizi ni gani, please select features ')
else: 
    #extract attributes for selected features only
    lis=[x.attributes() for x in layer.selectedFeatures()]

    #create a data frame
    df=pd.DataFrame(lis, columns=fieldNames)

    #save to csv
    df.to_csv( output_path, index=False)
    msg.pushMessage('See!',f'Successfuly saved file to {output_path}')

