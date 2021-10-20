import turtle

turtles_ninjas = ["gifs/Donatello.gif", "gifs/Leonardo.gif",
                  "gifs/Michelangelo.gif", "gifs/Raphael.gif"]


def Show_avatar(player, person):

    turtle.register_shape(turtles_ninjas[person - 1])
    player.shape(turtles_ninjas[person - 1])
    player.stamp()

    return player
