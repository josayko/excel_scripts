from setuptools import setup

APP = ["main.py"]  # Replace with your script name
OPTIONS = {
    "argv_emulation": True,  # Useful for GUI apps, especially with Tkinter
    # Add other options if needed, e.g., 'packages': ['yourpackage']
}

setup(
    app=APP,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
