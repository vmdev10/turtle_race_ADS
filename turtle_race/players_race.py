import turtle
import random


def Victoria(player):
    player += 100


def Tie(player):
    player += 50


secondary_font = ("Comic Sans", 16, "bold")


def Players_race(player1, player2):
    distance_player_1 = 0
    distance_player_2 = 0
    score_player_1 = 0
    score_player_2 = 0

    while distance_player_1 < 500 and distance_player_2 < 500:
        go_player_1 = random.randint(1, 5)
        go_player_2 = random.randint(1, 5)
        distance_player_1 = distance_player_1 + go_player_1
        distance_player_2 = distance_player_2 + go_player_2

        player1.fd(go_player_1)
        player2.fd(go_player_2)

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
