#Entrando em o que é Hash. Utilização:

#exemplo simples de hash #1
caderno = dict()

caderno["Maçã"] = 0.67
caderno["Leite"] = 1.49
caderno["Abacate"] = 1.49

#exemplo simples de hash #2
lista_telefonica = {}

lista_telefonica["Jenn"] = 87654321
lista_telefonica["Emergency"] = 190

#Fazendo verificação de item utilizando Hash

votou = {}
def verifica_eleitor(nome):
    if votou.get(nome):
        print('Mande embora!')
    else:
        votou[nome] = True
        print('Deixe votar!')

ligado = True
while ligado:
    print('Insira seu nome:')
    nome = input()
    if nome == '0':
        ligado = False
    else:
        verifica_eleitor(nome)

print('Votos registrados:')
print(votou)