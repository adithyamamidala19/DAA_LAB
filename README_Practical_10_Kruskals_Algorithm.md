# Practical 10: Kruskal's Algorithm (Minimum Spanning Tree)

## 1. Practical Number
**Practical 10**

## 2. Practical Name
**Implementation of Kruskal's Algorithm for Minimum Spanning Tree**

## 3. Objective
To implement Kruskal's greedy algorithm for finding the Minimum Spanning Tree (MST) of a weighted, connected, undirected graph using edge sorting and Disjoint Set Union (DSU / Union-Find) with Path Compression and Union by Rank, avoid cycle formation, calculate and display the total MST cost, measure actual execution time, and analyze theoretical time and space complexities.

---

## 4. Problem Statement
Given an undirected, connected, weighted graph $G = (V, E)$, find a spanning tree $T \subseteq E$ containing all vertices $V$ with exactly $|V| - 1$ edges such that no cycles are formed and the sum of edge weights is minimized.

---

## 5. Algorithm Explanation

### A. Core Concept & Greedy Edge Selection
Unlike Prim's algorithm (which grows a single connected component from a root vertex), Kruskal's algorithm grows a **forest of trees** that gradually merges into a single tree:
1. **Edge Sorting**: All edges in the graph are sorted in non-decreasing order of their weights.
2. **Greedy Addition**: Edges are inspected one by one from lightest to heaviest.
3. **Cycle Avoidance**: An edge $(u, v)$ is added to the MST if and only if $u$ and $v$ belong to different connected components. If $u$ and $v$ are already in the same component, adding $(u, v)$ would create a cycle, so it is discarded.

### B. Disjoint Set Union (DSU / Union-Find) Data Structure
To check whether two vertices belong to the same component in near-constant time:
- **`find(x)` with Path Compression**: Finds the root representative of the set containing $x$. Path compression flattens the tree structure by making every traversed node point directly to the root, optimizing subsequent queries.
- **`union(x, y)` with Union by Rank**: Attaches the smaller depth tree under the root of the deeper tree, keeping tree heights minimal.
- **Cycle Detection**: If `find(u) == find(v)`, vertices $u$ and $v$ already share the same root; adding the edge creates a cycle. If `find(u) != find(v)`, the edge is safe to add, and `union(u, v)` merges the two sets.

---

## 6. Step-by-Step Working

1. **Input Graph**:
   - Vertices: $\{A, B, C, D, E, F\}$
   - Edges: $(A, B, 4), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 8), (C, E, 6), (D, E, 3), (D, F, 6), (E, F, 2)$
2. **Step 1: Sort All Edges by Weight**:
   - $(B, C, 2), (E, F, 2), (D, E, 3), (A, B, 4), (A, C, 4), (B, D, 5), (C, E, 6), (D, F, 6), (C, D, 8)$
3. **Step 2: DSU Iteration**:
   - Pick $(B, C, 2)$: `find(B) != find(C)` $\to$ **Include** $(B, C)$, Union $\{B, C\}$.
   - Pick $(E, F, 2)$: `find(E) != find(F)` $\to$ **Include** $(E, F)$, Union $\{E, F\}$.
   - Pick $(D, E, 3)$: `find(D) != find(E)` $\to$ **Include** $(D, E)$, Union $\{D, E, F\}$.
   - Pick $(A, B, 4)$: `find(A) != find(B)` $\to$ **Include** $(A, B)$, Union $\{A, B, C\}$.
   - Pick $(A, C, 4)$: `find(A) == find(C)` $\to$ **Discard** (Forms cycle $A-B-C-A$).
   - Pick $(B, D, 5)$: `find(B) != find(D)` $\to$ **Include** $(B, D)$, Union $\{A, B, C, D, E, F\}$.
   - Selected $|V| - 1 = 5$ edges $\implies$ Stop.
4. **Total MST Cost**: $2 + 2 + 3 + 4 + 5 = 16$.

---

## 7. Python Implementation File Name
`Practical_10_Kruskals_Algorithm.py`

---

## 8. Sample Input
```python
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
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 10 — KRUSKAL'S ALGORITHM
======================================================================
Graph Vertices: ['A', 'B', 'C', 'D', 'E', 'F']
Total Edges   : 9

Sorted Edges:
  B - C : weight = 2
  E - F : weight = 2
  D - E : weight = 3
  A - B : weight = 4
  A - C : weight = 4
  B - D : weight = 5
  C - E : weight = 6
  D - F : weight = 6
  C - D : weight = 8

Edges in Minimum Spanning Tree:
  B - C : 2
  E - F : 2
  D - E : 3
  A - B : 4
  B - D : 5

Total MST Cost: 16

Execution Time: 0.00002150 seconds (0.0215 ms)

Time Complexity: O(E log E) or O(E log V)
  - Sorting edges: O(E log E)
  - DSU operations (Find/Union with path compression and rank): O(E * α(V)) ≈ O(E)
  Overall Time Complexity dominated by sorting: O(E log E) = O(E log V)
Space Complexity: O(V + E) auxiliary space for storing edges and DSU structures
======================================================================
```

---

## 10. Time Complexity Analysis

| Phase | Operations | Complexity |
| :--- | :--- | :--- |
| **Edge Sorting** | Comparison sort on $E$ edges | $O(E \log E)$ |
| **DSU Initialization** | Make-set for $V$ vertices | $O(V)$ |
| **DSU Find & Union** | $2E$ find operations and $V-1$ union operations | $O(E \cdot \alpha(V))$ |
| **Overall Time Complexity** | Dominated by edge sorting | $O(E \log E) = O(E \log V)$ |

*Here, $\alpha(V)$ is the Inverse Ackermann function, which is $\le 4$ for all practical input sizes, rendering DSU operations effectively linear $O(E)$.*

---

## 11. Space Complexity Analysis

- **Edge Storage & Sorted List**: $O(E)$ space.
- **DSU Parent and Rank Arrays**: $O(V)$ space.
- **MST Result List**: $O(V)$ space.
- **Total Auxiliary Space**: $O(V + E)$.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is used to capture execution duration from edge sorting through MST completion:
```python
start_time = time.perf_counter()
sorted_edges, mst_edges, total_cost = kruskals_mst(vertices, edges)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
- Selected MST edges: `B-C: 2`, `E-F: 2`, `D-E: 3`, `A-B: 4`, `B-D: 5`.
- Total Minimum Spanning Tree Cost = **16** (identical to Prim's Algorithm).

---

## 14. Important Concepts Used
- **Forest of Trees**: Initially, each vertex is an isolated tree; edges unite separate trees until a single spanning tree remains.
- **Cycle Prevention via DSU**: Cycle formation is detected when both endpoints of an edge have the same root.
- **Path Compression & Union by Rank**: Dual optimizations reducing DSU tree depth to near-constant amortized time per operation.
