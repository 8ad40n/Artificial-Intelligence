import random

def fitness_function(x):
    return 3 * x**2 + 17 * x

def binary_to_integer(binary_str):
    return int(binary_str, 2)

def calculate_fitness_of_individuals(individuals):
    return [fitness_function(binary_to_integer(individual)) for individual in individuals]

def roulette_wheel_selection(population, fitness_values, num_parents):
    total_fitness = sum(fitness_values)
    probabilities = [fitness / total_fitness for fitness in fitness_values]
    selected_parents = random.choices(population, probabilities, k=num_parents)
    return selected_parents

def crossover(parent1, parent2):
    crossover_point = random.randint(1, 4)  
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual, mutation_count):
    mutated_individual = list(individual)
    mutation_positions = random.sample(range(len(individual)), mutation_count)
    for i in mutation_positions:
        mutated_individual[i] = '1' if mutated_individual[i] == '0' else '0'
    return ''.join(mutated_individual)

population_size = 8
mutation_count = 1 

random_individuals = ['01101', '11000', '01000', '10011','11100','11000','00001','10101']

fitness_values = calculate_fitness_of_individuals(random_individuals)

mating_pool_size = 8
mating_pool = roulette_wheel_selection(random_individuals, fitness_values, mating_pool_size)

next_generation = []
for i in range(0, mating_pool_size, 2):
    offspring1, offspring2 = crossover(mating_pool[i], mating_pool[i + 1])
    offspring1 = mutate(offspring1, mutation_count)
    offspring2 = mutate(offspring2, mutation_count)
    next_generation.extend([offspring1, offspring2])

offspring_fitness_values = calculate_fitness_of_individuals(next_generation)

fittest_offspring = next_generation[offspring_fitness_values.index(max(offspring_fitness_values))]

print("Fitness of 8 random individuals:", fitness_values)
print("Mating Pool:", mating_pool)
print("Next Generation Offspring:", next_generation)
print("Fittest Offspring:", fittest_offspring)
