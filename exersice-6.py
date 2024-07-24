'''
ro run this script, go to
>> bottome left input widget; 'coordinate'
>>type in world
>>press enter
this will load the world map layer.
'''

#make an instance of the messagebar class
msg=QgsMessageBar()

#check the name of the layer
layer=iface.activeLayer()
name=layer.name()
print(name)

#the expected name of the layer
expect='World Map'

#check whether the name matches the expected
if name == expect:
    #push a message
    msg.pushSuccess('NOTE:','The layer is validated')
else:
    #try changing the expected name to see this in action
    msg.pushCritical('Failed:','Layer is not what we want')
