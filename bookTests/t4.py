#grafos ponderados(também conhecido como grafos valorados)
#algoritmos de Dijkstra


#Grafos ponderados adicionam peso as arestas
#Pesquisa em largura encontra o caminho mais curto, algoritmo de Dijkstra encontra o mais rápido
#Algoritmo de Dijkstra:
    #Encontre o vértice mais "barato", o que consegue chegar em menor tempo possível.
    #Verifique se há caminho mais barato para os vizinhos desse vértice, caso exista, atualize os custos deles.
    #Repita até que tenha feito isso para cada vértice do grafo
    #Calcule o caminho final
#Arestas com pesos negativos: o algoritmo de Dijkstra não funciona com eles. O mais indicado é o Algoritmo de Bellman-Ford.

#tabela pai: tabela onde se registra por qual ponto de partida você utilizada para chegar no ponto desejado.
    #ex: para chegar ao vértice A existe dois caminhos, partindo diretamente do Inicio é um deles. O segundo
    #é partindo do ponto B. O caminho mais curto é o primeiro, porém, o mais rápido é o segundo. Logo, opta-se
    #pelo caminho que se parte do ponto B. Na tabela pai, registra-se que B é pai de A.


#Implementando o algoritmo de Dijkstra
#utilizando tabelas hash para manipular os grafos
grafo = {}

#registrando o vértice inicio, seus vizinhos e o custo para chegar em cada um
grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2

#registrando o vértice 'a', seus vizinhos e o custo para chegar em cada um
grafo["a"] = {}
grafo["a"]["fim"] = 1

#registrando o vértice 'b', seus vizinhos e o custo para chegar em cada um
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

#registrando o vértice fim, ele não tem vizinhos
grafo["fim"] = {}

#tabela hash para registrar os custos de um ponto a outro
infinito = float("inf")
custos = {}

custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#tabela hash para os pais
pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

#array para registrar os vértices processados
processados = []

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None

    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

print('Vértices e seus vizinhos: ', grafo)
print('Custos: ', custos)
print('Pais de cada vértice: ', pais)
