class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Estimated cost from node to goal
        self.f = 0  # Total cost

def astar_space_complexity(graph, start, goal):
    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)
    
    # This will store the maximum size of the open list which correlates to the space complexity
    max_open_list_size = 1

    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        # Update the max_open_list_size
        max_open_list_size = max(max_open_list_size, len(open_list))

        if current_node.name == goal_node.name:
            # If goal is found, we can return the maximum open list size as space complexity
            return max_open_list_size

        for (next_node_name, time_cost) in graph[current_node.name]:
            if next_node_name in [closed_node.name for closed_node in closed_list]:
                continue
            
            child_node = Node(next_node_name, current_node)
            child_node.g = current_node.g + time_cost[0]  # Assuming the first element is the actual cost
            child_node.h = 0  # Simplified heuristic
            child_node.f = child_node.g + child_node.h
            
            if child_node.name in [open_node.name for open_node in open_list]:
                continue
            
            open_list.append(child_node)
    
    return max_open_list_size  # If goal is not found, space complexity is still determined by max open list size


graph = {
    'A': [('B', (500, 3)), ('C', (650, 2)),('D', (850,3))],  
    'B': [('G', (200, 1)),('C',(1000,4)), ('D',(590,1.5))],  
    'C': [('D', (600, 3))],
    'D': [('G',(1500, 2)),('E',(700,2))],
    'E': [('G',(2500,3))],
    'G': []
}

# Calculate space complexity
space_complexity = astar_space_complexity(graph, 'A', 'G')
print("Space Complexity (maximum nodes in memory):", space_complexity)

"""
Here we get the output as 2 becuase it is the actual maximum number of nodes that were in 
memory (in the open list) at any point during the execution of the A* algorithm 
and specific run. This is an empirical measure of space usage for that particular execution and input.

"""