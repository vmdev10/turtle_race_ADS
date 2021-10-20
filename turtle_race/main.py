import turtle
import random
from time import sleep

from presentation import Presentation
from show_turtles import Show_turtles
from players_name import Players_name
from chosen_turtle import Chosen_turtle
from show_avatar import Show_avatar
from countdown import Countdown
from coordinates_player_1 import Coordinates_player_1
from coordinates_player_2 import Coordinates_player_2

turtles_ninjas = ["gifs/Donatello.gif", "gifs/Leonardo.gif",
                  "gifs/Michelangelo.gif", "gifs/Raphael.gif"]

positions = [(100, 100), (-100, 100), (-100, -100), (100, -100)]


def Create_world(world):
    display = turtle.Screen()
    display.bgpic(world)


Create_world('gifs/background.gif')

font = ("Comic Sans", 30, "bold")

secondary_font = ("Comic Sans", 16, "bold")

player_1 = turtle.Turtle()
player_2 = turtle.Turtle()

score_player_1 = 0
score_player_2 = 0


def Turtle_color(player):
    if player == 1:
        color = 'purple'
    elif player == 2:
        color = 'blue'
    elif player == 3:
        color = 'orange'
    elif player == 4:
        color = 'red'

    return color


Presentation()

player_name_1 = Players_name()

Show_turtles()

person_player_1 = Chosen_turtle()

turtle.reset()
turtle.hideturtle()

player_1 = Show_avatar(player_1, person_player_1)
turtle.penup()
turtle.left(90)
turtle.fd(60)

turtle.pencolor(Turtle_color(person_player_1))
turtle.write('PLAYER 1', False, 'center', font)

sleep(3)
turtle.clear()
player_1.reset()
player_1.hideturtle()
turtle.home()


Presentation()

player_name_2 = Players_name()

Show_turtles()

person_player_2 = Chosen_turtle()

turtle.reset()
turtle.hideturtle()

player_2 = Show_avatar(player_2, person_player_2)
turtle.left(90)
turtle.fd(60)

turtle.pencolor(Turtle_color(person_player_2))
turtle.write('PLAYER 2', False, 'center', font)

sleep(3)
turtle.clear()
player_2.reset()
player_2.hideturtle()

game = 5

while game > 0:
    if game == 5:
        Create_world('gifs/background-2.gif')

        Countdown()

        Coordinates_player_1(player_1, -250, -10, -250, 85)
        Coordinates_player_2(player_2, -250, -30, -250, -100)

        distance_player_1 = 0
        distance_player_2 = 0

        while distance_player_1 < 500 and distance_player_2 < 500:
            go_player_1 = random.randint(1, 5)
            go_player_2 = random.randint(1, 5)
            distance_player_1 = distance_player_1 + go_player_1
            distance_player_2 = distance_player_2 + go_player_2

            player_1.fd(go_player_1)
            player_2.fd(go_player_2)

        if distance_player_1 > distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 100
            print(score_player_1)

        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            score_player_2 = score_player_2 + 100
            print(score_player_2)

        else:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 50
            score_player_2 = score_player_2 + 50
            print(score_player_1, score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 4:
        Create_world('gifs/background-3.gif')

        Countdown()

        Coordinates_player_1(player_1, -250, -90, -250, 150)
        Coordinates_player_2(player_2, -250, -100, -250, -180)

        distance_player_1 = 0
        distance_player_2 = 0

        while distance_player_1 < 500 and distance_player_2 < 500:
            go_player_1 = random.randint(1, 5)
            go_player_2 = random.randint(1, 5)
            distance_player_1 = distance_player_1 + go_player_1
            distance_player_2 = distance_player_2 + go_player_2

            player_1.fd(go_player_1)
            player_2.fd(go_player_2)

        if distance_player_1 > distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 100
            print(score_player_1)

        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            score_player_2 = score_player_2 + 100
            print(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 3:
        Create_world('gifs/background-4.gif')

        Countdown()

        Coordinates_player_1(player_1, -250, -120, -250, 200)
        Coordinates_player_2(player_2, -250, -150, -250, -220)

        distance_player_1 = 0
        distance_player_2 = 0

        while distance_player_1 < 500 and distance_player_2 < 500:
            go_player_1 = random.randint(1, 5)
            go_player_2 = random.randint(1, 5)
            distance_player_1 = distance_player_1 + go_player_1
            distance_player_2 = distance_player_2 + go_player_2

            player_1.fd(go_player_1)
            player_2.fd(go_player_2)

        if distance_player_1 > distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 100
            print(score_player_1)

        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            score_player_2 = score_player_2 + 100
            print(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 2:
        Create_world('gifs/background-5.gif')

        Countdown()

        Coordinates_player_1(player_1, -250, -90, -250, 130)
        Coordinates_player_2(player_2, -250, -100, -250, -160)

        distance_player_1 = 0
        distance_player_2 = 0

        while distance_player_1 < 500 and distance_player_2 < 500:
            go_player_1 = random.randint(1, 5)
            go_player_2 = random.randint(1, 5)
            distance_player_1 = distance_player_1 + go_player_1
            distance_player_2 = distance_player_2 + go_player_2

            player_1.fd(go_player_1)
            player_2.fd(go_player_2)

        if distance_player_1 > distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 100
            print(score_player_1)

        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            score_player_2 = score_player_2 + 100
            print(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 1:
        Create_world('gifs/background-6.gif')

        Countdown()

        Coordinates_player_1(player_1, -250, 0, -250, 80)
        Coordinates_player_2(player_2, -250, -30, -250, -100)

        distance_player_1 = 0
        distance_player_2 = 0

        while distance_player_1 < 500 and distance_player_2 < 500:
            go_player_1 = random.randint(1, 5)
            go_player_2 = random.randint(1, 5)
            distance_player_1 = distance_player_1 + go_player_1
            distance_player_2 = distance_player_2 + go_player_2

            player_1.fd(go_player_1)
            player_2.fd(go_player_2)

        if distance_player_1 > distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            score_player_1 = score_player_1 + 100
            print(score_player_1)

        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            score_player_2 = score_player_2 + 100
            print(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    game -= 1


Create_world('gifs/background.gif')
Presentation()

turtle.penup()
turtle.right(90)
turtle.fd(25)
turtle.pendown()

turtle.write('PLACAR:', False, 'center', secondary_font)

turtle.penup()
turtle.fd(25)

turtle.write(f'PLAYER 1: {score_player_1}',
             False, 'center', secondary_font)

turtle.penup()
turtle.fd(25)

turtle.write(f'PLAYER 2: {score_player_2}',
             False, 'center', secondary_font)

window = turtle.Screen()
window.exitonclick()
