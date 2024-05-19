import random
from collections import deque
import random
from time import time

from matplotlib import pyplot as plt
import sys

sys.setrecursionlimit(100000)

def print_matrix(matrix):
    print("Graf jako macierz sąsiedztwa:")
    for row in matrix:
        print(*row)


def generate_hamiltonian_graph(n, s):
    edges_count = s * (n * (n - 1) // 2)
    adjacency_matrix = [[0] * n for _ in range(n)]
    edge_count = 0
    if edges_count < n - 1:
        print("Wrong saturation")
        return

    start_vertex = random.randint(0, n - 1)
    visited = []
    current_vertex = start_vertex
    visited.append(start_vertex)
    while edge_count < n - 1:
        next_vertex = random.randint(0, n - 1)
        if next_vertex not in visited:
            adjacency_matrix[current_vertex][next_vertex] = 1
            adjacency_matrix[next_vertex][current_vertex] = 1
            visited.append(next_vertex)
            current_vertex = next_vertex
            edge_count += 1

    adjacency_matrix[start_vertex][current_vertex] = 1
    adjacency_matrix[current_vertex][start_vertex] = 1
    edge_count += 1

    while edge_count <= edges_count:
        v1 = random.randint(0, n - 1)
        v2 = random.randint(0, n - 1)
        v3 = random.randint(0, n - 1)
        if v1 != v2 and v1 != v3 and v2 != v3:
            if adjacency_matrix[v1][v2] == 0 and adjacency_matrix[v2][v3] == 0 and adjacency_matrix[v1][v3] == 0:
                adjacency_matrix[v1][v2] = 1
                adjacency_matrix[v2][v1] = 1
                adjacency_matrix[v1][v3] = 1
                adjacency_matrix[v3][v1] = 1
                adjacency_matrix[v3][v2] = 1
                adjacency_matrix[v2][v3] = 1
                edge_count += 3

    return adjacency_matrix


def generate_non_hamiltonian_graph(n):
    edges_count = 0.5 * (n * (n - 1) // 2)
    adjacency_matrix = [[0] * n for _ in range(n)]
    edge_count = 0
    if edges_count < n - 1:
        print("Wrong saturation")
        return

    start_vertex = random.randint(0, n - 1)
    visited = []
    current_vertex = start_vertex
    visited.append(start_vertex)
    while edge_count < n - 1:
        next_vertex = random.randint(0, n - 1)
        if next_vertex not in visited:
            adjacency_matrix[current_vertex][next_vertex] = 1
            adjacency_matrix[next_vertex][current_vertex] = 1
            visited.append(next_vertex)
            current_vertex = next_vertex
            edge_count += 1

    adjacency_matrix[start_vertex][current_vertex] = 1
    adjacency_matrix[current_vertex][start_vertex] = 1
    edge_count += 1

    while edge_count <= edges_count:
        v1 = random.randint(0, n - 1)
        v2 = random.randint(0, n - 1)
        v3 = random.randint(0, n - 1)
        if v1 != v2 and v1 != v3 and v2 != v3 and v1 != start_vertex and v3 != start_vertex and v2 != start_vertex:
            if adjacency_matrix[v1][v2] == 0 and adjacency_matrix[v2][v3] == 0 and adjacency_matrix[v1][v3] == 0:
                adjacency_matrix[v1][v2] = 1
                adjacency_matrix[v2][v1] = 1
                adjacency_matrix[v1][v3] = 1
                adjacency_matrix[v3][v1] = 1
                adjacency_matrix[v3][v2] = 1
                adjacency_matrix[v2][v3] = 1
                edge_count += 3

    x = random.randint(0, n - 1)
    for i in range(n):
        adjacency_matrix[x][i] = 0
        adjacency_matrix[i][x] = 0

    return adjacency_matrix


def dfs_euler(v, matrix, n, queue):
    for i in range(n):
        if matrix[v][i] == 1:
            matrix[v][i] = 0
            matrix[i][v] = 0
            dfs_euler(i, matrix, n, queue)
    queue.appendleft(v)


def search_euler(matrix, n):
    queue = deque()
    dfs_euler(0, matrix, n, queue)
    return list(queue)


def hamiltonian(v, matrix):
    global visited, k, Path, O, start
    O[v] = True
    visited += 1
    for i in range(len(matrix)):
        if matrix[v][i]:
            if i == start and visited == len(matrix):
                Path[k] = v
                return True
            if not O[i]:
                if hamiltonian(i, matrix):
                    Path[k] = v
                    k += 1
                    return True
    O[v] = False
    visited -= 1
    return False


def h_cycle(matrix):
    global visited, k, Path, O, start
    for i in range(len(matrix)):
        O[i] = False
    Path[0] = start = 0
    visited = 0
    k = 1
    return hamiltonian(start, matrix)

# answer = 1
# while answer != 0:
#     print("Wybierz opcje:\n"
#           "1 wygeneruj graf hamiltonowski\n"
#           "2 wygeneruj graf nie-hamiltonowski\n"
#           "3 znajdz cykl Eulera i Hamiltona\n"
#           "0 zakoncz program")
#     answer = int(input())
#     if answer == 1:
#         n = int(input("n = "))
#         s = float(input("s = ")) #hamilton 0.3 0.7 no-hamilton 0.5
#         matrix = generate_hamiltonian_graph(n, s)
#         print_matrix(matrix)
#     elif answer == 2:
#         n = int(input("n = "))
#         matrix = generate_non_hamiltonian_graph(n)
#         print_matrix(matrix)
#     elif answer == 3:
#         O = [False for _ in range(len(matrix))]
#         start = len(matrix) - 1
#         visited = 0
#         k = len(matrix) - 1
#         Path = [0 for _ in range(len(matrix))]
#         current_path = []
#
#         print_matrix(matrix)
#         h_cycle(matrix)
#         print(f"Cykl Hamiltona: {Path}")
#         print("Ścieżka Eulera:", search_euler(matrix, n))

xVal = [10, 30, 50, 70, 90, 110, 130, 150, 170, 190]
yVal1 = [0 for _ in range(len(xVal))]
yVal2 = [0 for _ in range(len(xVal))]

for i in range(len(xVal)):
    matrix = generate_hamiltonian_graph(xVal[i], 0.3)
    timer = time()
    search_euler(matrix, xVal[i])
    yVal1[i] = time() - timer

    matrix = generate_hamiltonian_graph(xVal[i], 0.7)
    timer = time()
    search_euler(matrix, xVal[i])
    yVal2[i] = time() - timer
plt.plot(xVal, yVal1, label="dla nasycenia 30%")
plt.plot(xVal, yVal2, label="dla nasycenia 70%")
plt.legend()
plt.title("graf hamiltonowski - znajdowanie cyklu Eulera")
plt.xlabel("n")
plt.ylabel("czas (s)")
plt.show()

for i in range(len(xVal)):
    matrix = generate_hamiltonian_graph(xVal[i], 0.3)
    timer = time()
    O = [False for _ in range(len(matrix))]
    start = len(matrix) - 1
    visited = 0
    k = len(matrix) - 1
    Path = [0 for _ in range(len(matrix))]
    current_path = []
    h_cycle(matrix)
    yVal1[i] = time() - timer

    matrix = generate_hamiltonian_graph(xVal[i], 0.7)
    timer = time()
    O = [False for _ in range(len(matrix))]
    start = len(matrix) - 1
    visited = 0
    k = len(matrix) - 1
    Path = [0 for _ in range(len(matrix))]
    current_path = []
    h_cycle(matrix)
    yVal2[i] = time() - timer

plt.plot(xVal, yVal1, label="dla nasycenia 30%")
plt.plot(xVal, yVal2, label="dla nasycenia 70%")
plt.legend()
plt.title("graf hamiltonowski - znajdowanie cyklu Hamiltona")
plt.xlabel("n")
plt.ylabel("czas (s)")
plt.show()

xVal = [10, 15, 20, 25, 30]
yVal1 = [0 for _ in range(len(xVal))]
for i in range(len(xVal)):
    matrix = generate_non_hamiltonian_graph(xVal[i])
    timer = time()
    O = [False for _ in range(len(matrix))]
    start = len(matrix) - 1
    visited = 0
    k = len(matrix) - 1
    Path = [0 for _ in range(len(matrix))]
    current_path = []
    h_cycle(matrix)
    yVal1[i] = time() - timer

plt.plot(xVal, yVal1, label="dla nasycenia 50%")
plt.legend()
plt.title("graf nie hamiltonowski - znajdowanie cyklu Hamiltona")
plt.xlabel("n")
plt.ylabel("czas (s)")
plt.show()