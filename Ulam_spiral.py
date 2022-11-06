# Ulam Spiral
from tkinter import *
from turtle import width
from math import sqrt


top = Tk()
top.title("Ulam's Spiral")
top.geometry('500x500')
w, h = 500, 500

# creating canvas
c = Canvas(top, bg = 'white', height = h, width = w)

def isPrime(value):
    i = 2
    primey = True
    while i <= sqrt(value):
        if (value % i == 0):
            primey = False

        i+=1
    
    return primey

def draw():
    step = 1
    stepSize = 40
    numSteps = 1
    state = 0
    turnCounter = 0
    x = w/2
    y = h/2

    for i in range(1000):
        if (isPrime(step)):
            c.create_text(x, y,font=('bold'), text=step, fill="blue")
        elif state == 0:
            c.create_text(x, y,font=("Purisa", 16), text='→', fill="black")
        elif state == 1:
            c.create_text(x, y,font=("Purisa", 16), text='↑', fill="black")
        elif state == 2:
            c.create_text(x, y,font=("Purisa", 16), text='←', fill="black")
        elif state == 3:
            c.create_text(x, y,font=("Purisa", 16), text='↓', fill="black")

        match state:
            case 0:
                x += stepSize   # move right
            case 1:
                y -= stepSize   # move up
            case 2:
                x -= stepSize   # move left
            case 3:
                y += stepSize   # move down

        if (step % numSteps == 0):
            state = (state + 1) % 4
            turnCounter += 1
            if (turnCounter % 2 == 0):
                numSteps += 1
        step += 1

c.pack()
draw()
top.mainloop()



