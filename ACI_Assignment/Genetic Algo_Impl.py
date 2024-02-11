import random

# Define the representation of a solution (individual)
class Path:
    def __init__(self, nodes):
        self.nodes = nodes
        self.fitness = -1

    def calculate_fitness(self, graph):
        total_cost = 0
        total_time = 0
        for i in range(len(self.nodes) - 1):
            for next_node, cost_time in graph[self.nodes[i]]:
                if next_node == self.nodes[i + 1]:
                    total_cost += cost_time[0]
                    total_time += cost_time[1]
                    break
        # Fitness is higher for lower cost and time
        self.fitness = 1 / (total_cost + total_time) if total_cost and total_time else 0

def create_initial_population(graph, start, goal, population_size):
    population = []
    nodes = list(graph.keys())
    for _ in range(population_size):
        # Randomly sample nodes to create a path, ensuring start and goal are fixed
        path = [start] + random.sample(nodes[1:-1], len(nodes) - 2) + [goal]
        population.append(Path(path))
    return population

def crossover(parent1, parent2):
    # Combine parts of two parents to produce a new path, ensuring start and goal are fixed
    child_p1 = parent1.nodes[1:-1]
    child_p2 = [item for item in parent2.nodes[1:-1] if item not in child_p1]
    child_path = [parent1.nodes[0]] + random.sample(child_p1 + child_p2, len(child_p1)) + [parent1.nodes[-1]]
    return Path(child_path)

def mutate(path, mutation_rate, graph):
    for i in range(1, len(path.nodes) - 1):
        if random.random() < mutation_rate:
            current_node = path.nodes[i]
            possible_moves = [move[0] for move in graph[path.nodes[i - 1]] if move[0] != current_node]
            if possible_moves:  # Check if the list is not empty
                path.nodes[i] = random.choice(possible_moves)


def select_parents(population):
    # Select parents for the next generation based on fitness
    population.sort(key=lambda x: x.fitness, reverse=True)
    return population[:2]

def genetic_algorithm(graph, start, goal, population_size, generations, mutation_rate):
    population = create_initial_population(graph, start, goal, population_size)
    for _ in range(generations):
        # Evaluate fitness
        for individual in population:
            individual.calculate_fitness(graph)
        # Select parents
        parents = select_parents(population)
        # Create next generation
        new_population = parents
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(parents, 2)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate, graph)
            child.calculate_fitness(graph)
            new_population.append(child)
        population = new_population
    # Return the best solution found
    best_path = max(population, key=lambda x: x.fitness)
    return best_path.nodes


graph = {
    'A': [('B', (500, 3)), ('C', (650, 2)),('D', (850,3))],  
    'B': [('G', (200, 1)),('C',(1000,4)), ('D',(590,1.5))],  
    'C': [('D', (600, 3))],
    'D': [('G',(1500, 2)),('E',(700,2))],
    'E': [('G',(2500,3))],
    'G': []
}

# Genetic Algorithm Impl
best_path = genetic_algorithm(graph, 'A', 'G', population_size=100, generations=50, mutation_rate=0.01)
print("Best Path by Genetic Algorithm:", best_path)
