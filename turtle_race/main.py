import turtle
import random
from time import sleep

from presentation import Presentation
from show_turtles import Show_turtles
from players_name import Players_name
from chosen_turtle import Chosen_turtle
from show_avatar import Show_avatar
from countdown import Countdown

turtles_ninjas = ["gifs/Donatello.gif", "gifs/Leonardo.gif",
                  "gifs/Michelangelo.gif", "gifs/Raphael.gif"]

positions = [(100, 100), (-100, 100), (-100, -100), (100, -100)]


def Create_world(world):
    display = turtle.Screen()
    display.bgpic(world)


def Victoria(player):
    player += 100


def Tie(player):
    player += 50


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

        player_1.st()
        player_1.up()
        player_1.goto(-250, -10)
        turtle.up()
        turtle.goto(-250, 85)
        turtle.write('PLAYER 1', False, 'center', secondary_font)

        player_2.st()
        player_2.up()
        player_2.goto(-250, -30)
        turtle.up()
        turtle.goto(-250, -100)
        turtle.write('PLAYER 2', False, 'center', secondary_font)

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

            Victoria(score_player_1)
        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            Victoria(score_player_2)
        else:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            Tie(score_player_1)
            Tie(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 4:
        Create_world('gifs/background-3.gif')

        Countdown()

        player_1.st()
        player_1.up()
        player_1.goto(-250, -90)
        turtle.up()
        turtle.goto(-250, 150)
        turtle.write('PLAYER 1', False, 'center', secondary_font)

        player_2.st()
        player_2.up()
        player_2.goto(-250, -100)
        turtle.up()
        turtle.goto(-250, -180)
        turtle.write('PLAYER 2', False, 'center', secondary_font)

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

            Victoria(score_player_1)
        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            Victoria(score_player_2)
        else:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            Tie(score_player_1)
            Tie(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 3:
        Create_world('gifs/background-4.gif')

        Countdown()

        player_1.st()
        player_1.up()
        player_1.goto(-250, -120)
        turtle.up()
        turtle.goto(-250, 200)
        turtle.write('PLAYER 1', False, 'center', secondary_font)

        player_2.st()
        player_2.up()
        player_2.goto(-250, -150)
        turtle.up()
        turtle.goto(-250, -220)
        turtle.write('PLAYER 2', False, 'center', secondary_font)

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
            turtle.pencolor('red')
            turtle.write('Player 1 venceu!', False, 'center', secondary_font)

            Victoria(score_player_1)
        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('red')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            Victoria(score_player_2)
        else:
            turtle.home()
            turtle.pencolor('red')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            Tie(score_player_1)
            Tie(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 2:
        Create_world('gifs/background-5.gif')

        Countdown()

        player_1.st()
        player_1.up()
        player_1.goto(-250, -90)
        turtle.up()
        turtle.goto(-250, 130)
        turtle.write('PLAYER 1', False, 'center', secondary_font)

        player_2.st()
        player_2.up()
        player_2.goto(-250, -100)
        turtle.up()
        turtle.goto(-250, -160)
        turtle.write('PLAYER 2', False, 'center', secondary_font)

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

            Victoria(score_player_1)
        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            Victoria(score_player_2)
        else:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            Tie(score_player_1)
            Tie(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    elif game == 1:
        Create_world('gifs/background-6.gif')

        Countdown()

        player_1.st()
        player_1.up()
        player_1.goto(-250, 0)
        turtle.up()
        turtle.goto(-250, 80)
        turtle.write('PLAYER 1', False, 'center', secondary_font)

        player_2.st()
        player_2.up()
        player_2.goto(-250, -30)
        turtle.up()
        turtle.goto(-250, -100)
        turtle.write('PLAYER 2', False, 'center', secondary_font)

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

            Victoria(score_player_1)
        elif distance_player_1 < distance_player_2:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('Player 2 venceu!', False, 'center', secondary_font)

            Victoria(score_player_2)
        else:
            turtle.home()
            turtle.pencolor('green')
            turtle.write('EMPATOU!', False, 'center', secondary_font)

            Tie(score_player_1)
            Tie(score_player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    game -= 1
