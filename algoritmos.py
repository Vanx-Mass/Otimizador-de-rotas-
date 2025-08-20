from collections import deque
import heapq

def bfs(grafo, origem, destino):
    """
    Encontra o caminho com menor número de conexões entre duas cidades.

    Args:
        grafo (dict): Dicionário representando o grafo.
        origem (str): Cidade de partida.
        destino (str): Cidade de destino.

    Returns:
        tuple: (caminho, número de conexões) ou (None, 0) se não houver caminho.
    """
    fila = deque([(origem, [origem])])
    visitados = set()

    while fila:
        cidade, caminho = fila.popleft()

        if cidade == destino:
            return caminho, len(caminho) - 1

        if cidade not in visitados:
            visitados.add(cidade)
            for vizinho in grafo.get(cidade, {}):
                fila.append((vizinho, caminho + [vizinho]))

    return None, 0


def dijkstra(grafo, origem, destino):
    """
    Encontra o caminho de menor distância entre duas cidades usando Dijkstra.

    Args:
        grafo (dict): Dicionário representando o grafo com pesos.
        origem (str): Cidade de partida.
        destino (str): Cidade de destino.

    Returns:
        tuple: (caminho, distância total) ou (None, inf) se não houver caminho.
    """
    fila = [(0, origem, [origem])]
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
