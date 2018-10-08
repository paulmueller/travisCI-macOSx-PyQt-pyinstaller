#!/bin/bash

if [ -z $1 ]; then
    echo "Please specify package name as command line argument!"
    exit 1
fi

NAME=$1
SCRIPT="./${1}/__main__.py"
APP="./dist/${1}.app"
DMG="./dist/${1}.dmg"
TMP="./dist/pack.temp.dmg"
pip install pyinstaller

pyinstaller -w -y -n $NAME --additional-hooks-dir ".travis" $SCRIPT

# create temporary DMG
hdiutil create -srcfolder "${APP}" -volname "${NAME}" -fs HFS+ \
        -fsargs "-c c=64,a=16,e=16" -format UDRW "${TMP}"

# optional: edit the DMG
# https://stackoverflow.com/questions/96882/how-do-i-create-a-nice-looking-dmg-for-mac-os-x-using-command-line-tools

# create crompressed DMG
hdiutil convert "${TMP}" -format UDZO -imagekey zlib-level=9 -o "${DMG}"

# remove temporary DMG
rm $TMP

# show created files
ls -l ./dist
