# CSES Distinct Routes

## Integrantes

* Aaron Nogueira
* Arthur Soares
* Davi de Paula
---

## Vídeo da Apresentação

https://youtu.be/r0_DJOmtSmk 

---

## Problema

Link do problema:

https://cses.fi/problemset/task/1711

Dado um conjunto de salas conectadas por teleportadores direcionados, o objetivo é descobrir o maior número possível de rotas da sala 1 até a sala n, de forma que nenhum teleportador seja utilizado mais de uma vez. Além disso, é necessário reconstruir e imprimir as rotas encontradas.

---

## Linguagem Utilizada

* Python 3

---

## Como Executar

```bash
python src/main.py < entrada.txt
```

---

## Modelagem como Rede de Fluxo

O problema foi modelado como um problema de fluxo máximo.

### Origem (source)

Vértice 1, representando a sala inicial.

### Sorvedouro (sink)

Vértice n, representando a sala final.

### Vértices

Cada sala do problema corresponde a um vértice do grafo.

### Arestas

Cada teleporter a → b é modelado como uma aresta direcionada a → b.

### Capacidades

Todas as arestas possuem capacidade 1.

Isso representa a restrição do problema: cada teleporter pode ser usado no máximo uma vez durante todo o jogo.

---

## Algoritmo Utilizado

Foi utilizado o algoritmo Edmonds-Karp, uma implementação do método de Ford-Fulkerson que utiliza BFS para encontrar caminhos aumentantes.

### Ideia do algoritmo

1. Iniciamos com fluxo igual a zero.
2. Usamos BFS para encontrar um caminho da origem ao sorvedouro com capacidade residual positiva.
3. Calculamos o gargalo do caminho.
4. Atualizamos o grafo residual.
5. Repetimos o processo até não existir mais caminho aumentante.

O valor final do fluxo corresponde ao número máximo de dias em que o jogo pode ser jogado.

---

## Grafo Residual

O grafo residual armazena a capacidade restante das arestas após cada aumento de fluxo.

* Ao utilizar uma aresta u → v, sua capacidade residual diminui.
* Ao mesmo tempo, a capacidade da aresta reversa v → u aumenta.

Isso permite corrigir escolhas anteriores caso necessário.

---

## Reconstrução das Rotas

Após calcular o fluxo máximo, as rotas são reconstruídas percorrendo as arestas originais que ficaram saturadas. Cada caminho reconstruído representa um dia válido de jogo.

---

## Correção da Solução

Como cada aresta possui capacidade 1:

* nenhum teleporter pode ser compartilhado por duas rotas;
* cada unidade de fluxo representa uma rota válida;
* qualquer conjunto válido de rotas corresponde a um fluxo viável.

Pelo teorema Max-Flow Min-Cut, o fluxo máximo encontrado é ótimo. Portanto, o número de rotas obtido é o máximo possível.

---

## Complexidade

Sejam:

* V = número de vértices
* E = número de arestas

Complexidade:

O(V · E²)

Com os limites do problema (n ≤ 500 e m ≤ 1000), a solução é eficiente para o tempo limite.

---

## Casos Especiais Tratados

* Grafo sem caminho da sala 1 até a sala n.
* Grafo com apenas um caminho possível.
* Múltiplos caminhos independentes.
* Reconstrução correta das rotas após o cálculo do fluxo máximo.

---

## Evidência de Accepted

A comprovação da submissão aceita encontra-se na pasta:

```text
evidencias/
```



## Estrutura do Repositório

```text
T3/
├── README.md
├── acompanhamento/
│   └── roteiro.md
├── src/
│   └── main.py
├── evidencias/
│   └── accepted.png
├── apresentacao/
│   └── apresentacao.md
└── dados/
    └── exemplo.txt
```
