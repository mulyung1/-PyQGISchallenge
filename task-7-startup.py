'''
this script is run every time q starts 
it sets the qgis versin name and no alongside the title in the main window
Q emits an 'initializationCompleted' signal every time it is run
we use this signal to run the code when the signal is emmited(when q starts)
'''

from qgis.utils import iface
from qgis.core import QgsExpressionContextUtils

#our slot - sets version nuber and name to window title
def customise():
    #get the version
    version=QgsExpressionContextUtils.globalScope().variable('qgis_version')
    #get the window title
    title=iface.mainWindow().windowTitle()
    #set version name and no to the project title
    proj=QgsProject.instance()
    proj.setTitle(f'{title} | {version}')
    
#signal and connection
iface.initializationCompleted.connect(customise)