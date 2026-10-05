"""
================================================================================
PRACTICAL 08: GRAPH SEARCHING — DEPTH FIRST SEARCH (DFS)
================================================================================
Practical Number : Practical 08
Topic Name       : Depth First Search (DFS)
Objective        : To represent an undirected graph using an Adjacency List, 
                   implement Depth First Search (DFS) in Python, display the 
                   vertex traversal order, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  Depth First Search is a graph traversal algorithm that explores as deep as 
  possible along each branch before backtracking. It utilizes recursion 
  (or an explicit LIFO stack) and maintains a 'visited' set to prevent cycles.
================================================================================
"""

import time


class Graph:
    """Graph representation using an Adjacency List."""
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v, directed=False):
        """Adds an edge between vertex u and vertex v."""
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []

        self.adj_list[u].append(v)
        if not directed:
            self.adj_list[v].append(u)

    def display(self):
        """Displays adjacency list representation of the graph."""
        print("Graph Adjacency List:")
        for node in sorted(self.adj_list.keys()):
            neighbors = ", ".join(map(str, sorted(self.adj_list[node])))
            print(f"  Node {node} -> [{neighbors}]")


def dfs_traversal(graph, start_vertex):
    """
    Performs Depth First Search starting from `start_vertex`.
    
    Parameters:
      graph (Graph): The graph object.
      start_vertex: The starting vertex for traversal.
      
    Returns:
      list: Order of visited vertices.
    """
    visited = set()
    traversal_order = []

    def _dfs_util(vertex):
        visited.add(vertex)
        traversal_order.append(vertex)
        # Explore neighbors in sorted order for deterministic output
        for neighbor in sorted(graph.adj_list.get(vertex, [])):
            if neighbor not in visited:
                _dfs_util(neighbor)

    _dfs_util(start_vertex)
    return traversal_order


def main():
    print("=" * 70)
    print("PRACTICAL 08: DEPTH FIRST SEARCH (DFS)")
    print("=" * 70)

    # Construct sample graph
    g = Graph()
    edges = [
        ('A', 'B'), ('A', 'C'),
        ('B', 'D'), ('B', 'E'),
        ('C', 'F'), ('C', 'G'),
        ('D', 'E'), ('E', 'F')
    ]
    for u, v in edges:
        g.add_edge(u, v)

    g.display()
    print()

    start_node = 'A'
    print(f"Starting Vertex : '{start_node}'\n")

    # Measure execution time
    start_time = time.perf_counter()
    dfs_order = dfs_traversal(g, start_node)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"DFS Traversal Sequence : {' -> '.join(dfs_order)}")
    print(f"Execution Time         : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Overall : O(V + E) [where V is the number of vertices and E is edges]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(V) [For recursion stack and visited set]")
    print("=" * 70)


if __name__ == "__main__":
    main()
