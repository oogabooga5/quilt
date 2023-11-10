import sys
def error(errorcode: str, md=None):
    if md==None:
        print(f"Error: {errorcode}")
    else:
        print(f"Error: {errorcode}\nExtra data: {md}")
if sys.platform != "linux":
    error("INVALID_OS")
    sys.exit()
import os
import pyautogui
from colorify import *
init_colorify()
def key(key: str):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
def color(text: str, color):
    print(colorify(text, color))
def cmd(command: str):
    if command.startswith("print "):
        text = command[6:]
        print(text)
    elif command.startswith("exit"):
        sys.exit()
    elif command.startswith("help"):
        print("print {text}")
        print("exit")
        print("f {file}")
        print("os {command}")
    elif command.startswith("os "):
        command = command[3:]
        os.system(command)
    else:
        error("INVALID_COMMAND")
def filecheck(command: str):
    if command.startswith("f "):
        file = command[2:]
        if os.path.exists(file):
            pass
        else:
            error("FILE_NOT_FOUND")
        with open(file,"r") as f:
            file = f.read().splitlines()
        for line in file:
            cmd(line)
    else:
        cmd(command)
key("f11")
color("Quilt 1.0", C.blue)
while True:
    command = input(colorify(">> ", C.light_blue))
    filecheck(command)
