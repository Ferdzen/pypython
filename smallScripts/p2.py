# Adivinhe o número que será gerado.
from random import randint

print('Adivinhe o número!')
print('Deseja jogar?')
resp = input()

game = True

numg = randint(0, 100)
print('Número gerado!')
cont = 0

while (game):
    print('ADIVINHE!')
    print('Qual número foi gerado?')
    chute = float(input())
    cont = cont + 1

    result = numg - chute

    if result > 0:
        if 0 < result <= 5:
            print('Quase! Muito quente!')
        elif 6 <= result <= 10:
            print('Chegando perto! Está quente!')
        elif 11 <= result <= 15:
            print('Está esquentando. Morno!')
        elif 16 <= result <= 20:
            print('Vish... Frio...')
        elif result > 21:
            print('O polo sul é logo ali. Frio rapaz, mas MUITO frio.')
    elif result < 0:
        if -5 <= result <= -1:
            print('Quase! Muito quente!')
        elif -10 <= result <= -6:
            print('Chegando perto! Está quente!')
        elif -15 <= result <= -11:
            print('Está esquentando. Morno!')
        elif -20 <= result <= -16:
            print('Vish... Frio...')
        elif result < -21:
            print('O polo sul é logo ali. Frio rapaz, mas MUITO frio.')
    elif result == 0:
        print('Parabéns. Você conseguiu adivinhar qual foi o número gerado, com um total de ', cont, ' tentativas.')
        exit()

    print('Deseja tentar novamente? s ou n.')
    resp2 = input()

    if resp2 == 's':
        game = True
    else:
        game = False

if game == False and numg != chute:
    print('Infelizmente você desistiu :( mesmo ', cont, ' tentativas não foram suficientes.\nO número gerado '
                                                        'foi:', numg)
