# Practical 09: Prim's Algorithm (Minimum Spanning Tree)

## 1. Practical Number
**Practical 09**

## 2. Practical Name
**Implementation of Prim's Algorithm for Minimum Spanning Tree**

## 3. Objective
To implement Prim's greedy algorithm for finding the Minimum Spanning Tree (MST) of a weighted, connected, undirected graph, display each selected edge along with its individual weight, calculate and print the total MST cost, measure actual execution time using `time.perf_counter()`, and thoroughly analyze its theoretical time and space complexities.

---

## 4. Problem Statement
Given a connected, undirected graph $G = (V, E)$ where each edge $(u, v) \in E$ has an associated non-negative weight $w(u, v)$, find an acyclic subset of edges $T \subseteq E$ that connects all vertices $V$ together such that the total weight:
$$w(T) = \sum_{(u, v) \in T} w(u, v)$$
is minimized.

---

## 5. Algorithm Explanation

### A. Core Concept & Greedy Strategy
Prim's algorithm builds the MST **vertex by vertex** starting from an arbitrary root vertex:
1. It maintains two disjoint sets of vertices:
   - $S$: Vertices already included in the growing MST.
   - $V \setminus S$: Vertices not yet included in the MST.
2. At each step, it considers all "cut edges" $(u, v)$ crossing the cut $(S, V \setminus S)$ where $u \in S$ and $v \in V \setminus S$.
3. By the **Cut Property of MSTs**, the light edge (minimum-weight edge) crossing the cut is guaranteed to belong to some MST.
4. The algorithm greedily selects this light edge $(u, v)$, adds $v$ to $S$, adds $(u, v)$ to the MST edge list, and repeats until $S = V$ (containing $V-1$ edges).

### B. Min-Heap / Priority Queue Implementation
To achieve optimal time efficiency:
- A Priority Queue (Min-Heap using Python's `heapq`) stores candidates as `(weight, u, v)`.
- When a vertex $u$ is added to $S$, all incident edges $(u, w)$ with $w \notin S$ are pushed onto the min-heap.
- In each extraction, the heap pops the minimum weight edge. If the target vertex is already visited, it is discarded; otherwise, the vertex is incorporated into the MST.

---

## 6. Step-by-Step Working

1. **Input Graph**:
   - Vertices: $\{A, B, C, D, E, F\}$
   - Weighted Edges:
     - $(A, B, 4), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 8), (C, E, 6), (D, E, 3), (D, F, 6), (E, F, 2)$
2. **Execution Steps starting from $A$**:
   - $S = \{A\}$, Heap contains: $(4, A, B), (4, A, C)$.
   - Pop $(4, A, B) \implies$ Add $B$, $S = \{A, B\}$. Heap pushes $B$'s edges: $(2, B, C), (5, B, D)$.
   - Pop $(2, B, C) \implies$ Add $C$, $S = \{A, B, C\}$. Heap pushes $C$'s edges: $(6, C, E), (8, C, D)$.
   - Pop $(4, A, C) \implies$ Skipped ($C$ already in $S$).
   - Pop $(5, B, D) \implies$ Add $D$, $S = \{A, B, C, D\}$. Heap pushes $(3, D, E), (6, D, F)$.
   - Pop $(3, D, E) \implies$ Add $E$, $S = \{A, B, C, D, E\}$. Heap pushes $(2, E, F)$.
   - Pop $(2, E, F) \implies$ Add $F$, $S = \{A, B, C, D, E, F\}$.
   - All $V = 6$ vertices included ($V - 1 = 5$ edges selected).
3. **Total MST Cost**: $4 + 2 + 5 + 3 + 2 = 16$.

---

## 7. Python Implementation File Name
`Practical_09_Prims_Algorithm.py`

---

## 8. Sample Input
```python
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
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 9 — PRIM'S ALGORITHM
======================================================================
Graph Adjacency List with Edge Weights:
  Node A -> [B(w=4), C(w=4)]
  Node B -> [A(w=4), C(w=2), D(w=5)]
  Node C -> [A(w=4), B(w=2), D(w=8), E(w=6)]
  Node D -> [B(w=5), C(w=8), E(w=3), F(w=6)]
  Node E -> [C(w=6), D(w=3), F(w=2)]
  Node F -> [D(w=6), E(w=2)]

Edges in Minimum Spanning Tree:
  A - B : 4
  B - C : 2
  B - D : 5
  D - E : 3
  E - F : 2

Total MST Cost: 16

Execution Time: 0.00001920 seconds (0.0192 ms)

Time Complexity:
  - Using Min-Heap with Adjacency List: O(E log V)
  - Using Adjacency Matrix: O(V²)
  where V is the number of vertices and E is the number of edges.
Space Complexity: O(V + E) auxiliary space for graph and priority queue
======================================================================
```

---

## 10. Time Complexity Analysis

| Implementation Method | Time Complexity | Best For |
| :--- | :--- | :--- |
| **Adjacency List + Binary Min-Heap** | $O(E \log V)$ | Sparse graphs ($E \ll V^2$) |
| **Adjacency Matrix + Linear Scan** | $O(V^2)$ | Dense graphs ($E \approx V^2$) |
| **Fibonacci Heap + Adjacency List** | $O(E + V \log V)$ | Theoretically optimal |

- In our Min-Heap implementation:
  - Each vertex is inserted/popped from heap at most once per incident edge: $O(E \log E) = O(E \log V)$.
  - Visited set checks take $O(1)$ average time.

---

## 11. Space Complexity Analysis

- **Graph Storage**: Adjacency list requires $O(V + E)$ space.
- **Priority Queue & Visited Set**: Holds at most $E$ items and $V$ visited markers.
- **Total Auxiliary Space**: $O(V + E)$.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` precisely measures the MST computation loop:
```python
start_time = time.perf_counter()
mst_edges, total_cost = prims_mst(g, 'A')
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
- Selected MST edges: `A-B: 4`, `B-C: 2`, `B-D: 5`, `D-E: 3`, `E-F: 2`.
- Total Minimum Spanning Tree Cost = **16**.

---

## 14. Important Concepts Used
- **Greedy Choice Property**: Locally optimal choice (lightest incident cut edge) leads to a globally optimal solution.
- **Cut Property**: For any cut $(S, V \setminus S)$, the minimum-weight crossing edge belongs to an MST.
- **Priority Queue (Min-Heap)**: Accelerates minimum edge extraction from $O(V)$ down to $O(\log V)$.
