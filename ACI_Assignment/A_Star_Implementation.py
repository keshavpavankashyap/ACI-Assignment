class Node:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.g = 0  # Cost from start to node
        self.h = 0  # Estimated cost from node to goal
        self.f = 0  # Total cost

# A-Star Implementation

def astar(graph, costs, start, goal):
    open_list = []
    closed_list = []

    start_node = Node(start)
    goal_node = Node(goal)
    open_list.append(start_node)
    
    while open_list:
        current_node = min(open_list, key=lambda node: node.f)
        open_list.remove(current_node)
        closed_list.append(current_node)

        if current_node.name == goal_node.name:
            path = []
            while current_node:
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]

        for (next_node_name, time_cost) in graph[current_node.name]:
            if next_node_name in [closed_node.name for closed_node in closed_list]:
                continue
            
            child_node = Node(next_node_name, current_node)
            child_node.g = current_node.g + time_cost[0]  # Assuming the first element of time_cost is the actual cost
            child_node.h = 0  # Simplified heuristic
            child_node.f = child_node.g + child_node.h
            
            if child_node.name in [open_node.name for open_node in open_list]:
                continue
            
            open_list.append(child_node)
    
    return None


graph = {
    'A': [('B', (500, 3)), ('C', (650, 2)),('D', (850,3))],  
    'B': [('G', (200, 1)),('C',(1000,4)), ('D',(590,1.5))],  
    'C': [('D', (600, 3))],
    'D': [('G',(1500, 2)),('E',(700,2))],
    'E': [('G',(2500,3))],
    'G': []
}

# Costs are incorporated into the graph as (cost, time) tuples for simplicity

path = astar(graph, None, 'A', 'G')
print("Path:", path)


