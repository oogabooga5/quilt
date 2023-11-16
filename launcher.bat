@echo off
pip install pyautogui
pip install colorify
pip install requests
set /p ver="Quilt version: "
set "url=https://raw.githubusercontent.com/oogabooga5/quilt/main/%ver%/quilt.py"
curl %url% -O quilt.py
python quilt.py
del quilt.py