import turtle

turtles_ninjas = ["gifs/Donatello.gif", "gifs/Leonardo.gif",
                  "gifs/Michelangelo.gif", "gifs/Raphael.gif"]

positions = [(-100, 100), (100, 100), (-100, -100), (100, -100)]


def Show_turtles():
    turtle.penup()

    for turtle_ninja, position in zip(turtles_ninjas, positions):
        turtle.register_shape(turtle_ninja)
        turtle.shape(turtle_ninja)
        turtle.setpos(position)
        turtle.stamp()
