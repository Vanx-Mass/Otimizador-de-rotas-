# Implementação BFS e Dijkstra com dados mockados
# ==============================================

import heapq
from collections import deque

# ======================
# 1. Grafo Mockado
# ======================
# Representação de cidades e conexões
grafo = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "D": 1, "E": 3},
    "C": {"A": 5, "F": 2},
    "D": {"B": 1},
    "E": {"B": 3, "F": 2},
    "F": {"C": 2, "E": 2}
}

# ======================
# 2. Algoritmo BFS
# ======================
def bfs(grafo, inicio, destino):
    """Busca em Largura (BFS) - encontra menor caminho em número de passos"""
    fila = deque([(inicio, [inicio])])  # (nó atual, caminho percorrido)
    visitados = set()

    while fila:
        no, caminho = fila.popleft()
        if no == destino:
            return caminho
        if no not in visitados:
            visitados.add(no)
            for vizinho in grafo[no]:
                fila.append((vizinho, caminho + [vizinho]))
    return None

# ======================
# 3. Algoritmo Dijkstra
# ======================
def dijkstra(grafo, inicio, destino):
    """Algoritmo de Dijkstra - encontra menor caminho em termos de distância"""
    fila = [(0, inicio, [inicio])]  # (custo acumulado, nó atual, caminho percorrido)
    visitados = set()

    while fila:
        custo, no, caminho = heapq.heappop(fila)
        if no == destino:
            return caminho, custo
        if no not in visitados:
            visitados.add(no)
            for vizinho, peso in grafo[no].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (custo + peso, vizinho, caminho + [vizinho]))
    return None, float("inf")

# ======================
# 4. Testes
# ======================
print("=== BFS ===")
print("Caminho A -> F:", bfs(grafo, "A", "F"))

print("\n=== Dijkstra ===")
caminho, custo = dijkstra(grafo, "A", "F")
print("Caminho A -> F:", caminho, " | Custo:", custo)
