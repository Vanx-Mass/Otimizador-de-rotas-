🚀 Otimizador de Rotas

Projeto em Python que encontra a melhor rota entre cidades utilizando **algoritmos clássicos de grafos**:

- **BFS (Breadth-First Search)** → encontra a rota com **menor número de conexões** entre cidades.
- **Dijkstra** → encontra a rota com **menor distância total** em quilômetros.

---

📂 Estrutura do Projeto

otimizador-de-rotas/
│
├── algoritmos.py # Implementação dos algoritmos BFS e Dijkstra
├── dados.py # Dados mockados das cidades e distâncias
├── main.py # Programa interativo no terminal
├── BFS.py # Exemplo isolado do BFS
├── rotas_entre_cidades.py # Testes integrados (Dia 18)
├── otimizador_de_rotas.ipynb # Notebook para rodar no Google Colab
└── README.md # Documentação do projeto

▶️ Como Executar

🔹 No Terminal
1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/otimizador-de-rotas.git
   cd otimizador-de-rotas

2. Rode o programa principal:
   python main.py

3. Siga o menu interativo para escolher entre BFS e Dijkstra.

🔹No Google Colab
Abra o arquivo otimizador_de_rotas.ipynb.
Execute as células para rodar o projeto diretamente no navegador.

✅ Exemplo de Uso
=== Otimizador de Rotas ===
1. Menor número de conexões (BFS)
2. Menor distância total (Dijkstra)
3. Sair
Escolha uma opção: 2
Cidade origem: São Paulo
Cidade destino: Brasília

Rota (Dijkstra): São Paulo -> Belo Horizonte -> Brasília
Distância total: 1302 km

📊 Complexidade dos Algoritmos

BFS (Breadth-First Search)

Objetivo: Encontrar o caminho com o menor número de conexões entre duas cidades.

Complexidade de tempo: O (V + E)

V = número de vértices (cidades)

E = número de arestas (conexões entre cidades)

Complexidade de espaço: O(V)
A fila e o conjunto de visitados podem armazenar até todos os vértices.

BFS explora todos os vizinhos de um nó antes de passar para o próximo nível, garantindo que o primeiro caminho encontrado seja o de menor número de conexões.

Dijkstra

Objetivo: Encontrar o caminho de menor distância total entre duas cidades.

Complexidade de tempo: O ((V + E) log V)

O uso de uma fila de prioridade (heap) garante que a extração do menor custo seja eficiente.

Complexidade de espaço: O (V + E)

Armazena todos os vizinhos e os caminhos explorados.

Dijkstra garante que, ao visitar um nó, já encontramos o caminho de menor custo até ele. É eficiente para grafos ponderados com pesos não negativos.
