from dados import CIDADES
from algoritmos import bfs, dijkstra

def menu():
    print("\n=== Otimizador de Rotas ===")
    print("1. Menor número de conexões (BFS)")
    print("2. Menor distância total (Dijkstra)")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()

        if opcao == "3":
            break

        origem = input("Cidade origem: ").strip()
        destino = input("Cidade destino: ").strip()

        if origem not in CIDADES or destino not in CIDADES:
            print("Cidade não encontrada!")
            continue

        if opcao == "1":
            caminho = bfs(CIDADES, origem, destino)
            if caminho:
                print(f"Rota (BFS): {' -> '.join(caminho)}")
            else:
                print("Sem rota disponível!")

        elif opcao == "2":
            caminho, distancia = dijkstra(CIDADES, origem, destino)
            if caminho:
                print(f"Rota (Dijkstra): {' -> '.join(caminho)}")
                print(f"Distância total: {distancia} km")
            else:
                print("Sem rota disponível!")

if __name__ == "__main__":
    main()
