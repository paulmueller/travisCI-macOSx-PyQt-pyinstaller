import pkg_resources
import signal
import sys
import traceback

from PyQt5 import uic, QtWidgets

from ._version import version as __version__

# load QMainWindow from ui file
ui_path = pkg_resources.resource_filename("fooqt", "main.ui")
MainBase = uic.loadUiType(ui_path)[0]


class FooQt(QtWidgets.QMainWindow, MainBase):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        MainBase.__init__(self)
        self.setupUi(self)
        # Disable native menubar (e.g. on Mac)
        self.menubar.setNativeMenuBar(False)
        # if "--version" was specified, print the version and exit
        if "--version" in sys.argv:
            print(__version__)
            QtWidgets.QApplication.processEvents()
            sys.exit(0)


def excepthook(etype, value, trace):
    """
    Handler for all unhandled exceptions.

    :param `etype`: the exception type (`SyntaxError`, etc...);
    :type `etype`: `Exception`
    :param string `value`: the exception error message;
    :param string `trace`: the traceback header, if any (otherwise,
     it prints the standard Python header:
     ``Traceback (most recent call last)``.
    """
    vinfo = "Unhandled exception in PyJibe version {}:\n".format(__version__)
    tmp = traceback.format_exception(etype, value, trace)
    exception = "".join([vinfo]+tmp)

    errorbox = QtWidgets.QMessageBox()
    errorbox.addButton(QtWidgets.QPushButton('Close'),
                       QtWidgets.QMessageBox.YesRole)
    errorbox.addButton(QtWidgets.QPushButton(
        'Copy text && Close'), QtWidgets.QMessageBox.NoRole)
    errorbox.setText(exception)
    ret = errorbox.exec_()
    if ret == 1:
        cb = QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(exception)


# Make Ctr+C close the app
signal.signal(signal.SIGINT, signal.SIG_DFL)
# Display exception hook in separate dialog instead of crashing
sys.excepthook = excepthook
