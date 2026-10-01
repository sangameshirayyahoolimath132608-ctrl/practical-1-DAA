from collections import deque

# Graph represented as an Adjacency List
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

def bfs(graph, start_node):
    visited = set([start_node])
    queue = deque([start_node])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order


def dfs(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(node)
    order.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    return order


# Example Usage
print("BFS Traversal starting from 'A':", bfs(graph, 'A'))
print("DFS Traversal starting from 'A':", dfs(graph, 'A'))

# ---------------------------------------------------------
# TIME AND SPACE COMPLEXITY:
# Where V = number of vertices, E = number of edges
# BFS Time Complexity:  O(V + E) - Visits every vertex and edge once
# BFS Space Complexity: O(V)     - Queue and visited set storage
#
# DFS Time Complexity:  O(V + E) - Visits every vertex and edge once
# DFS Space Complexity: O(V)     - Recursion stack and visited set
# ---------------------------------------------------------