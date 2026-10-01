INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    # Create a copy of the graph matrix to store shortest distances
    dist = [row[:] for row in graph]

    # k is the intermediate vertex
    for k in range(V):
        # i is the source vertex
        for i in range(V):
            # j is the destination vertex
            for j in range(V):
                # If vertex k is on the shortest path from i to j, update dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


def print_matrix(matrix):
    for row in matrix:
        print(["INF" if val == INF else val for val in row])


# Example Usage
# Graph represented as an Adjacency Matrix (4 vertices: 0, 1, 2, 3)
graph = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0]
]

shortest_paths = floyd_warshall(graph)
print("Shortest distance matrix between every pair of vertices:")
print_matrix(shortest_paths)

# ---------------------------------------------------------
# TIME AND SPACE COMPLEXITY:
# Where V = number of vertices in the graph
# Time Complexity:  O(V^3) - Three nested loops each running V times
# Space Complexity: O(V^2) - 2D matrix of size V x V to store distances
# ---------------------------------------------------------