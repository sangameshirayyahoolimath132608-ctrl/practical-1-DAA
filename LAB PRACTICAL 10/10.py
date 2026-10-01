class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, set1, set2):
        root1 = self.find(set1)
        root2 = self.find(set2)
        if root1 != root2:
            self.parent[root1] = root2
            return True
        return False


def kruskals_mst(vertices, edges):
    # Sort edges based on weight (index 2)
    edges.sort(key=lambda x: x[2])
    ds = DisjointSet(vertices)
    
    mst_edges = []
    total_cost = 0

    for u, v, weight in edges:
        # If including this edge doesn't cause a cycle, include it
        if ds.union(u, v):
            mst_edges.append((u, v, weight))
            total_cost += weight

    return mst_edges, total_cost


# Example Usage
vertices = ['A', 'B', 'C', 'D']
# Edges list: (Node1, Node2, Weight)
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

mst, cost = kruskals_mst(vertices, edges)
print("Edges in Kruskal's MST:", mst)
print("Total Minimum Cost:", cost)

# ---------------------------------------------------------
# TIME AND SPACE COMPLEXITY:
# Where V = number of vertices, E = number of edges
# Time Complexity:  O(E log E) or O(E log V) - Dominated by sorting edges
# Space Complexity: O(V + E)                 - Parent dictionary and edge list
# ---------------------------------------------------------