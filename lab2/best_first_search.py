# Aim: To implement the Best-First Search algorithm to greedily explore the node closest to the goal based on a heuristic evaluation function.
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}
print("Best First Search :")
def best_first_search(start, goal):
    open_list = [start]
    visited = []

    while open_list:

        # Select node with the lowest heuristic value
        current = min(open_list, key=lambda x: h[x])
        open_list.remove(current)

        # Skip already visited nodes
        if current in visited:
            continue

        print(current, end=" ")

        # Check whether goal is reached
        if current == goal:
            print("\nGoal Found!")
            return

        visited.append(current)

        # Add unvisited neighbours
        for neighbour in graph[current]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)

    print("\nGoal Not Found!")


best_first_search('A', 'F')
