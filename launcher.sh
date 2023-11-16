#!/usr/bin/env bash
pip install pyautogui
pip install colorify
pip install requests
sudo apt-get install python-tk
read -p "Quilt version: " ver
url="https://raw.githubusercontent.com/oogabooga5/quilt/main/$ver/quilt.py"
curl $url -O quilt.py
python3 quilt.py
rm quilt.py