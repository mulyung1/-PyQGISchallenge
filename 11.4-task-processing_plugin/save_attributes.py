'''the main class of the plugin
tells Q that 
1. this is the algorithm and this is the provider i.e Registers the custom provider containing the algorithm.
3. adds a button to the toolbar instead of user going to find it in the toolbox

'''

import os
import sys
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

from qgis.core import QgsProcessingAlgorithm, QgsApplication
import processing
from .save_attributes_provider import SaveAttributesProvider


cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

#main class of the plugin
class SaveAttributesPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initProcessing(self):
      self.provider = SaveAttributesProvider()
      QgsApplication.processingRegistry().addProvider(self.provider)

    '''Adds a button to the toolbar and plugin menu for easy access to the algorithm.'''
    def initGui(self):
      self.initProcessing()
      icon = os.path.join(os.path.join(cmd_folder, 'logo.png'))
      #addd a toolbar
      self.action = QAction(QIcon(icon), 'Save Attributes as CSV', self.iface.mainWindow())
      #connect toolbar signal to run slot
      self.action.triggered.connect(self.run)
      #add the toolbar to plugins menu
      self.iface.addPluginToMenu('&Save Attributes', self.action)
      self.iface.addToolBarIcon(self.action)

    def unload(self):
      QgsApplication.processingRegistry().removeProvider(self.provider)
      self.iface.removeToolBarIcon(self.action)
      self.iface.removePluginMenu('&Save Attributes', self.action)  
      del self.action

    def run(self):
      processing.execAlgorithmDialog('save_attributes:save_attributes')