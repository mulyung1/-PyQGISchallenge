'''
We create:
        ->> a toolbar 
        with a: > Label
                > an input box
                > a Go button
'''

# 1. Create the toolbar
tulbar = iface.addToolBar('CRS Switch')

# 2. Create the label
label = QLabel('Enter an EPSG Code:', parent=tulbar)

# 3. Create line edit widget for entering EPSG code
txtbox = QLineEdit('3857', parent=tulbar)  # Default EPSG code is set to 3857

# 4. Create the button that triggers the CRS change
btn = QPushButton('Go!', parent=tulbar)

# 5. Append the widgets to the toolbar
tulbar.addWidget(label)
tulbar.addWidget(txtbox)
tulbar.addWidget(btn)

# Define the function to change CRS
def changecrs(user_input):
    # Get the EPSG code entered by the user and convert it to an integer
    code = int(txtbox.text())
    
    # Display a message indicating the function was called and the EPSG code entered
    msg.pushMessage('Function Called:', f'You entered EPSG Code: {code}.')
    
    '''---------Change project CRS to the entered CRS-----'''
    
    # Instantiate the current project
    proj = QgsProject.instance()
    
    # Create a new CRS object
    crs = QgsCoordinateReferenceSystem()
    
    # Initialize the CRS object using the EPSG code entered by the user
    crs.createFromOgcWmsCrs(f'EPSG:{code}')
    
    # Set the project's CRS to the new CRS
    proj.setCrs(crs)
    
    # Display a warning message indicating the CRS has been set
    msg.pushWarning('NOTE:', f'You set the CRS to {code}')
    
# Connect the button click event to the changecrs function
btn.clicked.connect(changecrs)
