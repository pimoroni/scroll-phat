#!/bin/bash

python ./mkfont.py > ./font.py

sudo find /usr -name font.py | grep "scrollphat" | xargs -n 1 sudo cp ./font.py

exit 0
