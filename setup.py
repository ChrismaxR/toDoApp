from setuptools import setup

APP = ['/Users/home/Documents/5. Extra Curriculair/toDoApp/toDoApp.py']  # Replace 'your_script.py' with the actual name of your script
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
