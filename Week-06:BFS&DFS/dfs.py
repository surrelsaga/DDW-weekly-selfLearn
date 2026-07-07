graph = {'V1': ['V2', 'V5'],
          'V2': ['V1', 'V3', 'V4'],
          'V3': ['V2'],
          'V4': ['V1', 'V3'],
          'V5': ['V4']}


def dfs(graph, node):
    visited = []
    stack = []
    
    visited.append(node)
    stack.append(node)
    
    while len(stack) > 0:
        s = stack.pop()
        print(s, end = " ")
        
        for n in reversed(graph[s]):
            if n not in visited:
                visited.append(n)
                stack.append(n)

dfs(graph, 'V1')
