'''
here, we load a project using 
    -> the read method and 
    -> a dropdown widget added to the toolbar
'''


'''------.read() method------'''
#project location
path=r'C:\Users\hp\jupyter\QGISCHALLENGE\data\sf.qgz'

proj=QgsProject.instance()
proj.read(path)

