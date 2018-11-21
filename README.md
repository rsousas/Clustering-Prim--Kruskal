# Clustering-Prim--Kruskal
Árvores Geradoras Mínimas aplicadas a Agrupamento de Dados
Algoritmos desenvolvidos em Python.

### 1. Como executa-los via terminal:

##### Prim:
Python Prim.py (algum arquivo de dados que possua  AB BA) (Vertice inicio) (Quantidade de Clusters)
Ex.: Python Prim.py dados.txt 2 3


##### Kruskal:
Python Kruskal.py (algum arquivo de dados que possua  AB BA) (Quantidade de Clusters)
Ex.: Python Kruskal.py dados.txt 3


### 2. Descrição

Algoritmos para induzir Árvore Geradora Mínima (do inglês, Minimum Spanning Tree (MST)) a
partir de um grafo G(V;A) são amplamente utilizados em vários cenários de aplicação. Um deles
é conhecido como Agrupamento de Dados.
Agrupamento de Dados (ou Clustering) é uma técnica de análise de padrões em dados que
descreve um conjunto de objetos em uma coleção de grupos (clusters) distintos. A intuição dessa
técnica é determinar que objetos que são mais parecidos entre si sejam colocados em um mesmo
grupo.
Exemplo de agrupamento: https://goo.gl/Sffi2V.
Os objetos agrupados podem ser diversos, como imagens, documentos, itens de compras, entre
vários outros. Nesse sentido, dado um conjunto de algum desses tipos de objetos, é necessário
utilizar métricas que indiquem a (dis)similaridade entre os objetos do conjunto. As medidas de
distância (e.g., euclidiana) são comumente utilizadas para este cenário.
A ideia aplicar funções de distância entre pares de objetos de um conjunto de dados é de
mostrar que quanto maior a distância entre eles, maior será a possibilidade de eles pertencerem a 
grupos distintos. Em contrapartida, quanto menos distantes, maiores são as chances desses pares
de objetos serem do mesmo grupo.

**Agrupamento de Espaçamentos Máximos:** Árvores Geradoras Mínimas são excelentes ferramentas
para representar a intuição de agrupamento de objetos descrita anteriormente. Supondo
que exista um conjunto X = {x1, x2, ..., xn} composto por n objetos distintos. Para cada objeto xi
e xj , em que i != j, existe uma distância d(xi, xj) > 0. Adicionalmente, essa distância é simétrica,
isto é d(xi, xj) = d(xj, xi).
Supondo que X possa ser dividido em k grupos (k-agrupamento), em que k >= 2. Então, podese
dizer que os k grupos obtidos fazem parte de uma partição de grupos não vazios C1, ..., Ck.
Neste contexto, o k-agrupamento de espaçamento é definido como sendo a distância mínima entre
qualquer par de pontos situados em diferentes grupos. Dado que queremos que os pontos em
diferentes grupos estejam distantes um do outro, um objetivo natural é buscar o k-agrupamento
com o máximo espaçamento possível.
Para encontrar o agrupamento de espaçamento máximo, consideramos que os objetos de um
conjunto de dados são representados por um grafo G(V;A), em que V é o conjunto de vértices
(objetos) e A o conjunto de arestas ponderadas pelas distâncias entre cada par de vértice em V .
Esse grafo é construído “iterativamente” com a determinação e inserção de arestas de menor peso
(distância d(xi, xj)) em uma Árvore Geradora mínima. O processo de k-agrupamento termina
quando k componentes conectados do grafo G são encontrados. Assim, esses mesmos componentes
são considerados como grupos. Como exemplo, pode-se observar a Figura 2.
Figure 2: Exemplo de grupos (componentes) distintos no grafo.


#### 2.1 k-agrupamento pelo Algoritmo de Kruskal

A ideia geral para encontrar k-agrupamento por meio do algoritmo de Kruskal é determinar (pelo
usuário) o número de grupos (componentes) que se deseja encontrar no conjunto de dados (grafo).
Então, “unir” iterativamente, cada aresta de menor peso (distância) e contabilizar/registrar quantos
componentes existem em cada iteração do algoritmo. O processo iterativo termina quando são
obtidos k grupos (componentes).


#### 2.2 k-agrupamento pelo Algoritmo de Prim

Para obter o k-agrupamento pelo algoritmo de Prim, é necessário construir toda a árvore geradora
mínima a partir do grafo. Após toda a construção da árvore, as arestas de maior peso são retiradas.
A cada aresta (considerando empates) retirada, novos componentes são determinados a partir de
alguma busca no grafo (e.g., busca em largura ou profundidade). Ou seja, os objetos que forem
explorados em cada busca são determinados como objetos de grupos (componentes) em questão.
Adicionalmente, o processo de retirada de arestas termina quando obtém-se k componentes conectados
a partir da árvore geradora mínima obtida.


### 3. Implementação!
Implementação dos algoritmos de Prim e de Kruskal para o cenário de k-agrupamento.

- **Entrada:**

Cada algoritmo recebe como parâmetro de entrada, uma lista de arestas do grafo e o número de grupos a ser obtido (k). Para também Prim deve ser informado o vértice inicial em segundo e o K como terceiro parametro.
O arquivo de lista de arestas deve conter em em cada linha o vértice origem (u), vértice destino (v) e
o peso (distância (d(u; v))) entre u e v, e representarem um grafo completo ponderado. Ou Seja, para (u v 5) deve existir (v u 5)

- **Saída:**

A saída para cada algoritmo, isto é, Prim e Kruskal é um vetor contendo os vértices e seus respectivos
rótulos de grupos (de 1 a k) para cada objeto do conjunto de dados (vértices).
