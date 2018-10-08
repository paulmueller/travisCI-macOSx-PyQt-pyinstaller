travisCI-macOSx-PyQt-pyinstaller
================================

|Build Status|

This is a recipe for building PyQt5 applications for macOSx on travisCI
with Pyinstaller. As in  https://github.com/paulmueller/travisCI-macOSx-cython-wheels, 
all relevant files are located in the `.travis` directory.


The pipeline includes:

- Downloading and installing MacPython from https://www.python.org/ftp/python/
  (The Python version has to be specified with the `MAC_PYTHON_VERSION=X.Y`
  environment variable in `.travis.yml`).
  I did not use homebrew or macports because python.org provides universal
  (in the sense that they are compatible with all osx versions above 10.6)
  MacPython installers that work on x64 and i386 systems.
- Running pytest
- Creating an app with pyinstaller
- Storing the app in a compressed DMG container
- Uploading the DMG to GitHub releases


Notes
-----

- There is no Python2.7 wheel for PyQt5, so Python2.7 will not work.


.. |Build Status| image:: http://img.shields.io/travis/paulmueller/travisCI-macOSx-PyQt-pyinstaller.svg
   :target: https://travis-ci.org/paulmueller/travisCI-macOSx-PyQt-pyinstaller/
