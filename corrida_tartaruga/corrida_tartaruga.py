import turtle
import random
from time import sleep


turtles_ninjas = ["Donatello.gif", "Leonardo.gif",
                  "Michelangelo.gif", "Raphael.gif"]

positions = [(100, 100), (-100, 100), (-100, -100), (100, -100)]

display = turtle.Screen()
display.bgpic("background.gif")

colors = ['green', 'yellow', 'orange red', 'black', 'white', 'red', 'blue']

font = ("Comic Sans", 30, "bold")

secondary_font = ("Comic Sans", 16, "bold")


def Presentation():
    for i in range(5):
        turtle.ht()
        color = random.choice(colors)
        sleep(0.25)
        turtle.pencolor(color)
        turtle.write('CORRIDA NINJA', False, 'center', font)


def Show_person():
    turtle.penup()

    for turtle_ninja, position in zip(turtles_ninjas, positions):
        turtle.register_shape(turtle_ninja)
        turtle.shape(turtle_ninja)
        turtle.setpos(position)
        turtle.stamp()


def Players_name():
    name = ''
    while len(name) == 0:
        name = turtle.textinput('CORRIDA NINJA', 'Nome do jogador: ')

        turtle.penup()
        turtle.right(90)
        turtle.fd(25)
        turtle.pendown()

        turtle.write('Olá, ' + name, False, 'center', secondary_font)

        turtle.penup()
        turtle.fd(25)

        turtle.write('Escolha seu personagem:',
                     False, 'center', secondary_font)

    return name


def Chosen_person():
    player = int(turtle.textinput('Escolha o seu personagem: ',
                 '(1 - Leonardo, 2 - Donatello, 3 - Michelangelo, 4 - Raphael) '))

    return player


def ShowTurtle(person):
    turtle.register_shape(turtles_ninjas[person])
    turtle.shape(turtles_ninjas[person - 1])
    turtle.stamp()


Presentation()

player_1 = Players_name()

Show_person()

person_player_1 = Chosen_person()

turtle.reset()
turtle.hideturtle()

ShowTurtle(person_player_1)
turtle.write('PLAYER 1', False, 'center', font)

sleep(3)
turtle.reset()
turtle.hideturtle()

Presentation()

player_2 = Players_name()

Show_person()

person_player_2 = Chosen_person()

turtle.reset()
turtle.hideturtle()

ShowTurtle(person_player_2)
turtle.write('PLAYER 1', False, 'center', font)
sleep(3)
turtle.reset()
turtle.hideturtle()

# my_turtle.hideturtle()
# turtle.reset()

# showTurtle(player_1)

# turtle.hideturtle()

# for i in range(5):
#   turtle.ht()
#   color = random.choice(colors)
#   sleep(0.25)
#   turtle.pencolor(color)
#   font = ("Comic Sans", 30, "bold")
#   turtle.write('CORRIDA NINJA', False, 'center', font)

# name_player_2 = ''

# while len(name_player_2) == 0:
#   name_player_2 = turtle.textinput('CORRIDA NINJA', 'Nome do jogador: ')

# turtle.penup()
# turtle.right(90)
# turtle.fd(25)
# turtle.pendown()

# secondary_font = ("Comic Sans", 16, "bold")
# turtle.write('Olá, '+ name_player_2, False, 'center',secondary_font)

# turtle.penup()
# turtle.fd(25)

# turtle.write('Escolha seu personagem:', False, 'center',secondary_font)

# my_turtle.penup()

# sleep(1)

# for turtle_ninja, position in zip(turtles_ninjas, positions):
#     turtle.register_shape(turtle_ninja)
#     my_turtle.shape(turtle_ninja)
#     my_turtle.setpos(position)
#     my_turtle.stamp()

# player_2 = int(turtle.textinput('Escolha o seu personagem: ', '(1 - Leonardo, 2 - Donatello, 3 - Michelangelo, 4 - Raphael) '))


# showTurtle(player_2)
