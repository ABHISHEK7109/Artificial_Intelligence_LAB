# Aim: To implement the A* search algorithm using heuristics to find the shortest path from a start node to a goal node.

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 2)],
    'D': [],
    'E': [],
    'F': []
}

# Heuristic values
h = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}

print("A* Search Output :")

def a_star(start, goal):
    open_list = [(start, 0)]
    g = {start: 0}

    while open_list:
        # f(n) = g(n) + h(n)
        current, cost = min(
            open_list,
            key=lambda x: x[1] + h[x[0]]
        )

        open_list.remove((current, cost))

        print(current, end=" ")

        if current == goal:
            print("\nGoal Found!")
            return

        for neighbour, edge_cost in graph[current]:
            new_cost = g[current] + edge_cost

            if neighbour not in g or new_cost < g[neighbour]:
                g[neighbour] = new_cost
                open_list.append((neighbour, new_cost))

    print("\nGoal Not Found!")


a_star('A', 'F')