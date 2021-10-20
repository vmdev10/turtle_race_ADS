import turtle
import random
from time import sleep

colors = ['green', 'yellow', 'orange red', 'black', 'white', 'red', 'blue']
font = ("Comic Sans", 30, "bold")


def Presentation():
    for i in range(5):
        turtle.ht()
        color = random.choice(colors)
        sleep(0.25)
        turtle.pencolor(color)
        turtle.write('CORRIDA NINJA', False, 'center', font)
