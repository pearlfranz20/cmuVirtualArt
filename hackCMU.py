# hackCMU.py
# Collaborators: Cameron, Julia, Pat, Pearl
# Project: CMU Virtual Art Installation

from cmu_112_graphics import *
from tkinter import colorchooser
import random

def appStarted(app):
    app.red = 255
    app.green = 0
    app.blue = 0

    app.topMargin = 60
    app.sideMargin = 10
    app.colorBar = 60

    app.building = 'Gates'
    app.color = 'pink'

    app.cx = 0
    app.cy = 0
    app.r = 5

    app.click = False
    app.listOfDots = [] #x, y, color, selectedCircle

    app.selectedCircle = 0

def drawDots(app, canvas):
    for i in range(len(app.listOfDots)):
        x = app.listOfDots[i][0]
        y = app.listOfDots[i][1]
        color = app.listOfDots[i][2]
        radius = app.listOfDots[i][3]
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill= color, outline="")


def choose_color(app): 
    # variable to store hexadecimal code of color 
    color_code = colorchooser.askcolor(title ="Choose color")
    if color_code[1] != None:
        app.color = color_code[1]

    
def distance(x0, y0, x1, y1):
    return ((x0-x1)**2+(y1-y0)**2)**.5

def mousePressed(app, event):
    if (app.width - app.sideMargin - 130 <= event.x <= app.width - app.sideMargin - 25 and
    app.height - app.sideMargin - app.colorBar/2 - 13 <= event.y <= app.height - app.sideMargin - app.colorBar/2 + 15):
        choose_color(app)
    if (app.sideMargin + app.r <= event.x <= app.width-app.sideMargin - app.r and app.topMargin + app.r <=event.y<= app.height - app.sideMargin - app.colorBar - app.r):
        app.cx = event.x
        app.cy = event.y
        app.listOfDots.append((app.cx, app.cy, app.color, app.r))
        app.click = True

    if distance(app.width - app.sideMargin - 290 + 5, app.height - app.sideMargin - app.colorBar/2 - 5 + 5, event.x, event.y) <= 10:
        app.selectedCircle = 0
        app.r = 5
    elif distance(app.width - app.sideMargin - 262.5 + 7.5, app.height - app.sideMargin - app.colorBar/2 - 7.5 + 7.5, event.x, event.y) <= 15:
        app.selectedCircle = 1
        app.r = 7.5
    elif distance(app.width - app.sideMargin - 230 + 5, app.height - app.sideMargin - app.colorBar/2 - 10 + 5, event.x, event.y) <= 20:
        app.selectedCircle = 2
        app.r = 10
    
    

def selectCircle(canvas, app):
    if app.selectedCircle == 0:
        canvas.create_oval(app.width - app.sideMargin - 289, app.height - app.sideMargin - app.colorBar/2 - 4,
                                app.width - app.sideMargin - 281, app.height - app.sideMargin - app.colorBar/2 + 4,
                                fill='white', outline='')
    elif app.selectedCircle == 1:
        canvas.create_oval(app.width - app.sideMargin - 261.5, app.height - app.sideMargin - app.colorBar/2 - 6.5,
                            app.width - app.sideMargin - 248.5, app.height - app.sideMargin - app.colorBar/2 + 6.5,
                            fill='white', outline='')
    elif app.selectedCircle == 2:
        canvas.create_oval(app.width - app.sideMargin - 229, app.height - app.sideMargin - app.colorBar/2 - 9,
                            app.width - app.sideMargin - 211, app.height - app.sideMargin - app.colorBar/2 + 9,
                            fill='white', outline='')



def redrawAll(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill="black")
    canvas.create_rectangle(app.sideMargin, app.topMargin,
            app.width - app.sideMargin, app.height - app.sideMargin, fill="white", width=0)
    canvas.create_text(app.width//2, app.topMargin//2,
                        text=f"{app.building}'s Virtual Art Installation",
                        font="Georgia 18", fill="white", width=0)
    canvas.create_rectangle(app.sideMargin, app.height - app.sideMargin - app.colorBar,
                        app.width - app.sideMargin, app.height - app.sideMargin, outline="black")
    canvas.create_text(app.sideMargin + 5, app.height - app.sideMargin - app.colorBar/2,
                        text='Color: ', font='Georgia 18', anchor='w')
    canvas.create_rectangle(70, app.height - app.sideMargin - app.colorBar/2 - 9,
                            90, app.height - app.sideMargin - app.colorBar/2 + 11,
                            fill=f'{app.color}')
    canvas.create_rectangle(app.width - app.sideMargin - 130, app.height - app.sideMargin - app.colorBar/2 - 13,
                            app.width - app.sideMargin - 25, app.height - app.sideMargin - app.colorBar/2 + 15,
                            fill='black')
    canvas.create_text(app.width - 130, app.height - app.colorBar/2 - 8,
                        text='Change Color', font='Georgia 14', anchor='w', fill='white')
    canvas.create_oval(app.width - app.sideMargin - 290, app.height - app.sideMargin - app.colorBar/2 - 5,
                            app.width - app.sideMargin - 280, app.height - app.sideMargin - app.colorBar/2 + 5,
                            fill='gray', outline='')
    canvas.create_oval(app.width - app.sideMargin - 262.5, app.height - app.sideMargin - app.colorBar/2 - 7.5,
                            app.width - app.sideMargin - 247.5, app.height - app.sideMargin - app.colorBar/2 + 7.5,
                            fill='gray', outline='')
    canvas.create_oval(app.width - app.sideMargin - 230, app.height - app.sideMargin - app.colorBar/2 - 10,
                            app.width - app.sideMargin - 210, app.height - app.sideMargin - app.colorBar/2 + 10,
                            fill='gray', outline='')
    selectCircle(canvas, app)
    drawDots(app, canvas)
    

runApp(width=450, height=630)