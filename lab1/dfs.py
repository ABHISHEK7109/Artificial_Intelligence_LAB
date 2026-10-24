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

def dfs(node):
    if node in visited:
        return

    print(node, end=" ")
    visited.add(node)

    for neighbour in graph.get(node, []):
        dfs(neighbour)

dfs(0)