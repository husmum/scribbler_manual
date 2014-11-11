from Myro import *
from Graphics import *

init()

win= Window("A",250,250)
win.mode = "manual"

def move(win,event):

    if event.key == "Up":
        forward (1) #Goes Forward

    if event.key == "Down":
        backward(1)

    if event.key == "Left":
        turnLeft(1)

    if event.key == "Right":
        turnRight(1)

    if event.key == "b":
        beep (1,800)

    if event.key == "B":
        beep (1,800)

    if event.key == " "
        stop()

onKeyPress(move)
