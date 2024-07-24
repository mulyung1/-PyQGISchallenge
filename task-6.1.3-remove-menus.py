'''
Why remove them??

the processing toolbox has a new set of tools compared 
to those in these to menus.
it is advisable to use those in the processing toolbox
rather than the old ones in these menus.
'''

#get reference to the menus
vecMenu=iface.vectorMenu()
rasMenu=iface.rasterMenu()

#get a refernece to the menubar -> houses the menus
menubar=vecMenu.parentWidget()
#remove them from the menubar
menubar.removeAction(vecMenu.menuAction())
menubar.removeAction(rasMenu.menuAction())

'''
-> check menu bar, they are gone
use case- custom simple Qgis plugin that adds code like this to simplify Q
-> addAction() returns them to the menubar
'''


#menubar.addAction(vecMenu.menuAction())
#menubar.addAction(rasMenu.menuAction())