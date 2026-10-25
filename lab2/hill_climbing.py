
# Aim: To implement the Hill Climbing local optimization algorithm to find a local maximum/minimum by iteratively moving in the direction of increasing/decreasing value.

def hill_climbing(start, goal, graph, h):
    current = start

    while True:
        print("Current Node:", current)

        # Check if goal is reached
        if current == goal:
            print("Goal Found!")
            return

        # Get neighbouring nodes
        neighbours = graph[current]

        # If no neighbours are available
        if not neighbours:
            print("No better neighbour. Stuck!")
            return

        # Select neighbour with lowest heuristic value
        next_node = min(neighbours, key=lambda x: h[x])

        # Move only if neighbour is better
        if h[next_node] < h[current]:
            current = next_node
        else:
            print("No better neighbour. Stuck!")
            return


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Lower heuristic means closer to the goal
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}
print("Hill Climbing Search :")
hill_climbing('A', 'F', graph, h)
