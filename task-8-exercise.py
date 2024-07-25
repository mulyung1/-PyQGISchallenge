dir=os.path.join(os.path.expanduser('~'),'jupyter','QGISCHALLENGE','data')

shapefile='seismic_zones.shp'
raster='srtm.tif'
rasta_file=os.path.join(dir,raster)
seismic_zone=os.path.join(dir,shapefile)

#fix geomerty errors
results=processing.run("native:fixgeometries", {
    'INPUT':seismic_zone,
    'METHOD':1,
    'OUTPUT':'TEMPORARY_OUTPUT'})

fixed=results['OUTPUT']

#do zonal statistics of count, sum, and mean
results2=processing.runAndLoadResults("native:zonalstatisticsfb", {
    'INPUT':fixed,
    'INPUT_RASTER':rasta_file,
    'RASTER_BAND':1,
    'COLUMN_PREFIX':'zonal_stats_',
    'STATISTICS':[0,1,2],
    'OUTPUT':'TEMPORARY_OUTPUT'})
