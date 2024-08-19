#a shell file to point our python code to python instalation with qgis
#sets all environment versions

#!/bin/bash

# Store old paths to restore later
OLD_PATH=$PATH
OLD_PYTHONPATH=$PYTHONPATH

# Define QGIS version (e.g., '3.28.0' or 'LTR' for the Long Term Release)
QGIS_VERSION="QGIS-LTR"  # Adjust this to your installed QGIS version if needed

# Update the environment for QGIS on Ubuntu
export PATH=/usr/bin:$PATH
export PYTHONPATH=/usr/share/qgis/python:/usr/share/qgis/python/plugins:$PYTHONPATH
export QGIS_PREFIX_PATH=/usr
export LD_LIBRARY_PATH=/usr/lib/qgis:$LD_LIBRARY_PATH
export QT_QPA_PLATFORM_PLUGIN_PATH=/usr/lib/qt/plugins/platforms/

echo "Using python3 from $(which python3)"

# Run your script with QGIS environment
python3 13_task_headless_mode.py

# Restore old environment
export PATH=$OLD_PATH
export PYTHONPATH=$OLD_PYTHONPATH
unset QGIS_PREFIX_PATH
unset LD_LIBRARY_PATH
unset QT_QPA_PLATFORM_PLUGIN_PATH

