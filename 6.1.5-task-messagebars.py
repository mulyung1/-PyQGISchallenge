
'''
lets add a clock icon in the toolbar where we 
see time anytime the clock icon is pressed in a qmessagebar

'''
from datetime import datetime

#path to your icon :replace with path to your shapefile
# icondir=r'C:\Users\hp\jupyter\QGISCHALLENGE\data\question.svg'
icon=QIcon(icondir)

#our slot
def showtime():
    now=datetime.now()
    currenttime=now.strftime('%H:%M:%S:')
    iface.messageBar().pushWarning('Our time now is:', currenttime)
    
#what we what to to?? an action
act=QAction('Show Time')

#our signal
act.triggered.connect(showtime)
#what icon is for our action??
act.setIcon(icon)

#add the icon to toolbar
iface.addToolBarIcon(act)
