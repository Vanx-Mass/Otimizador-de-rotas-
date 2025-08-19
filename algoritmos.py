from collections import deque
import heapq

def bfs(grafo, origem, destino):
    fila = deque()
    fila.append((origem, [origem]))
    visitados = set()

    while fila:
        cidade, caminho = fila.popleft()

        if cidade == destino:
            return caminho

        for vizinho in grafo.get(cidade, {}):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))

    return None


def dijkstra(grafo, origem, destino):
    fila = []
    heapq.heappush(fila, (0, origem, [origem]))
    visitados = set()

    while fila:
        dist, cidade, caminho = heapq.heappop(fila)

        if cidade == destino:
            return caminho, dist

        if cidade in visitados:
            continue

        visitados.add(cidade)

        for vizinho, distancia in grafo.get(cidade, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (dist + distancia, vizinho, caminho + [vizinho]))

    return None, float('inf')
