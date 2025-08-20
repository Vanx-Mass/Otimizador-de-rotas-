from dados import CIDADES
from algoritmos import bfs, dijkstra

def menu():
    print("\n=== Otimizador de Rotas ===")
    print("1. Menor número de conexões (BFS)")
    print("2. Menor distância total (Dijkstra)")
    print("3. Sair")
    return input("Escolha uma opção: ").strip()

def main():
    while True:
        opcao = menu()

        if opcao == "3":
            print("Saindo...")
            break

        origem = input("Cidade origem: ").strip().title()
        destino = input("Cidade destino: ").strip().title()

        if origem not in CIDADES or destino not in CIDADES:
            print("Cidade não encontrada!")
            print("Cidades disponíveis:", ", ".join(CIDADES.keys()))
            continue

        if opcao == "1":
            caminho, conexoes = bfs(CIDADES, origem, destino)
            if caminho:
                print(f"Rota (BFS): {' -> '.join(caminho)} | Conexões: {conexoes}")
            else:
                print("Sem rota disponível!")

        elif opcao == "2":
            caminho, distancia = dijkstra(CIDADES, origem, destino)
            if caminho:
                print(f"Rota (Dijkstra): {' -> '.join(caminho)}")
                print(f"Distância total: {distancia} km")
            else:
                print("Sem rota disponível!")

        else:
            print("Opção inválida! Escolha 1, 2 ou 3.")

if __name__ == "__main__":
    main()
