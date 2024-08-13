"""
this script is from 11.3. it has the main logic to do operations
***************************************************************************
*    SAVE THIS SCRIPT  INTO THE PROCESSING SCRIPT EDITOR TO RUN                                                                   *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingException,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFileDestination,
                       QgsVectorFileWriter,
                       QgsWkbTypes,
                       QgsProject)
from qgis import processing


class SaveAttributtesAlgorithm(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        """
        Returns a translatable string with the self.tr() function.
        """
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return SaveAttributtesAlgorithm()

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'save_attributtes'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr('Save Attributtes As CSV')


    def shortHelpString(self):
        """
        Returns a localised short helper string for the algorithm. This string
        should provide a basic description about what the algorithm does and the
        parameters and outputs associated with it..
        """
        return self.tr("This algorithm saves the attributes of a selected vector layer to a csv file")

    def initAlgorithm(self, config=None):
        #defines input and output parameters for the plugin
        self.addParameter(QgsProcessingParameterFeatureSource(
            'INPUT',
            'Select Your Input Layer'
        ))
        self.addParameter(QgsProcessingParameterFileDestination(
            'OUTPUT',
            'Your Output file: CSV',
            'CSV Files (*.csv)'
            
        ))
        
    #processing alg always returns a dictionary
    #this is where the magic happens 
    def processAlgorithm(self, parameters, context, feedback):
        #check the parameters for your algorithm
        print(parameters)
        #read user input as a vector layer object
        layer=self.parameterAsVectorLayer(parameters, 'INPUT', context)
        print(layer)
        #since output, get path object
        output=self.parameterAsFileOutput(parameters, 'OUTPUT', context)
        print(output)
        
        
        # Define the options for saving the layer
        save_options = QgsVectorFileWriter.SaveVectorOptions()
        save_options.driverName = 'CSV'
        save_options.fileEncoding = 'UTF-8'
        # We can also add some format-specific layer options 
        # These come from GDAL/OGR
        # https://gdal.org/drivers/vector/csv.html
        save_options.layerOptions = ['SEPARATOR=COMMA']
        
        
        total=layer.featureCount()
        print(total)
        
        
        # Create the writer
        writer = QgsVectorFileWriter.create(
            fileName=output,
            fields=layer.fields(),
            geometryType=QgsWkbTypes.NoGeometry,
            srs=layer.crs(),
            transformContext=QgsProject.instance().transformContext(),
            options=save_options)
        '''set the progress bar
        1. call enumerate function on any iterator
        2 get the index of the object/feature being processed 
        3.define progress as index/total multiplied by 100
        4 call the setProgress() on the feature being processed
        '''
        feedback.pushInfo('Processing started')
        for index, x in enumerate(layer.getFeatures()):
            #signal checked when user clicks cancel
            if feedback.isCanceled():
                break
            writer.addFeature(x)
            progress=int(100*(index/total))
            feedback.setProgress(progress)
        feedback.pushInfo('Processing Done!')
        
        
        return{'OUTPUT':output} 
        