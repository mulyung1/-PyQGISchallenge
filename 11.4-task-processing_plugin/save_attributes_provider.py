'''this file gives the plugin access to the tlbx/processing provider'''

import os
import inspect
from PyQt5.QtGui import QIcon

from qgis.core import QgsProcessingProvider
from .save_attributes_algorithm import SaveAttributesAlgorithm


class SaveAttributesProvider(QgsProcessingProvider):

    def __init__(self):
        QgsProcessingProvider.__init__(self)

    def unload(self):
        QgsProcessingProvider.unload(self)

    def loadAlgorithms(self):
        #add the first algorithm
        self.addAlgorithm(SaveAttributesAlgorithm())
        #add more algorithms

    def id(self):
        #the hovername of the tool/plugin
        return 'save_attributes'

    def name(self):
        #displayed name of the plugin in tlbx/processing provider
        return self.tr('Save Attributes')

    def icon(self):
        cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]
        icon = QIcon(os.path.join(os.path.join(cmd_folder, 'logo.png')))
        return icon

    def longName(self):
        return self.name()