# Roteiro de Acompanhamento — Distinct Routes

## Integrantes

* Aaron Nogueira
* Arthur Soares
* Davi de Paula

---

# 1. Resumo do Problema

O problema pede o maior número de rotas distintas entre a sala 1 e a sala n utilizando cada teleporter no máximo uma vez.

Além do valor máximo, também é necessário reconstruir as rotas encontradas.

---

# 2. Entrada e Saída

## Entrada

* n = número de salas.
* m = número de teleportadores.
* Cada uma das próximas m linhas contém dois inteiros a e b.

## Saída

* Um inteiro k representando o número máximo de dias.
* Em seguida, k rotas válidas da sala 1 até a sala n.

---

# 3. Modelagem da Rede de Fluxo

## Origem

Sala 1.

## Sorvedouro

Sala n.

## Vértices

Cada sala do problema corresponde a um vértice.

## Arestas

Cada teleporter a → b gera uma aresta direcionada.

## Capacidades

Todas as arestas possuem capacidade 1.

Isso representa que cada teleporter pode ser usado apenas uma vez.

---

# 4. Escolha do Algoritmo

Foi utilizado Edmonds-Karp.

### Justificativa

* Usa BFS para encontrar caminhos aumentantes.
* Possui complexidade polinomial.
* É adequado para os limites do problema.
* Facilita a implementação do fluxo máximo.

---

# 5. Instância Pequena

Entrada:

```text
6 7
1 2
1 3
2 6
3 4
3 5
4 6
5 6
```

---

# 6. Execução Manual

## Estado Inicial

Fluxo total:

```text
0
```

Todas as capacidades são iguais a 1.

---

## Primeiro Caminho Aumentante

BFS encontra:

```text
1 → 2 → 6
```

Gargalo:

```text
1
```

Fluxo total:

```text
1
```

---

## Segundo Caminho Aumentante

BFS encontra:

```text
1 → 3 → 4 → 6
```

Gargalo:

```text
1
```

Fluxo total:

```text
2
```

---

## Nova Busca

Não existe mais caminho da sala 1 até a sala 6 com capacidade residual positiva.

O algoritmo termina.

---

# 7. Resultado Final

Fluxo máximo:

```text
2
```

Rotas:

```text
1 2 6
1 3 4 6
```

---

# 8. Verificação da Resposta

As duas rotas encontradas não compartilham nenhum teleporter.

Portanto, ambas são válidas.

Não existe uma terceira rota possível sem reutilizar alguma aresta.

Logo, a resposta ótima é 2.

---

# 9. Papel do Grafo Residual

O grafo residual armazena as capacidades restantes após cada aumento de fluxo.

As arestas reversas permitem desfazer escolhas anteriores caso isso seja necessário para encontrar uma solução melhor.

Essa propriedade garante que o algoritmo encontre o fluxo máximo correto.
