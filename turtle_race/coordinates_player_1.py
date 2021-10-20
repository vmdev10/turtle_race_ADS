import turtle

secondary_font = ("Comic Sans", 16, "bold")


def Coordinates_player_1(player, playerX, playerY, textX, textY):
    player.st()
    player.up()
    player.goto(playerX, playerY)
    turtle.up()
    turtle.goto(textX, textY)
    turtle.write('PLAYER 1', False, 'center', secondary_font)
