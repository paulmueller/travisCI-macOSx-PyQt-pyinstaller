#!/bin/bash

if [ -z $1 ]; then
    echo "Please specify package name as command line argument!"
    exit 1
fi

ls -l ./dist

NAME=$1
SCRIPT="./${1}/__main__.py"
APP="./dist/${1}.app"
DMG="./dist/${1}.dmg"

pip install pyinstaller

pyinstaller -w -y -n $NAME $SCRIPT

hdiutil create -srcfolder "${APP}" -volname "${NAME}" -fs HFS+ \
        -fsargs "-c c=64,a=16,e=16" -format UDRW ./dist/pack.temp.dmg

hdiutil convert ./dist/pack.temp.dmg -format UDZO -imagekey zlib-level=9 \
        -o "${DMG}"

ls -l ./dist
