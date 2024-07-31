'''
third file: tells the plugin manager which class to initialise
imports the plugin class created in the second file and creates an instance of it.

'''

from .load_basemap import BasemapLoaderPlugin

def classFactory(iface):
    return BasemapLoaderPlugin(iface)