import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    idx = 0
    n = int(input_data[idx])
    m = int(input_data[idx+1])
    idx += 2
    
    cap = [[0] * (n + 1) for _ in range(n + 1)]
    adj_residual = [set() for _ in range(n + 1)]
    adj_original = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        a = int(input_data[idx])
        b = int(input_data[idx+1])
        idx += 2
        
        cap[a][b] += 1
        adj_residual[a].add(b)
        adj_residual[b].add(a)
        adj_original[a].append(b)
    
    source, sink = 1, n
    
    def bfs_flow():
        parent = [-1] * (n + 1)
        queue = deque([source])
        parent[source] = source
        while queue:
            u = queue.popleft()
            for v in adj_residual[u]:
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u
                    if v == sink:
                        return parent
                    queue.append(v)
        return None

    max_flow = 0
    while True:
        parent = bfs_flow()
        if parent is None:
            break
        
        v = sink
        while v != source:
            u = parent[v]
            cap[u][v] -= 1
            cap[v][u] += 1
            v = u
        max_flow += 1
    
    print(max_flow)
    
    # BFS Corrigida para reconstrução
    def bfs_reconstruct():
        parent = [-1] * (n + 1)
        queue = deque([source])
        parent[source] = source
        
        found = False
        while queue:
            u = queue.popleft()
            if u == sink:
                found = True
                break
            
            for v in adj_original[u]:
                # CRÍTICO: No algoritmo de Edmonds-Karp, se cap[u][v] inicial era > 0 
                # e agora cap[u][v] == 0, significa que enviamos fluxo com sucesso de u para v.
                if parent[v] == -1 and cap[u][v] == 0:
                    parent[v] = u
                    queue.append(v)
                    break # Garante que pegamos apenas uma aresta por vértice nesta BFS
                    
        if not found:
            return None
            
        path = []
        v = sink
        while v != source:
            u = parent[v]
            # Devolvemos a capacidade para 1 para indicar que este caminho já foi extraído
            cap[u][v] = 1 
            path.append(v)
            v = u
        path.append(source)
        path.reverse()
        return path

    for _ in range(max_flow):
        path = bfs_reconstruct()
        if path:
            print(len(path))
            print(*(path))

if __name__ == '__main__':
    solve()