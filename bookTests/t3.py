#Estudando grafos e pesquisa em largura!
#Grafo: conjunto de conexões
#Para descobrir como resolver um problema:
    #Modele-o com grafo.
    #Resolva-o com pesquisa em largura.

from collections import deque

#criando grafo utilizando o hash
grafo = {}
grafo["voce"] = ["maddy", "joy", "bob"]
grafo["bob"] = ["maicom", "julien"]
grafo["maddy"] = ["julien"]
grafo["joy"] = ["yeri", "seulgi"]
grafo["maicom"] = []
grafo["julien"] = []
grafo["yeri"] = []
grafo["seulgi"] = []



#função para determinar qual é o vendedor de manga.
def pessoa_e_vendedor(nome):
    return nome[-1] == 'm' #nome que termine com a letra setada

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo["voce"]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft() #pega a primeira pessoa da fila
        if not pessoa in verificadas: #verifica se o nome já não foi checado
            if pessoa_e_vendedor(pessoa): #verifica se essa pessoa vende manga
                print(pessoa +' é vendedor de manga!') #sim, ela vende manga
                return True #finaliza programa
            else:
                fila_de_pesquisa += grafo[pessoa] #não, ela nao vende manga. adiciona todos os amigos dessa pessoa à lista
                verificadas.append(pessoa) #adiciona ao vetor o nome verificado para que não seja feita checagem 2 vezes
    return False

pesquisa("voce")