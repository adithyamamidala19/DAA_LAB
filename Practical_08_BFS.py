"""
================================================================================
PRACTICAL 08: GRAPH SEARCHING — BREADTH FIRST SEARCH (BFS)
================================================================================
Practical Number : Practical 08
Topic Name       : Breadth First Search (BFS)
Objective        : To represent an undirected graph using an Adjacency List, 
                   implement Breadth First Search (BFS) in Python, display the 
                   level-order vertex traversal, measure actual execution time 
                   using time.perf_counter(), and analyze its theoretical time 
                   and space complexity.

Algorithm Description:
  Breadth First Search explores all the neighbor vertices at the present depth 
  level before moving on to vertices at the next depth level. It utilizes a 
  First-In-First-Out (FIFO) queue (collections.deque) and a 'visited' set.
================================================================================
"""

import time
from collections import deque


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


def bfs_traversal(graph, start_vertex):
    """
    Performs Breadth First Search starting from `start_vertex`.
    
    Parameters:
      graph (Graph): The graph object.
      start_vertex: The starting vertex for traversal.
      
    Returns:
      list: Order of visited vertices.
    """
    visited = set()
    queue = deque([start_vertex])
    visited.add(start_vertex)
    traversal_order = []

    while queue:
        vertex = queue.popleft()
        traversal_order.append(vertex)

        # Explore unvisited neighbors level by level
        for neighbor in sorted(graph.adj_list.get(vertex, [])):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


def main():
    print("=" * 70)
    print("PRACTICAL 08: BREADTH FIRST SEARCH (BFS)")
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
    bfs_order = bfs_traversal(g, start_node)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"BFS Traversal Sequence : {' -> '.join(bfs_order)}")
    print(f"Execution Time         : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Overall : O(V + E) [where V is the number of vertices and E is edges]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(V) [For FIFO queue and visited set]")
    print("=" * 70)


if __name__ == "__main__":
    main()
