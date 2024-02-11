graph = {
    'A': [('B', (500, 3)), ('C', (650, 2)), ('D', (850,3))],  
    'B': [('G', (200, 1)), ('C', (1000,4)), ('D', (590,1.5))],  
    'C': [('D', (600, 3))],
    'D': [('G', (1500, 2)), ('E', (700,2))],
    'E': [('G', (2500,3))],
    'G': []
}

## Calculation of heuristic values ##

def calculate_heuristics(graph):
    heuristics = {}
    heuristics['G'] = 0
    for node in reversed(graph):
        if node != 'G':
            if graph[node]:
                heuristics[node] = min(time for _, time in graph[node])
            else:
                heuristics[node] = float('inf')
    return heuristics

heuristic_values = calculate_heuristics(graph)
print("Below are the heuristics values: "+"\n")
print(heuristic_values)

## Calculation of fitness ##

paths = [
    ['A', 'B', 'G'],  
    ['A', 'B', 'D', 'G'],
    ['A', 'D', 'G'],
    ['A', 'C', 'D', 'G'],
    ['A', 'C', 'B', 'G'],
    ['A', 'C', 'D', 'E', 'G']
]

# Dictionary to hold the fitness values for each path
fitness_values = {}

# Function to calculate the fitness of a path according to the updated graph structure
def fitness_function_updated(path, graph):
    total_time = 0
    total_fare = 0
    for i in range(len(path) - 1):
        from_node = path[i]
        to_node = path[i + 1]
        # Find the edge connecting from_node to to_node
        edge = next((edge for edge in graph[from_node] if edge[0] == to_node), None)
        if edge:
            # Add the fare and time from this edge to the totals
            fare, time = edge[1]  # Unpack the tuple
            total_time += time
            total_fare += fare
    # Combine time and scaled fare to get the fitness value
    fitness_value = total_time + (total_fare / 100)  # Scale fare down by a factor of 100
    return fitness_value

# Calculate and print the fitness values for each path
for path in paths:
    fitness_values[str(path)] = fitness_function_updated(path, graph)

print("\n Below is the fitness calculation: "+"\n")
print(fitness_values)
## From the fitness value it is evident that path ABG is more optimal as it is closer to zero comapred to other paths ##
