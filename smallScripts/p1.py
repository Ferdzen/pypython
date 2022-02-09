##Jogando um dado e exibindo ao usuário o resultado

from random import randint

def jogando_dado():
    jogada = True
    while jogada:
        print('Você jogou o dado. O resultado foi - ', randint(1,6))
        print('Deseja jogar novamente? s ou n para resposta.')
        resp2 = input()

        if resp2 == 's':
            jogada = True
        elif resp2 == 'n':
            jogada = False
        else:
            print('Resposta não registrada no banco de dados. Encerrando programa.')
            jogada = False

print('Você quer jogar o dado? s ou n para resposta.')
resp = input()

if resp == 's':
    jogando_dado()
elif resp == 'n':
    print('Encerrando programa')
    exit()
else:
    print('Resposta não registrada no banco de dados. Encerrando programa.')