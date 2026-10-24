
import random

# Fitness function
def fitness(x):
    return x * x

# Initialize population
population = [random.randint(0, 31) for _ in range(6)]

best_overall = population[0]

for generation in range(10):

    # Sort population by fitness
    population.sort(key=fitness, reverse=True)

    # Display best solution
    best = population[0]

    if fitness(best) > fitness(best_overall):
        best_overall = best

    print("Generation:", generation + 1,
          "Best x:", best,
          "Fitness:", fitness(best))

    # Selection: choose the best individuals
    parents = population[:3]

    # Crossover: create the next generation
    new_population = parents.copy()

    while len(new_population) < 6:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2

        # Mutation
        if random.random() < 0.2:
            child = random.randint(0, 31)

        new_population.append(child)

    population = new_population

# Check the final population too
best_final = max(population, key=fitness)

if fitness(best_final) > fitness(best_overall):
    best_overall = best_final

print("\nOptimal solution:", best_overall)
print("Maximum fitness:", fitness(best_overall))
