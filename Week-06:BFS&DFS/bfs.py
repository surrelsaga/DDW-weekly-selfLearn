# Adjacency list dict[node, list[neighbors]]
graph = {'V1': ['V2', 'V5'],
          'V2': ['V1', 'V3', 'V4'],
          'V3': ['V2'],
          'V4': ['V1', 'V3'],
          'V5': ['V4']}


# This is to traverse the graph, explore
# graph traversel => can translate to OOP easily
# queue, vertex
def bfs(graph, startNode):
    visitedNodes = []
    queue = [startNode]
    
    # while the queue is not empty
    while len(queue) > 0:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes and neighbor not in queue:
                queue.append(neighbor)
    
    return visitedNodes

print(bfs(graph, 'V2'))

# The whole point of bfs is to traverse in a graph, not a searchiing algo
# But, can make use to find the shortest path from one node to another
def bfsShortestPath(graph, startNode, endNode):
    visitedNodes = []
    queue = [startNode]
    parentNodes = {}
    
    # while the queue is not empty
    while len(queue) > 0:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes and neighbor not in queue:
                queue.append(neighbor)
                parentNodes[neighbor] = currentNode
    
    print(shortestPath(parentNodes, startNode, endNode))
    
def shortestPath(parentNodes, startNode, endNode):
    # Recursion
    # if endNode == startNode:
    #     return [startNode]
    # return shortestPath(parentNodes, startNode, parentNodes[endNode]) + [endNode]
    
    path = [endNode]
    currentNode = endNode
    # travel from the end upwards
    while currentNode != startNode:
        # find the parent node of the current node
        currentNode = parentNodes[currentNode]
        # travel, stay at the parent node place and repeat until reaching the starting point
        path.append(currentNode)
    
    path.reverse()
    return path

bfsShortestPath(graph, 'V1', 'V3')
