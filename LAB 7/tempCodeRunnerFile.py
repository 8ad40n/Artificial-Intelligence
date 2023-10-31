import random

# Fitness function
def fitness_function(x):
    return 3 * x**2 + 17 * x

# (a) Calculate the fitness of 8 random individuals (parents)
population_size = 8
parents = [random.randint(0, 31) for _ in range(population_size)]
fitness_values = [fitness_function(x) for x in parents]

# (b) Roulette wheel selection to select parents for the mating pool
def roulette_wheel_selection(population, fitness_values, num_parents):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected_parents = random.choices(population, probabilities, k=num_parents)
    return selected_parents

mating_pool_size = 4  # You can adjust this as needed
mating_pool = roulette_wheel_selection(parents, fitness_values, mating_pool_size)

# (c) Calculate the fitness of the next generation offspring after crossover
def crossover(parent1, parent2):
    # Implement your crossover logic here
    # For example, a one-point crossover:
    crossover_point = random.randint(1, 30)  # Avoid the endpoints
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

offspring = []
for i in range(0, mating_pool_size, 2):
    offspring1, offspring2 = crossover(mating_pool[i], mating_pool[i + 1])
    offspring.append(offspring1)
    offspring.append(offspring2)

# (d) Accept the fittest offspring
next_generation = offspring  # For simplicity, no mutation for this example

# Calculate the fitness of the next generation offspring
offspring_fitness_values = [fitness_function(x) for x in next_generation]

# Select the fittest offspring
fittest_offspring = next_generation[offspring_fitness_values.index(max(offspring_fitness_values))]

# Printing results
print("Parents:", parents)
print("Mating Pool:", mating_pool)
print("Offspring:", next_generation)
print("Fittest Offspring:", fittest_offspring)
