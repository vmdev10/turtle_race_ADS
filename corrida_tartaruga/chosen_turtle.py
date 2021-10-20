import turtle


def Chosen_turtle():
    player = int(turtle.textinput('Escolha o seu personagem: ',
                 '(1 - Leonardo, 2 - Donatello, 3 - Michelangelo, 4 - Raphael) '))

    return player
