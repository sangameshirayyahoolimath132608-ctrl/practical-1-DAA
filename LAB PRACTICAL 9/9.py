import heapq

def prims_mst(graph, start_node):
    visited = set()
    # Min-heap stores tuples of (weight, from_node, to_node)
    min_heap = [(0, None, start_node)]
    mst_edges = []
    total_cost = 0

    while min_heap:
        weight, frm, to = heapq.heappop(min_heap)

        if to in visited:
            continue

        visited.add(to)
        total_cost += weight
        if frm is not None:
            mst_edges.append((frm, to, weight))

        for neighbor, edge_weight in graph[to]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, to, neighbor))

    return mst_edges, total_cost


# Graph: {Node: [(Neighbor, Weight), ...]}
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

# Example Usage
edges, cost = prims_mst(graph, 'A')
print("Edges in Prim's MST:", edges)
print("Total Minimum Cost:", cost)

# ---------------------------------------------------------
# TIME AND SPACE COMPLEXITY:
# Where V = number of vertices, E = number of edges
# Time Complexity:  O(E log V) - Using binary min-heap and adjacency list
# Space Complexity: O(V + E)   - Storing the graph, heap, and visited set
# ---------------------------------------------------------