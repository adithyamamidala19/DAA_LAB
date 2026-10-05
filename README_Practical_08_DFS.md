# Practical 08: Depth First Search (DFS)

## 1. Practical Number
**Practical 08**

## 2. Practical Name / Topic Name
**Graph Searching — Depth First Search (DFS)**

## 3. Objective
To represent an undirected graph using an Adjacency List, implement Depth First Search (DFS) in Python, display the traversal sequence, measure actual execution time using `time.perf_counter()`, and analyze theoretical time and space complexity.

---

## 4. Problem Statement
Given an unweighted graph $G = (V, E)$ and a start vertex $S$, visit all reachable vertices in depth-first order by proceeding as deep as possible along each branch before backtracking.

---

## 5. Algorithm Explanation

### Core Logic
1. Represent the graph using an Adjacency List.
2. Initialize an empty `visited` set and a traversal order list.
3. For a given vertex $u$:
   - Mark $u$ as visited.
   - Add $u$ to the traversal order.
   - For each adjacent neighbor $v$ of $u$:
     - If $v$ is not visited, recursively call DFS on $v$.
4. Backtrack when all adjacent vertices from the current node have been visited.

---

## 6. Step-by-Step Working

1. **Input Graph**:
   - Vertices: `A, B, C, D, E, F, G`
   - Edges: `(A, B), (A, C), (B, D), (B, E), (C, F), (C, G), (D, E), (E, F)`
2. **Traversal Flow starting at A**:
   - Visit `A` $\to$ Explore neighbor `B`.
   - Visit `B` $\to$ Explore neighbor `D`.
   - Visit `D` $\to$ Explore neighbor `E`.
   - Visit `E` $\to$ Explore neighbor `F`.
   - Visit `F` $\to$ Explore neighbor `C`.
   - Visit `C` $\to$ Explore neighbor `G`.
   - Visit `G` $\to$ Backtracks up the recursion tree.
3. **Traversal Order**: `A -> B -> D -> E -> F -> C -> G`.
4. **Timing**: Measured via `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_08_DFS.py`

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
PRACTICAL 08: DEPTH FIRST SEARCH (DFS)
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

DFS Traversal Sequence : A -> B -> D -> E -> F -> C -> G
Execution Time         : 0.00000780 seconds (0.0078 ms)

Complexity Analysis:
  Time Complexity:
    - Overall : O(V + E) [where V is the number of vertices and E is edges]
  Space Complexity:
    - Auxiliary Space : O(V) [For recursion stack and visited set]
======================================================================
```

---

## 10. Time Complexity Analysis

- **Time Complexity**: $O(V + E)$
  - Every vertex $V$ is visited once.
  - Every edge $E$ is traversed twice (once per endpoint in an undirected graph).

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(V)$ auxiliary space for the recursion call stack (or explicit LIFO stack) and the `visited` set.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` captures timestamps around the traversal routine:
```python
start_time = time.perf_counter()
dfs_order = dfs_traversal(g, start_node)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
Returns the traversal order: `A -> B -> D -> E -> F -> C -> G`.

---

## 14. Important Concepts Used
- **Adjacency List**: Efficient graph representation.
- **Recursive Backtracking**: Exploring deeply before unspooling.
- **Cycle Prevention**: Ensuring each node is visited at most once via a lookup set.
