import sys

from PyQt5 import QtWidgets, QtCore

import fooqt.gui

def test_fit_all(qtbot):
    """Perform a simple fit with the standard parameters
    
    The values tested here are the same as in the afmlib test
    ´test_appraoch_retract.test_afm_data_set_fitting`
    """
    main_window = fooqt.gui.FooQt()
    main_window.close()


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
