# Aim: To implement the Breadth-First Search (BFS) graph traversal algorithm to explore nodes level by level.
from collections import deque

graph = {
    0: [2, 4],
    2: [5],
    4: [7],
    5: [9, 8],
    3: [9],
    9: [1],
    8: [2],
    6: [8]
}

visited = set()
queue = deque([0])

print("BFS Output :")
while queue:
    node = queue.popleft()

    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        for neighbour in graph.get(node, []):
            queue.append(neighbour)