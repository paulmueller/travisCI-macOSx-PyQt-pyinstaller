from PyQt5 import QtWidgets, QtCore

import fooqt.gui

def test_simple(qtbot):
    """Open the main window and close it again"""
    main_window = fooqt.gui.FooQt()
    main_window.close()


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
