import turtle
secondary_font = ("Comic Sans", 16, "bold")


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
