#!/bin/bash

cp -r scrollphat test/
# Prevent the init from loading i2c etc
rm test/scrollphat/__init__*
cat /dev/null >> test/scrollphat/__init__.py

cd test
python create_test.py
