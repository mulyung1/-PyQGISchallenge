'''
the main file with all the functionality
where the main plugin class is written
'''

import os
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

#plugin manager calls this class to create an instance of the plugin
class BasemapLoaderPlugin:
    #access iface is using self.iface
    def __init__(self, iface):
        self.iface = iface
    
    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder, 'icons8-python-48.png'))
        self.action = QAction(QIcon(icon), 'Load Basemap', self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)
      
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
        
    def run(self):
        #where the magic happens. some processing is done here
        self.iface.messageBar().pushMessage('HOORAY! This is your first plugin')