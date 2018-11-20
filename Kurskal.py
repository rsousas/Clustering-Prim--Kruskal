# -*- coding: UTF-8 -*-
import sys

subgrupo = dict() # Armazena os rotulos de cada grupo Ex.: {A:B,B:B,C:C}, os verties A e B estao no mesmo subconjunto
classif = dict()  # Armazena a quantidade de elementos rotulados para cada vertices, util para balanceamento dos subconjuntos

# Povoa as variaveis. vertices armazena os vertices existentes. 
def make_set(grafo):
  vertices = list()
  
  for linha in grafo:
    if not (linha[1] in vertices):
      vertices.append(linha[1])
    subgrupo[linha[1]] = linha[1]
    classif[linha[1]] = 1
  
  return vertices

# Encontra o rotulo raiz de um elemento 
def find(vertice):
  if subgrupo[vertice] != vertice: 
    subgrupo[vertice] = find(subgrupo[vertice]) 
  return subgrupo[vertice]

# Une dois vertices se eles nao pertencerem ao mesmo subconjunto
def union(vertice1, vertice2):
  v1_rotulo = find(vertice1)
  v2_rotulo = find(vertice2)
  
  if v1_rotulo != v2_rotulo:
    if classif[v1_rotulo] > classif[v2_rotulo]: # Balanceando os subconjuntos
      subgrupo[v2_rotulo] = v1_rotulo
      classif[v1_rotulo] += classif[v2_rotulo]
    else:
      subgrupo[v1_rotulo] = v2_rotulo
      classif[v2_rotulo] += classif[v1_rotulo]


def kruskal(grafo, vertices, k_clusters):
  MST = list()
  
  clusters = len(vertices)

  for aresta in grafo:
    peso, vertice1, vertice2 = aresta
    if clusters <= k_clusters: # Verifica se existem k subconjuntos (evita problema caso K seja maior que o possivel de subconjuntos)
      break

    if find(vertice1) != find(vertice2): #Caso nao pertencerem ao mesmo subconjunto, une os vertices, adiciona a MST e ajusta o contador de conjuntos
      union(vertice1, vertice2)
      MST.append(aresta)
      clusters -= 1
  
# Re-rotula os vertices para serem representados pelos vertices raiz
def rotule(raiz):
  def rerotule(vertice):
    for j in subgrupo.items():
          if j[1] != j[0] and j[1] == vertice: # Verifica se existem vertices rotulads com o vertice do parametro
            subgrupo[j[0]] = v  # Re-rotula
            rerotule(j[0])
  i = list()
  j = list()
  for v in raiz:
    for i in subgrupo.items(): 
      if i[1] == v: # Verifica se existem vertices com rotulo sendo o vertice raiz
        rerotule(i[0])

# Ordena os registros para saida
def order_out_data():
  rotulos = list()
  raiz = list()
  
  for i, j in subgrupo.items(): # Encontra os vertices raiz
    if i == j:
      raiz.append(i)
  rotule(raiz)
  
  try:
    for i, j in subgrupo.items():
      rotulos.append([int(i), int(j)])
  except:
    for i, j in subgrupo.items():
      rotulos.append([i, j])
  
  rotulos.sort()
  
  for i in rotulos:
    print i
  
  return rotulos

# Povoa as listas com os dados lidos do arquivo informado
def Dict_Arestas(lista):
  grafo = list() # Povoa grafo com as arestas existentes e ordenado por seus respectivos pesos
  
  for j in range(len(lista)):
    i = lista[j].split()
    grafo.append([float(i[2]), i[0], i[1]])
  
  vertices = make_set(grafo)
  grafo.sort()
  
  return grafo, vertices


try:
  elements = sys.argv[1]
except IndexError:
  elements = 'teste.txt'

try:
  k_clusters = int(sys.argv[2])
except IndexError:
  print 'Informe a quantidade de grupos!'
  sys.exit()
  
dados = open(elements, "r")
lista = dados.readlines()  

grafo, vertices = Dict_Arestas(lista)
kruskal(grafo, vertices, k_clusters)
order_out_data()

