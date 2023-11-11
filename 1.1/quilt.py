import sys
import os
import pyautogui
from colorify import *
init_colorify()
def color(text: str, color):
    print(colorify(text, color))
def error(errorcode: str, md=None):
    if md==None:
        color(f"Error: {errorcode}", C.red)
    else:
        color(f"Error: {errorcode}\nExtra data: {md}", C.red)
def invalidcmd():
    error("INVALID_COMMAND")
if sys.platform != "linux":
    error("INVALID_OS")
    sys.exit()
def key(key: str):
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
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
        invalidcmd()
def filecheck(command: str):
    if command.startswith("f "):
        file = command[2:]
        file += ".quilt"
        if os.path.exists(file):
            with open(file,"r") as f:
                file = f.read().splitlines()
            for line in file:
                cmd(line)
        else:
            error("FILE_NOT_FOUND",file)
    else:
        cmd(command)
key("f11")
color("Quilt 1.1", C.blue)
while True:
    command = input(colorify(">> ", C.light_blue))
    filecheck(command)
