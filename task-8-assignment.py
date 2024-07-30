'''Add a button to the Plugins Toolbar called Show Raster Statistics
with an icon of your choice.
Write a function named show_statistics() that is called when the button 
is clicked.
The function should obtain the current extent of the map canvas and 
calculate the raster statistics.
Once the statistics are computed, it should display a message in the 
message bar with the information.'''

dir=os.path.join(os.path.expanduser('~'),'jupyter','QGISCHALLENGE','data')
icon_name='icons8-python-48.png'
icon_path=os.path.join(dir, icon_name)

msg=QgsMessageBar()
#describe a button for the plugins toolbar
icon=QAction(QIcon(icon_path), 'Show Raster Statistics')

#get reference to the plugins toolbar
tulbar=iface.pluginToolBar()

#add the button + icon to plugins toolbar
tulbar.addAction(icon)


#our slot
def show_statistics():
    #get the current extent of the mapcanvas
    extent=iface.mapCanvas().extent()
    
    #get an instance of current project
    proj=QgsProject.instance()
    
    #create the layer to be loaded
    vlayer=QgsVectorLayer('Polygon', 'temp-layer', 'memory')
    prov=vlayer.dataProvider()
    
    #create a feature
    feat=QgsFeature()
    geom=QgsGeometry.fromRect(extent)
    feat.setGeometry(geom)

    #append feature via the dataProvider
    prov.addFeature(feat)

    vlayer.updateExtents()
    
    #get the selected raster layer
    raster_file=iface.activeLayer()
    
    # get the extent of the raster layer
    raster_extent = raster_file.extent()
    
    # Check for intersection between the raster layer and the extent layer
    if extent.intersects(raster_extent):
        pass
    else:
        msg.pushWarning('ala!','No pixel values found')
        return
    
    
    if isinstance(raster_file, QgsRasterLayer):
        #path to stor the output file
        stats_file=os.path.join(dir, 'output3.csv')
        result=processing.runAndLoadResults("native:zonalstatisticsfb", {
                'INPUT':vlayer,
                'INPUT_RASTER':raster_file,
                'RASTER_BAND':1,
                'COLUMN_PREFIX':'elev_',
                'STATISTICS':[0,1,2,3,5,6],
                'OUTPUT':stats_file})
                
        with open(stats_file, 'r') as file:
            lines = file.readlines()
            if lines:
                # Assuming the output file is in CSV format and the average value is in the sixth column (index 5)
                avg_value_line = lines[-1]  # Get the last line which might contain the statistics
                avg_values = avg_value_line.split(',')  # Split by comma
                average_value = avg_values[2] if len(avg_values) > 5 else 'N/A'
                msg.pushSuccess('Raster Statistics!',f'average elevation is {average_value}')
    else:
        msg.pushCritical('YO!','Only raster layers allowed here, HINT: SELECT A RASTER LAYER')
        
#our signal
icon.triggered.connect(show_statistics)









    

