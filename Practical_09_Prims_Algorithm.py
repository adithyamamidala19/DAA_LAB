"""
================================================================================
PRACTICAL 09: PRIM'S ALGORITHM (MINIMUM SPANNING TREE)
================================================================================
Title: Implementation of Prim's Algorithm for Minimum Spanning Tree (MST)
Algorithm:
  - Prim's Greedy MST Algorithm using Priority Queue (Min-Heap)

Description:
  This program implements Prim's Algorithm to find the Minimum Spanning Tree (MST)
  of a connected, weighted, undirected graph. Starting from an arbitrary vertex,
  it grows the spanning tree one vertex at a time by greedily choosing the
  minimum-weight edge connecting a vertex in the MST to a vertex outside the MST.
================================================================================
"""

import time
import heapq


class WeightedGraph:
    """Weighted Undirected Graph representation using an Adjacency List."""
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v, weight):
        """Adds an undirected edge between u and v with given weight."""
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []

        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def vertices(self):
        """Returns the list of all vertices in the graph."""
        return list(self.adj.keys())


def prims_mst(graph, start_node=None):
    """
    Computes the Minimum Spanning Tree (MST) using Prim's Algorithm.
    
    Parameters:
      graph (WeightedGraph): The input connected weighted graph.
      start_node (optional): The starting vertex.
      
    Returns:
      tuple: (mst_edges, total_cost)
        mst_edges: List of tuples (u, v, weight) in the MST.
        total_cost: Sum of weights of all edges in the MST.
    """
    nodes = graph.vertices()
    if not nodes:
        return [], 0

    if start_node is None:
        start_node = nodes[0]

    visited = set()
    mst_edges = []
    total_cost = 0

    # Min-Heap stores tuples: (edge_weight, from_vertex, to_vertex)
    min_heap = []

    # Mark the start node as visited and add all its incident edges to the heap
    visited.add(start_node)
    for neighbor, weight in graph.adj[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    while min_heap and len(visited) < len(nodes):
        weight, u, v = heapq.heappop(min_heap)

        # If destination vertex is already in MST, skip to avoid cycles
        if v in visited:
            continue

        # Include edge (u, v) in MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        total_cost += weight

        # Add all outgoing edges from newly added vertex v to unvisited vertices
        for next_neighbor, next_weight in graph.adj[v]:
            if next_neighbor not in visited:
                heapq.heappush(min_heap, (next_weight, v, next_neighbor))

    return mst_edges, total_cost


def main():
    print("=" * 70)
    print("PRACTICAL 9 - PRIM'S ALGORITHM")
    print("=" * 70)

    # Construct sample weighted undirected graph
    # Graph vertices: A, B, C, D, E, F
    g = WeightedGraph()
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

    for u, v, w in edges:
        g.add_edge(u, v, w)

    print("Graph Adjacency List with Edge Weights:")
    for node in sorted(g.adj.keys()):
        adj_info = ", ".join(f"{nbr}(w={w})" for nbr, w in g.adj[node])
        print(f"  Node {node} -> [{adj_info}]")
    print()

    # Measure execution time
    start_time = time.perf_counter()
    mst_edges, total_cost = prims_mst(g, 'A')
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output formatted exactly as required
    print("Edges in Minimum Spanning Tree:")
    for u, v, weight in mst_edges:
        print(f"  {u} - {v} : {weight}")

    print(f"\nTotal MST Cost: {total_cost}")
    print(f"\nExecution Time: {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)")

    print("\nTime Complexity:")
    print("  - Using Min-Heap with Adjacency List: O(E log V)")
    print("  - Using Adjacency Matrix: O(V^2)")
    print("  where V is the number of vertices and E is the number of edges.")
    print("Space Complexity: O(V + E) auxiliary space for graph and priority queue")
    print("=" * 70)


if __name__ == "__main__":
    main()
