from turtle import *
import random
from time import sleep

colors = ['green', 'yellow', 'orange red', 'black', 'white', 'red', 'blue']


def Text_presentation(text):
    for i in range(5):
        ht()

        color = random.choice(colors)
        sleep(0.25)

        pencolor(color)
        font = ("Comic Sans", 30, "bold")
        write(text, False, 'center', font)
