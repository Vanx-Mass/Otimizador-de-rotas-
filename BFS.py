# Dia 17 - Implementação BFS e Dijkstra com dados mockados

from collections import deque
import heapq

# -------------------------------
# 1. Criar grafo mockado
# -------------------------------
# Grafo representado como dicionário:
# Cada chave é um nó e o valor é uma lista de tuplas (vizinho, peso)
grafo = {
    "A": [("B", 1), ("C", 4)],
    "B": [("A", 1), ("D", 2), ("E", 5)],
    "C": [("A", 4), ("F", 3)],
    "D": [("B", 2), ("E", 1)],
    "E": [("B", 5), ("D", 1), ("F", 2)],
    "F": [("C", 3), ("E", 2)]
}

# -------------------------------
# 2. BFS (Busca em Largura) - sem pesos
# -------------------------------
def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    ordem_visita = []

    while fila:
        no = fila.popleft()
        if no not in visitados:
            visitados.add(no)
            ordem_visita.append(no)
            for vizinho, _ in grafo[no]:  # ignoramos peso
                if vizinho not in visitados:
                    fila.append(vizinho)
    return ordem_visita

# -------------------------------
# 3. Dijkstra (menor caminho com pesos)
# -------------------------------
def dijkstra(grafo, inicio):
    distancias = {no: float("inf") for no in grafo}
    distancias[inicio] = 0
    fila_prioridade = [(0, inicio)]  # (distância, nó)
    visitados = set()

    while fila_prioridade:
        dist_atual, no = heapq.heappop(fila_prioridade)
        if no in visitados:
            continue
        visitados.add(no)

        for vizinho, peso in grafo[no]:
            nova_dist = dist_atual + peso
            if nova_dist < distancias[vizinho]:
                distancias[vizinho] = nova_dist
                heapq.heappush(fila_prioridade, (nova_dist, vizinho))

    return distancias

# -------------------------------
# 4. Testando os algoritmos
# -------------------------------
print("📌 BFS (ordem de visita):")
print(bfs(grafo, "A"))

print("\n📌 Dijkstra (menores distâncias a partir de A):")
resultado_dijkstra = dijkstra(grafo, "A")
for no, dist in resultado_dijkstra.items():
    print(f"A -> {no} = {dist}")
