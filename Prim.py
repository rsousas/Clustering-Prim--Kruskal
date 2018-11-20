# -*- coding: UTF-8 -*-
import sys
import time

MAX = 100000000 # Constante para ajustar variavel 'menor'

# Retorna a Minimum Spanning Tree utilizando o metodo de Prim
def MST_Prim(grafo_adj, ini):
  vertices = list()
  arestas = dict()
  MST = list()
  visitados = list()
  
  while True:  
    visitados.append(ini) # Armazena os vertices ja visitados
    for i in grafo_adj[ini]: # Adiciona as arestas conhecidas com excecao das que ligam a vertices ja visitados e substituindo por arestas de menor valor
      if (i not in vertices) and (i not in visitados): 
        vertices.append(i)
      if i in arestas:
        if arestas[i][0] > grafo_adj[ini][i]:
          arestas[i] = grafo_adj[ini][i], ini
      else:
        arestas[i] = grafo_adj[ini][i], ini

    menor = (MAX, '-')
    for i in vertices: # Encontra a menor aresta entre as arestas conhecidas
     if arestas[i][0] < menor[0]:
       menor = (arestas[i][0], i)
  
    MST.append([menor[0], arestas[menor[1]][1], menor[1]]) # Adiciona a aresta a MST
    arestas.pop(menor[1]) # Remove das arestas conhecidas
    vertices.remove(menor[1]) # Remove da lista de vertices existentes
    ini = menor[1] # Armazena o vertice encontrado para adicionar as novas arestas conhecidas

    if not vertices: # Caso nao existam mais vertices, ou seja, todos ja tenham sido 'visitados' para o algoritmo
      break
  
  return MST

# Realiza o processo de agrupamento
def removeEdges(clusters, k):
  clusters.sort()  # Ordena o grupo contendo o MST, pelo valor da aresta
  for i in range(0,k-1): # Remove, a partir da maior aresta, K-1 arestas
    try:
      clusters.pop(len(clusters)-1)
    except:
      break
  return clusters
  
# Rotula os vertices e os Re-rotula para serem representados pelos vertices raiz
def rotule(clusters, rotulos):
  def rerotule(vertice):
    for j in rotulos.items():
          if j[1] != j[0] and j[1] == vertice: # Verifica se existem vertices rotulads com o vertice do parametro
            rotulos[j[0]] = v  # Re-rotula
            rerotule(j[0])
  raiz = list()
  i = list()
  j = list()
  
  for aresta in clusters: # Para cada aresta dos subconjuntos, rotula o segundo vertice com o primeiro, ou rotulo deste
    if rotulos[aresta[1]] == aresta[1]:
      rotulos[aresta[2]] = aresta[1]
    else:
      rotulos[aresta[2]] = rotulos[aresta[1]]
  
  for i, j in rotulos.items(): # Encontra os vertices raiz
    if i == j:
      raiz.append(i)
  
  for v in raiz:
    for i in rotulos.items(): 
      if i[1] == v: # Verifica se existem vertices com rotulo sendo o vertice raiz
        rerotule(i[0])
  
  return rotulos
  
# Ordena os registros para saida
def order_out_data(rotulos):
  rotulos_list = list()
  try:
    for i, j in rotulos.items():
      rotulos_list.append([int(i), int(j)])
  except:
    for i, j in rotulos.items():
      rotulos_list.append([i, j])
  
  rotulos_list.sort()
  
  for i in rotulos_list:
    print i
  
  return rotulos_list
  
# Povoa as listas com os dados lidos do arquivo informado
def Dict_Arestas(lista):
  list_adj = dict() # Povoa grafo com as arestas existentes e ordenado por seus respectivos pesos
  grafo_adj = dict() # Grafo contendo as adjascencias entre os vertices, ou seja, as arestas conhecidas por cada vertice
  grafo = list()
  rotulos = dict() # Prepara a lista de rotulos com todos os vertices
  
  v = lista[0].split()
  vertice = v[0]
  
  for j in range(len(lista)):
    i = lista[j].split() 
    if i[0] == vertice:
      list_adj[i[1]] = float(i[2])
      continue
    grafo_adj[vertice] = list_adj
    vertice = i[0]
    list_adj = {}
    list_adj[i[1]] = float(i[2])
  grafo_adj[vertice] = list_adj
  
  for j in range(len(lista)):
    i = lista[j].split()
    grafo.append([float(i[2]), i[0], i[1]])
  grafo.sort()
  
  for linha in grafo:
    rotulos[linha[1]] = linha[1]
  
  return grafo, grafo_adj, rotulos
   
try:
  elements = sys.argv[1]
except IndexError:
  elements = 'teste.txt'

try:
  ini = sys.argv[2]
except IndexError:
  print 'Informe o vertice inicial!'
  sys.exit()
  
try:
  k_clusters = int(sys.argv[3])
except IndexError:
  print 'Informe a quantidade de grupos!'
  sys.exit()
  
dados = open(elements, "r")
lista = dados.readlines()  

grafo, grafo_adj, rotulos = Dict_Arestas(lista)

#ini = grafo[0][1]

MST = MST_Prim(grafo_adj, ini)
clusters = removeEdges(MST, k_clusters)
rotulos = rotule(clusters, rotulos)
order_out_data(rotulos)

