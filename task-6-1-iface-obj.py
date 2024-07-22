#->> go into the mainwindow via the iface object
#->> get the window title
title=iface.mainWindow().windowTitle()
print(title)
#what is your new title
newTitle=title.replace('QGIS', 'Custom Q')
#set new title
iface.mainWindow().setWindowTitle(newTitle)

