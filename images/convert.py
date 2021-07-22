import pyqt5ac

pyqt5ac.main(uicOptions='--from-imports', force=False, initPackage=True, ioPaths=[
        ['images/*.qrc', 'generated/%%FILENAME%%_rc.py']
])
