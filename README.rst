travisCI-macOSx-PyQt-pyinstaller
================================

|Build Status|

This is a recipe for building PyQt5 applications for macOSx on travisCI
with Pyinstaller. As in  https://github.com/paulmueller/travisCI-macOSx-cython-wheels, 
all relevant build scripts are located in the `.travis` directory.


The pipeline includes:

- Downloading and installing MacPython from https://www.python.org/ftp/python/
  (The Python version has to be specified with the `MAC_PYTHON_VERSION=X.Y`
  environment variable in `.travis.yml`).
  I did not use homebrew or macports because python.org provides universal
  (in the sense that they are compatible with all osx versions above 10.6)
  MacPython installers that work on x64 and i386 systems.
- Installing all package dependencies into a virtual environment
- Running pytest
- Creating an app with pyinstaller
- Storing the app in a compressed DMG container
- Uploading the DMG to GitHub releases


Notes
-----

- There is no Python2.7 wheel for PyQt5, so Python2.7 will not work.
- Qt5 does no support all versions of osx. For instance
  `Qt5.9 <http://doc.qt.io/qt-5/supported-platforms-and-configurations.html#qt-5-9>`
  is the last version of Qt5 that supports osx 10.10. In this case, an older
  version of PyQt5 has to be installed via `pip install "pyqt5<5.10"`.
- The Python script used by PyInstaller `.travis/FooQtApp.py` must not have the
  exact same name as the Python package `fooqt` (capitalization does not help),
  because PyInstaller will confuse the script for a library, resulting in
  an unusable binary.
- The version of the `foo` package is determined from the current git tag and
  wheels are named accordingly.


.. |Build Status| image:: http://img.shields.io/travis/paulmueller/travisCI-macOSx-PyQt-pyinstaller.svg
   :target: https://travis-ci.org/paulmueller/travisCI-macOSx-PyQt-pyinstaller/
