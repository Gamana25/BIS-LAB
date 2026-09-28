import random

courses = [
    
    "Physics",
    "Programming",
    "Artificial Intelligence",
    "Database",
    "Mathematics"
]

# Credits required for each course
credits = [3, 4, 3, 4, 3]

# Benefit of each course
benefits = [60, 85, 85, 70, 75]

# Maximum credits a student can take
MAX_CREDITS = 10


POPULATION_SIZE = 100
CHROMOSOME_LENGTH = 5
MUTATION_RATE = 0.01
CROSSOVER_RATE = 0.8
GENERATIONS = 20

def fitness(chromosome):
    """
    Calculate fitness based on course benefits.

    If total credits exceed the limit,
    fitness is 0.
    """

    total_credits = 0
    total_benefit = 0

    for i in range(CHROMOSOME_LENGTH):

        if chromosome[i] == 1:
            total_credits += credits[i]
            total_benefit += benefits[i]

    # Penalty for exceeding credit limit
    if total_credits > MAX_CREDITS:
        return 0

    return total_benefit

def create_population():

    return [
        [random.randint(0, 1) for _ in range(CHROMOSOME_LENGTH)]
        for _ in range(POPULATION_SIZE)
    ]


def selection(population):

    parent1 = random.choice(population)
    parent2 = random.choice(population)

    if fitness(parent1) > fitness(parent2):
        return parent1
    else:
        return parent2


def crossover(parent1, parent2):

    if random.random() < CROSSOVER_RATE:

        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1[:], parent2[:]


def mutation(chromosome):

    for i in range(CHROMOSOME_LENGTH):

        if random.random() < MUTATION_RATE:

            chromosome[i] = 1 - chromosome[i]

    return chromosome


def genetic_algorithm():

    population = create_population()

    best_solution = None
    best_fitness = float("-inf")

    for generation in range(GENERATIONS):

        # Evaluate population
        for individual in population:

            current_fitness = fitness(individual)

            if current_fitness > best_fitness:

                best_fitness = current_fitness
                best_solution = individual[:]

        print(
            f"Generation {generation + 1}: "
            f"Best Selection = {best_solution}, "
            f"Fitness = {best_fitness}"
        )


        new_population = []

        while len(new_population) < POPULATION_SIZE:

            # Selection
            parent1 = selection(population)
            parent2 = selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    total_credits = 0
    selected_courses = []

    for i in range(CHROMOSOME_LENGTH):

        if best_solution[i] == 1:

            selected_courses.append(courses[i])
            total_credits += credits[i]

    print("\n========== FINAL RESULT ==========")

    print("Best Chromosome:", best_solution)

    print("\nSelected Courses:")

    for course in selected_courses:
        print("-", course)

    print("\nTotal Credits:", total_credits)
    print("Maximum Benefit:", best_fitness)

genetic_algorithm()