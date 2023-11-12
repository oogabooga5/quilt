import sys
import os
import pyautogui
import turtle
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
def data(data: str, path:str="https://raw.githubusercontent.com/oogabooga5/quilt/main/1.2/data"):
    os.system(f"curl {path}/{data} -O {data}")
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
        print("cookieclicker")
        print("data {data}")
    elif command.startswith("os "):
        command = command[3:]
        os.system(command)
    elif command.startswith("data "):
        dataname = command[5:]
        data(dataname)
    elif command.startswith("cookieclicker"):
        data("cookie.gif")
        print("Ctrl+Z to quit")
        wn = turtle.Screen()
        wn.title("Cookie Clicker")
        wn.bgcolor("black")
        wn.register_shape("cookie.gif")
        cookie = turtle.Turtle()
        cookie.shape("cookie.gif")
        cookie.speed(0)
        clicks = 0
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.color("white")
        pen.penup()
        pen.goto(0,200)
        pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
        def clicked(x, y):
            global clicks
            clicks += 1
            pen.clear()
            pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
            cookie.onclick(clicked)
        wn.mainloop()
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
color("Quilt 1.2", C.blue)
while True:
    command = input(colorify(">> ", C.light_blue))
    filecheck(command)

