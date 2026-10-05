# Practical 08: Breadth First Search (BFS)

## 1. Practical Number
**Practical 08**

## 2. Practical Name / Topic Name
**Graph Searching — Breadth First Search (BFS)**

## 3. Objective
To represent an undirected graph using an Adjacency List, implement Breadth First Search (BFS) in Python using a FIFO queue, display the level-order traversal sequence, measure actual execution time using `time.perf_counter()`, and analyze theoretical time and space complexity.

---

## 4. Problem Statement
Given an unweighted graph $G = (V, E)$ and a starting vertex $S$, systematically visit all vertices reachable from $S$ in order of their shortest path distance (level-by-level) from $S$.

---

## 5. Algorithm Explanation

### Core Logic
1. Represent the graph using an Adjacency List.
2. Initialize an empty `visited` set and a FIFO Queue (`collections.deque`).
3. Enqueue the start vertex $S$ and add it to `visited`.
4. While the queue is not empty:
   - Dequeue front vertex $u$ and append it to the traversal order.
   - For each adjacent neighbor $v$ of $u$:
     - If $v$ is not in `visited`, mark $v$ as visited and enqueue $v$.
5. Terminate when the queue is exhausted.

---

## 6. Step-by-Step Working

1. **Input Graph**:
   - Vertices: `A, B, C, D, E, F, G`
   - Edges: `(A, B), (A, C), (B, D), (B, E), (C, F), (C, G), (D, E), (E, F)`
2. **Level-by-Level Exploration**:
   - **Level 0 (Distance 0)**: Vertex `A`.
   - **Level 1 (Distance 1)**: Neighbors of `A` $\implies$ `B, C`.
   - **Level 2 (Distance 2)**: Neighbors of `B` and `C` $\implies$ `D, E, F, G`.
3. **Traversal Order**: `A -> B -> C -> D -> E -> F -> G`.
4. **Timing**: Measured via `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_08_BFS.py`

---

## 8. Sample Input
```python
edges = [
    ('A', 'B'), ('A', 'C'),
    ('B', 'D'), ('B', 'E'),
    ('C', 'F'), ('C', 'G'),
    ('D', 'E'), ('E', 'F')
]
start_node = 'A'
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 08: BREADTH FIRST SEARCH (BFS)
======================================================================
Graph Adjacency List:
  Node A -> [B, C]
  Node B -> [A, D, E]
  Node C -> [A, F, G]
  Node D -> [B, E]
  Node E -> [B, D, F]
  Node F -> [C, E]
  Node G -> [C]

Starting Vertex : 'A'

BFS Traversal Sequence : A -> B -> C -> D -> E -> F -> G
Execution Time         : 0.00000850 seconds (0.0085 ms)

Complexity Analysis:
  Time Complexity:
    - Overall : O(V + E) [where V is the number of vertices and E is edges]
  Space Complexity:
    - Auxiliary Space : O(V) [For FIFO queue and visited set]
======================================================================
```

---

## 10. Time Complexity Analysis

- **Time Complexity**: $O(V + E)$
  - Each vertex enters and leaves the queue at most once: $O(V)$.
  - Each edge is inspected twice (once from each endpoint): $O(E)$.

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(V)$ auxiliary space for the FIFO queue and `visited` set.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` captures timestamps around the BFS traversal routine:
```python
start_time = time.perf_counter()
bfs_order = bfs_traversal(g, start_node)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
Returns the level-order traversal: `A -> B -> C -> D -> E -> F -> G`.

---

## 14. Important Concepts Used
- **Level-Order Traversal**: Guarantees finding the shortest path in unweighted graphs.
- **FIFO Queue**: Manages frontier expansion efficiently.
- **Visited Tracking**: Prevents redundant processing and infinite loops in cyclic graphs.
