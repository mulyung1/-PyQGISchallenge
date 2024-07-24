'''
every Qwidget emits a signal when clicked
in this script: 
we write code  to do something when the signal is emitted/a button is clicked
add button to chatgpt log in to allow code debbuging
'''

import webbrowser

def openGpt(): #our slot
    webbrowser.open('https://chatgpt.com/auth/login?sso')
    
#describe a button for the help menu
descr=QAction('Log in to Gpt')

#signal is 'triggered', connect to our slot
descr.triggered.connect(openGpt)

#get reference to the help menu in the menubar
hlp=iface.helpMenu()

#add a separator
hlp.addSeparator()

#add the button to helpMenu()
hlp.addAction(descr)

