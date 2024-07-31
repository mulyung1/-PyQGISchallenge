
dir=os.path.join(os.path.expanduser('~'),'jupyter','QGISCHALLENGE','data')
results=processing.run("gdal:cliprasterbymasklayer", {
    'INPUT':'C:/Users/hp/jupyter/QGISCHALLENGE/data/srtm.tif',
    'MASK':'C:/Users/hp/jupyter/QGISCHALLENGE/data/shoreline.shp',
    'OUTPUT':'TEMPORARY_OUTPUT'
    })
clip=results['OUTPUT']

#prepare your output
output='hillshade.tif'
output_path=os.path.join(dir, output)

#run the hillshade algorithm on the clipped file
processing.runAndLoadResults("native:hillshade", {
    'INPUT':clip,
    'Z_FACTOR':1,
    'AZIMUTH':300,
    'V_ANGLE':40,
    'OUTPUT':output_path})
