#!/bin/bash

python ./mkfont.py > ./font.py

sudo find /usr -name font.py | grep -w "scrollphat" | xargs -n 1 sudo cp ./font.py
sudo find /usr -name *.pyc | grep -w "scrollphat" | xargs sudo rm &> /dev/null

exit 0
