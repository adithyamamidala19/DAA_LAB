"""
================================================================================
PRACTICAL 10: KRUSKAL'S ALGORITHM (MINIMUM SPANNING TREE)
================================================================================
Title: Implementation of Kruskal's Algorithm for Minimum Spanning Tree (MST)
Algorithm:
  - Kruskal's Greedy MST Algorithm using Disjoint Set Union (DSU / Union-Find)
  - Features: Edge Sorting, Path Compression, and Union by Rank

Description:
  This program implements Kruskal's Algorithm to find the Minimum Spanning Tree (MST)
  of a connected, weighted, undirected graph. It sorts all edges in non-decreasing
  order of their weights and iterates through them, adding an edge to the MST if
  and only if it does not form a cycle. Cycle detection is efficiently managed
  using a Disjoint Set Union (DSU) data structure with Path Compression and
  Union by Rank.
================================================================================
"""

import time


class DisjointSet:
    """Disjoint Set Union (DSU) / Union-Find data structure with Path Compression and Union by Rank."""
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        """Finds the representative root of the set containing `item` with Path Compression."""
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])  # Path compression
        return self.parent[item]

    def union(self, root1, root2):
        """Unites the sets containing root1 and root2 using Union by Rank."""
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1


def kruskals_mst(vertices, edges):
    """
    Computes the Minimum Spanning Tree (MST) using Kruskal's Algorithm.
    
    Parameters:
      vertices (list): List of all vertices in the graph.
      edges (list): List of tuples (u, v, weight).
      
    Returns:
      tuple: (sorted_edges, mst_edges, total_cost)
    """
    # Step 1: Sort all edges in non-decreasing order of weight
    sorted_edges = sorted(edges, key=lambda edge: edge[2])

    # Step 2: Initialize Disjoint Set for all vertices
    dsu = DisjointSet(vertices)
    mst_edges = []
    total_cost = 0

    # Step 3: Iterate through sorted edges and pick edges that do not form a cycle
    for u, v, weight in sorted_edges:
        root_u = dsu.find(u)
        root_v = dsu.find(v)

        # If roots are different, including this edge will not form a cycle
        if root_u != root_v:
            mst_edges.append((u, v, weight))
            total_cost += weight
            dsu.union(root_u, root_v)

            # Optimization: MST has exactly (V - 1) edges
            if len(mst_edges) == len(vertices) - 1:
                break

    return sorted_edges, mst_edges, total_cost


def main():
    print("=" * 70)
    print("PRACTICAL 10 - KRUSKAL'S ALGORITHM")
    print("=" * 70)

    # Define vertices and weighted edges
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 6),
        ('D', 'E', 3),
        ('D', 'F', 6),
        ('E', 'F', 2)
    ]

    print(f"Graph Vertices: {vertices}")
    print(f"Total Edges   : {len(edges)}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_edges, mst_edges, total_cost = kruskals_mst(vertices, edges)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output formatted exactly as required
    print("Sorted Edges:")
    for u, v, w in sorted_edges:
        print(f"  {u} - {v} : weight = {w}")

    print("\nEdges in Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"  {u} - {v} : {weight}")

    print(f"\nTotal MST Cost: {total_cost}")
    print(f"\nExecution Time: {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)")

    print("\nTime Complexity: O(E log E) or O(E log V)")
    print("  - Sorting edges: O(E log E)")
    print("  - DSU operations (Find/Union with path compression and rank): O(E * alpha(V)) ~= O(E)")
    print("  Overall Time Complexity dominated by sorting: O(E log E) = O(E log V)")
    print("Space Complexity: O(V + E) auxiliary space for storing edges and DSU structures")
    print("=" * 70)


if __name__ == "__main__":
    main()
