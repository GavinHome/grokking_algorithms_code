# the graph (from one node to another node with weights)
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

# init the costs table (from start to all nodes)
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity


# init the parents table (for the last)
parents = {}
parents["a"] = "start"
parents["b"] = "start" 
parents["end"] = None 

# for the processed node
processed = []


# find the lowest cost node not in processed
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_node = None
    for key in costs:
        if key not in processed and costs[key] < lowest_cost:
            lowest_node = key
            lowest_cost = costs[key]
    return lowest_node

def print_lowest_cost_path(parents):
    path = []
    current = "end"
    while current != "start":
        path.append(current)
        if current not in parents:
            break
        current = parents[current]
    path.append("start")  
    path.reverse()  
    return "->".join(path)

# find the lowest path from start to end
def find_lowest_path():
    node = find_lowest_cost_node(costs)
    while node is not None:
        nexts = graph[node]
        for next in nexts.keys():
            cost = costs[node] + nexts[next]
            if  cost < costs[next]:
                costs[next] = cost
                parents[next] = node

        processed.append(node)
        node = find_lowest_cost_node(costs)

    return print_lowest_cost_path(parents)


print(find_lowest_path())


