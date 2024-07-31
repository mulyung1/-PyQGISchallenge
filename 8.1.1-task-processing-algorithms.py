'''
here we use the native hillshade algorithm to create
hillshades at different angles using python
'''

import os
#load your active raster layer(DEM)
layer=iface.activeLayer()

#data directory
dir=os.path.join(os.path.expanduser('~'), 'jupyter','QGISCHALLENGE','data')

#hillshades where the angle is between 10 and 90 with a separation of 20
for angle in range(10,90,20):
    output=f'hillshade_{angle}.tif'
    output_path=os.path.join(dir,output)
    #run the algorithm
    results=processing.runAndLoadResults("native:hillshade", {
        'INPUT':layer,
        'Z_FACTOR':1,
        'AZIMUTH':300,
        'V_ANGLE':angle,
        'OUTPUT':output_path
    })
