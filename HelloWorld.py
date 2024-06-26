import os

from pypulse import Window, Aplication
from pypulse.Template import Template

# Specifying application Route
Aplication.Vars.APLICATION_PATH = os.path.dirname(os.path.abspath(__file__))

# Configuring applications
# If you create a new application, make sure to include it here.
APPLICATIONS = ["baseapp"]

# Application window settings
APP_SETTINGS = {
    'title': 'PyPulse App',
    'debug': False,
    'debug_file_name': 'debug.log',
    'window_size_x': 1270,
    'window_size_y': 720,
    'icon_path': os.path.join(
        Aplication.Vars.APLICATION_PATH, 'window_logo.ico')
}

# Defining the locations for templates and static files.
Template.TEMPLATE_PATH = os.path.join(
    Aplication.Vars.APLICATION_PATH, 'templates')
Template.STATIC_PATH = os.path.join(
    Aplication.Vars.APLICATION_PATH, 'static')

# setting apps
for x in APPLICATIONS:
    Aplication.SetAplication(x)

# Initializing window
browser = Window.LoadBrowser(**APP_SETTINGS)
