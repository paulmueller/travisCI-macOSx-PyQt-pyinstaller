#-----------------------------------------------------------------------------
# Copyright (c) 2017, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# Hook for fooqt
import os
import platform

from PyInstaller.utils.hooks import collect_data_files

# Data files
datas = collect_data_files("fooqt")
datas += collect_data_files("fooqt", subdir="img")


# Windows specific
if platform.system()=="Windows":
    # The build machine should have this variable set
    # (see Readme.rst)
    dllsource = os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"]
    for ds in dllsource.split(";"):
        datas += [(ds+"/*.dll", "platforms")]

hiddenimports = ["fooqt"]
