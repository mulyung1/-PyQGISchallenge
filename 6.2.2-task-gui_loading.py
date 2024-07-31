'''------DROPDOWN WIDGET------'''
import os

#data location

#1. create the toolbar to which it will be hosted
tulbar=iface.addToolBar('Project Selector')

#create the label
label=QLabel('Select a project to add', parent=tulbar)

#create the dropdown
selekta=QComboBox(parent=tulbar)
selekta.addItem('sf.qgz')
selekta.addItem('places.qgz')

#set to show nothing
selekta.setCurrentIndex(-1)

#our slot
def load_proj(proj_name):
    proj=QgsProject.instance()
    dir=os.path.join(os.path.expanduser('~'),'jupyter','QGISCHALLENGE','data')
    path=os.path.join(dir, proj_name)
    proj.read(path)
    print('read')

#our signal
selekta.currentTextChanged.connect(load_proj)
tulbar.addWidget(label)
tulbar.addWidget(selekta)


    
    
    