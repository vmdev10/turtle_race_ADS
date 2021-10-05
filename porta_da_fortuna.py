import random

print('''
            Porta da Fortuna

Existe um super prêmio atrás de um destas 3 portas!
Advinhe qual é a porta certa para ganhar o prêmio!
 _______   _______   _______
|       | |       | |       |
|  [1]  | |  [2]  | |  [3]  |
|       | |       | |       |
|       | |       | |       |
 -------   -------   -------

'''
      )

allowed_doors = [1, 2, 3]
# Lista de prêmios
list_of_prizes = ['Apple MacBook Air', 'Notebook Gamer Acer Nitro 5',
                  'Monitor Dell Alienware', 'Xbox One X', 'iPhone 12 Pro Apple',
                  'Headphone Sony', 'Echo Dot (4ª Geração) - ALEXA', 'TECLADO GAMER MECÂNICO ALIENWARE LOW PROFILE RGB AW510K',
                  'Chevrolet Onix Plus 0 Km', 'PC Gamer Fácil Intel Core i5 9400F (Nona Geração)']


# A variável responsável por iniciar uma nova partida se retornada true
try_again = 'SIM'

while (try_again == 'SIM'):
    # A 'vida', ou seja, o total de chances do jogador
    life = 2

    # Estou na mesma partida, portanto a porta premiada e o prêmio escolhido permanecem o mesmo até o final da partida.
    # Número aleatório entre o intervalo de 1 e 3 para ser a porta premiada
    award_winning_door = random.randint(1, 3)

    # Um prêmio aleatório da lista list_of_prizes
    prize_drawn = random.choice(list_of_prizes)

    while (life > 0):

        chosen_door = int(input('Escolha uma porta entre 1, 2 e 3: '))

        # Se a porta escolhida NÃO for encontrada dentro da lista allowed_doors (portas permitidas)
        if (chosen_door not in allowed_doors):
            print('Essa porta não existe!')

        # Se a porta escolhida for igual a porta premiada
        elif (chosen_door == award_winning_door):
            print('''
           ______                             __        __      __  _
          / ____/___  ____  ____ __________ _/ /___  __/ /___ _/ /_(_)___  ____  _____
         / /   / __ \/ __ \/ __ `/ ___/ __ `/ __/ / / / / __ `/ __/ / __ \/ __ \/ ___/
        / /___/ /_/ / / / / /_/ / /  / /_/ / /_/ /_/ / / /_/ / /_/ / /_/ / / / (__  )
        \____/\____/_/ /_/\__, /_/   \__,_/\__/\__,_/_/\__,_/\__/_/\____/_/ /_/____/
            ''')

            print('Você acertou a porta premiada!!!')
            print('E ganhou um', prize_drawn)
            break
        # Se a porta escolhida for encontrada dentro da lista de allowed_doors (portas permitidas)
        # mas não for igual a porta premiada
        else:
            life -= 1
            if (life == 1):
                print('Porta errada! Você tem mais uma chance')

            else:
                print('GAME OVER')
    try_again = str(input('Iniciar nova partida? Sim ou Não?: ')).upper()
