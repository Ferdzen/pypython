#exemplo simples de recursão #1

def sauda(nome):
    print('Olá, '+nome+'!')

    sauda2(nome)
    print('preparando para dizer tchau...')
    tchau()


def sauda2(nome):
    print('Como vai '+nome+'?')


def tchau():
    print('Ok, tchau!')

sauda('Pedro')

#exemplo simples de recursão #2
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

print(fat(3))

#quicksort e ordenação de arrays de qualquer tamanho
#use caso base e caso recursivo - Recursão!
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <=pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

print(quicksort([10,5,2,3]))