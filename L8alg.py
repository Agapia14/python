# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Решите задачу при помощи построения графа.
from functools import reduce

n = int(input('Сколько встретилось друзей: '))
graph = [[int(i > j) for i in range(n)] for j in range(n)]
count = reduce(lambda acc, x: acc + sum(x), graph, 0)
print(f'Количество рукопожатий {count}')

2
""""
Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
"""
g = [
  #  0  1  2  3  4  4  6  7
    [0, 0, 1, 1, 9, 0, 0, 0,],  # 0
    [0, 0, 9, 4, 0, 0, 5, 0,],  # 1
    [0, 9, 0, 0, 3, 0, 6, 0,],  # 2
    [0, 0, 0, 0, 0, 0, 0, 0,],  # 3
    [0, 0, 0, 0, 0, 0, 1, 0,],  # 4
    [0, 0, 0, 0, 0, 0, 5, 0,],  # 5
    [0, 0, 7, 0, 8, 1, 0, 0,],  # 6
    [0, 0, 0, 0, 0, 1, 2, 0,],  # 7
]

g2 = [
    [0, 3, 1, 9],
    [0, 0, 1, 2],
    [0, 1, 0, 4],
    [0, 0, 0, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    # parent = [-1] * length

    cost[start] = 0
    min_cost = 0
    way = []

    while min_cost < float('inf'):
        is_visited[start] = True
        way.append(start)

        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                new_cost = vertex + cost[start]
                if cost[i] > new_cost:
                    cost[i] = new_cost
                    # parent[i] = start

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, way


print(dijkstra(g, 0))

3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""

from collections import deque


def generate_graph(num):
    new_graph = {}

    for i in range(num):
        new_graph[i] = tuple(j for j in range(num) if j != i)

    return new_graph


def walk_graph(graph, start, finish):
    length = len(graph)
    parent = [None] * length
    is_visited = [False] * length

    deq = deque([start])
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop()

        if current == finish:
            break

        for vertex in graph[current]:
            if not is_visited[vertex]:
                is_visited[vertex] = True
                parent[vertex] = current
                deq.appendleft(vertex)
    else:
        return f"Из вершины {start} невозможно попасть в вершину {finish}"

    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return list(way)


n = int(input("Количество вершин в графе: "))
s = int(input("Введите вершину начала: "))
f = int(input("Введите вершину конца: "))

g = generate_graph(30)

print (walk_graph(g, s, f))

