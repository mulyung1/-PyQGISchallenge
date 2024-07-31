'''
the main file with all the functionality adding the basemap
where the main plugin class is written
The PyQGIS code to load a XYZ tile layer 
can be found here:'https://docs.qgis.org/3.34/en/docs/pyqgis_developer_cookbook/cheat_sheet.html'
we will insert the layer at the bottom of the layers after loading the places.gpkg file

'''
import os
import inspect
from PyQt5.QtWidgets import QAction
from PyQt5.QtGui import QIcon
from qgis.core import QgsRasterLayer, QgsProject

cmd_folder = os.path.split(inspect.getfile(inspect.currentframe()))[0]

#access iface via self.iface
class BasemapLoaderPlugin:
    def __init__(self, iface):
        self.iface = iface
    #create the button with icon + add to plugins toolbar
    def initGui(self):
        icon = os.path.join(os.path.join(cmd_folder, 'icons8-python-48.png'))
        self.action = QAction(QIcon(icon), 'Load Basemap', self.iface.mainWindow())
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)
      
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action
    #where all the magic happens--data processing goes here
    def run(self):
        #url for tile layer we want
        basemap_url = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
        zmin = 0
        zmax = 19
        crs = 'EPSG:3857'
        #calls url
        uri = f'type=xyz&url={basemap_url}&zmax={zmax}&zmin={zmin}$crs={crs}'
        #create raster layer
        rlayer = QgsRasterLayer(uri, 'OpenStreetMap', 'wms')
        if rlayer.isValid():
            # Add the layer, but not to the legend
            QgsProject.instance().addMapLayer(rlayer, False)
            # Insert layer at the bottom of Layer Tree
            root = QgsProject.instance().layerTreeRoot()
            position = len(root.children())
            root.insertLayer(position, rlayer)
            self.iface.messageBar().pushSuccess('Success', 'Basemap Layer Loaded')
        else:
            self.iface.messageBar().pushCritical('Error', 'Invalid Basemap Layer')
