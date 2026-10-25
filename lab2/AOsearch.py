# Aim: To implement the AO* algorithm for problem-solving using AND-OR graphs and heuristic search strategies.

graph = {
    'A': [['B', 'C'], ['D']],
    'B': [['E']],
    'C': [['F']],
    'D': [['G']],
    'E': [],
    'F': [],
    'G': []
}

cost = {
    'A': 10,
    'B': 4,
    'C': 3,
    'D': 5,
    'E': 1,
    'F': 1,
    'G': 1
}
print("AO Search")
def ao_star(node):
    print("Visiting:", node)

    if not graph[node]:
        return cost[node]

    best_cost = float('inf')

    for option in graph[node]:
        total = 0

        for child in option:
            total += ao_star(child)

        if total < best_cost:
            best_cost = total

    cost[node] = best_cost
    return best_cost


answer = ao_star('A')

print("Minimum Cost:", answer)