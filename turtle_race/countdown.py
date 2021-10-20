import turtle
from time import sleep

font = ("Comic Sans", 30, "bold")


def Countdown():
    turtle.write('3', False, 'center', font)
    sleep(1)
    turtle.clear()
    turtle.write('2', False, 'center', font)
    sleep(1)
    turtle.clear()
    turtle.write('1', False, 'center', font)
    sleep(1)
    turtle.clear()
    turtle.write('JÁÁ!!!', False, 'center', font)
    sleep(1)
    turtle.clear()
