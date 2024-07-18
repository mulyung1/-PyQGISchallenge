#create an object of the message box class
msgBox=QMessageBox()

#write a dialog
msgBox.setText('Click OK to confirm!')

#add the cancel button
msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#store the return value based on the clicked button
return_value=msgBox.exec()
if return_value == QMessageBox.Ok:
    print('You pressed ok')
elif return_value== QMessageBox.Cancel:
    print('You exited')