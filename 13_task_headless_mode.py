import os
from qgis.core import QgsApplication

#an instance of QGIS without starting the application
qgs = QgsApplication([], False)
#initialise your Qobject
qgs.initQgis()

import processing
from processing.core.Processing import Processing
Processing.initialize()

#define your data directory
data_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'pyqgis_masterclass')

#define your boundaries layer
vector_layer = 'seismic_zones.shp'
vector_layer_path = os.path.join(data_dir, vector_layer)

#define your raster layer
raster_layer = 'srtm.tif'
raster_layer_path = os.path.join(data_dir, raster_layer)

# Input vector has invalid geometries
# Fix them first
results=processing.run("native:fixgeometries", {
    'INPUT':vector_layer_path,
    'METHOD':0,
    'OUTPUT':'TEMPORARY_OUTPUT'
    })

#get the fixed layer from the results dictionary
fixed_vector_layer=results['OUTPUT']


# Run Zonal Statistics

# Save output to a geopackage
output_name = 'seismic_zones_with_elevation3.gpkg'
output_path = os.path.join(data_dir, output_name)

#save result to output path
processing.run("native:zonalstatisticsfb", {
    'INPUT':fixed_vector_layer,
    'INPUT_RASTER':raster_layer_path,
    'RASTER_BAND':1,
    'COLUMN_PREFIX':'elevation_',
    'STATISTICS':[0,1,2],
    'OUTPUT':output_path
    })
print('Output Layer Created', output_path)
#stop qgis

qgs.exitQgis()