import turtle
from time import sleep

from presentation import Presentation
from show_turtles import Show_turtles
from players_name import Players_name
from chosen_turtle import Chosen_turtle
from show_avatar import Show_avatar
from countdown import Countdown
from coordinates_player_1 import Coordinates_player_1
from coordinates_player_2 import Coordinates_player_2
from players_race import Players_race

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

        Players_race(player_1, player_2)

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

        Players_race(player_1, player_2)

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

        Players_race(player_1, player_2)

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

        Players_race(player_1, player_2)

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

        Players_race(player_1, player_2)

        sleep(3)
        turtle.clear()
        player_1.reset()
        player_1.hideturtle()
        player_2.reset()
        player_2.hideturtle()

    game -= 1

window = turtle.Screen()
window.exitonclick()
