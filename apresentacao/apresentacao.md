# Distinct Routes — CSES

## Integrantes

* Aaron Nogueira
* Arthur Soares
* Davi de Paula

---

# 1. Contexto do Problema

Temos n salas conectadas por m teleportadores direcionados.

Em cada dia, começamos na sala 1 e precisamos chegar à sala n.

Cada teleporter pode ser usado no máximo uma vez durante todo o jogo.

O objetivo é descobrir o número máximo de dias possíveis e reconstruir as rotas utilizadas.

---

# 2. Modelagem como Rede de Fluxo

## Origem (Source)

Sala 1.

## Sorvedouro (Sink)

Sala n.

## Vértices

Cada sala do problema é um vértice do grafo.

## Arestas

Cada teleporter a → b vira uma aresta direcionada a → b.

## Capacidades

Todas as arestas têm capacidade 1.

Assim:

* cada unidade de fluxo representa um dia válido;
* fluxo máximo = número máximo de dias.

---

# 3. Exemplo

Rotas:

```text
1 → 2 → 6
1 → 3 → 4 → 6
```

Fluxo máximo:

```text
2
```

---

# 4. Algoritmo Utilizado

Utilizamos Edmonds-Karp.

### Passos

1. Encontrar um caminho aumentante usando BFS.
2. Calcular o gargalo.
3. Atualizar o grafo residual.
4. Repetir até não existir mais caminho.

Pelo teorema Max-Flow Min-Cut, o fluxo máximo encontrado corresponde exatamente ao número máximo de dias possíveis.

---

# 5. Grafo Residual

Após utilizar uma aresta:

```text
u → v
```

* a capacidade residual direta diminui;
* a capacidade residual reversa aumenta.

As arestas reversas permitem corrigir escolhas anteriores e garantem a otimalidade da solução.

---

# 6. Reconstrução das Rotas

Após calcular o fluxo máximo:

* identificamos as arestas utilizadas pelo fluxo;
* reconstruímos cada caminho da sala 1 até a sala n;
* imprimimos as rotas exigidas pelo problema.

---

# 7. Complexidade

Edmonds-Karp:

```text
O(V · E²)
```

onde:

* V = vértices
* E = arestas

---

# 8. Conclusão

Modelamos o problema como fluxo máximo.

* Fonte = sala 1
* Sorvedouro = sala n
* Capacidade = 1 por teleporter

O fluxo máximo obtido corresponde exatamente ao número máximo de dias em que o jogo pode ser jogado.
