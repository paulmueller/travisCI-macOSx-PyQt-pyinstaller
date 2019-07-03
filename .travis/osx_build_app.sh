#!/bin/bash
# Builds a macOS app in a DMG container using PyInstaller and an app launcher.
# usage:
#     osx_build_app.sh AppName [AppVersion]
#
# Notes:
# - AppVersion is optional (only used for name of DMG container)
# - This script must be called from the root directory of the repository
# - The file ./travis/AppNameApp.py [sic] must be present (relative
#   to root of the repository)

if [ -z $1 ]; then
    echo "Please specify package name as command line argument!"
    exit 1
fi
NAME=$1

if [ -z $2 ]; then
    NAMEVERSION=${1}
else
    NAMEVERSION=${1}_${2}
fi

# append "App" to avoid naming conflicts with python library
SCRIPT=".travis/${NAME}App.py"
APP="./dist_app/${NAME}App.app"
DMG="./dist_app/${NAMEVERSION}.dmg"
TMP="./dist_app/pack.temp.dmg"
pip install pyinstaller

# Work in a different directory (./dist_app instead of ./dist),
# otherwise PyPI deployment on travis-CI tries to upload *.dmg files.
pyinstaller -w -y --distpath="./dist_app" --additional-hooks-dir=".travis" $SCRIPT

# create temporary DMG
hdiutil create -srcfolder "${APP}" -volname "${NAMEVERSION}" -fs HFS+ \
        -fsargs "-c c=64,a=16,e=16" -format UDRW "${TMP}"

# optional: edit the DMG
# https://stackoverflow.com/questions/96882/how-do-i-create-a-nice-looking-dmg-for-mac-os-x-using-command-line-tools

# create crompressed DMG
hdiutil convert "${TMP}" -format UDZO -imagekey zlib-level=9 -o "${DMG}"

# remove temporary DMG
rm $TMP

