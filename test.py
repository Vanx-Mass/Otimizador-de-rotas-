from algoritmos import bfs, dijkstra

grafo_mock = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "D": 1, "E": 3},
    "C": {"A": 5, "F": 2},
    "D": {"B": 1},
    "E": {"B": 3, "F": 2},
    "F": {"C": 2, "E": 2}
}

def test_bfs():
    caminho, conexoes = bfs(grafo_mock, "A", "F")
    assert caminho == ['A', 'C', 'F'] or caminho == ['A', 'B', 'E', 'F']
    assert conexoes >= 2

def test_dijkstra():
    caminho, custo = dijkstra(grafo_mock, "A", "F")
    assert caminho == ['A', 'C', 'F']
    assert custo == 7
