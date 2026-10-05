# Design and Analysis of Algorithms (DAA) Laboratory

A comprehensive repository containing complete, benchmarked, and documented Python implementations of fundamental algorithms for the **Design and Analysis of Algorithms (DAA) Lab**.

Each practical includes the problem statement, algorithm explanation, theoretical time and space complexity analysis, step-by-step trace, and empirical execution runtime measurement using Python's high-precision `time.perf_counter()`.

---

## 📋 Table of Contents

- [Overview & Algorithm Index](#-overview--algorithm-index)
- [Repository Structure](#-repository-structure)
- [Prerequisites & Running Instructions](#-prerequisites--running-instructions)
- [Comprehensive Practical Documentation](#-comprehensive-practical-documentation)
  - [Practical 01: Sorting Algorithms](#practical-01-sorting-algorithms)
    - [1. Bubble Sort](#1-bubble-sort)
    - [2. Insertion Sort](#2-insertion-sort)
    - [3. Selection Sort](#3-selection-sort)
    - [4. Merge Sort](#4-merge-sort)
    - [5. Quick Sort](#5-quick-sort)
  - [Practical 02: Searching Algorithms](#practical-02-searching-algorithms)
    - [1. Linear Search](#1-linear-search)
    - [2. Binary Search](#2-binary-search)
  - [Practical 03: Max-Heap Sort](#practical-03-max-heap-sort)
  - [Practical 04: Factorial (Iterative vs Recursive)](#practical-04-factorial-computation)
    - [1. Iterative Factorial](#1-iterative-factorial)
    - [2. Recursive Factorial](#2-recursive-factorial)
  - [Practical 05: 0/1 Knapsack Problem (Dynamic Programming)](#practical-05-01-knapsack-problem-dynamic-programming)
  - [Practical 06: Matrix Chain Multiplication (Dynamic Programming)](#practical-06-matrix-chain-multiplication-dynamic-programming)
  - [Practical 07: Coin Change / Making Change Problem (Dynamic Programming)](#practical-07-coin-change--making-change-dynamic-programming)
  - [Practical 08: Graph Traversals (BFS & DFS)](#practical-08-graph-traversals)
    - [1. Breadth First Search (BFS)](#1-breadth-first-search-bfs)
    - [2. Depth First Search (DFS)](#2-depth-first-search-dfs)
  - [Practical 09: Prim's Algorithm (Minimum Spanning Tree)](#practical-09-prims-algorithm-minimum-spanning-tree)
  - [Practical 10: Kruskal's Algorithm (Minimum Spanning Tree)](#practical-10-kruskals-algorithm-minimum-spanning-tree)
- [Master Complexity Comparison Table](#-master-complexity-comparison-table)

---

## 📊 Overview & Algorithm Index

| Practical # | Topic / Algorithm | Paradigm / Technique | Source File | Time Complexity (Avg / Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Practical 01** | Bubble Sort | Brute Force / Comparison | `Practical_01_Bubble_Sort.py` | $O(n^2) / O(n^2)$ | $O(1)$ |
| **Practical 01** | Insertion Sort | Incremental / Comparison | `Practical_01_Insertion_Sort.py` | $O(n^2) / O(n^2)$ | $O(1)$ |
| **Practical 01** | Selection Sort | Brute Force / In-place | `Practical_01_Selection_Sort.py` | $O(n^2) / O(n^2)$ | $O(1)$ |
| **Practical 01** | Merge Sort | Divide and Conquer | `Practical_01_Merge_Sort.py` | $O(n \log n) / O(n \log n)$ | $O(n)$ |
| **Practical 01** | Quick Sort | Divide and Conquer | `Practical_01_Quick_Sort.py` | $O(n \log n) / O(n^2)$ | $O(\log n)$ |
| **Practical 02** | Linear Search | Sequential Search | `Practical_02_Linear_Search.py` | $O(n) / O(n)$ | $O(1)$ |
| **Practical 02** | Binary Search | Decrease and Conquer | `Practical_02_Binary_Search.py` | $O(\log n) / O(\log n)$ | $O(1)$ |
| **Practical 03** | Max-Heap Sort | Heap Data Structure | `Practical_03_Max_Heap_Sort.py` | $O(n \log n) / O(n \log n)$ | $O(1)$ |
| **Practical 04** | Iterative Factorial | State Accumulation Loop | `Practical_04_Iterative_Factorial.py` | $O(n) / O(n)$ | $O(1)$ |
| **Practical 04** | Recursive Factorial | Mathematical Recurrence | `Practical_04_Recursive_Factorial.py` | $O(n) / O(n)$ | $O(n)$ |
| **Practical 05** | 0/1 Knapsack Problem | Dynamic Programming (Tabulation) | `Practical_05_Knapsack_DP.py` | $O(n \cdot W) / O(n \cdot W)$ | $O(n \cdot W)$ |
| **Practical 06** | Matrix Chain Multiplication | Dynamic Programming (Chain DP) | `Practical_06_Chain_Matrix_Multiplication_DP.py` | $O(n^3) / O(n^3)$ | $O(n^2)$ |
| **Practical 07** | Coin Change Problem | Dynamic Programming (Unbounded DP) | `Practical_07_Coin_Change_DP.py` | $O(n \cdot V) / O(n \cdot V)$ | $O(V)$ |
| **Practical 08** | Breadth First Search (BFS) | Graph Traversal (FIFO Queue) | `Practical_08_BFS.py` | $O(V + E) / O(V + E)$ | $O(V)$ |
| **Practical 08** | Depth First Search (DFS) | Graph Traversal (Recursion / Stack) | `Practical_08_DFS.py` | $O(V + E) / O(V + E)$ | $O(V)$ |
| **Practical 09** | Prim's Algorithm (MST) | Greedy (Min-Heap / Priority Queue) | `Practical_09_Prims_Algorithm.py` | $O(E \log V) / O(E \log V)$ | $O(V + E)$ |
| **Practical 10** | Kruskal's Algorithm (MST) | Greedy + Disjoint Set Union (DSU) | `Practical_10_Kruskals_Algorithm.py` | $O(E \log E) / O(E \log E)$ | $O(V + E)$ |

---

## 📁 Repository Structure

```text
DAA_LAB/
│
├── Practical_01_Bubble_Sort.py
├── Practical_01_Insertion_Sort.py
├── Practical_01_Merge_Sort.py
├── Practical_01_Quick_Sort.py
├── Practical_01_Selection_Sort.py
│
├── Practical_02_Linear_Search.py
├── Practical_02_Binary_Search.py
│
├── Practical_03_Max_Heap_Sort.py
│
├── Practical_04_Iterative_Factorial.py
├── Practical_04_Recursive_Factorial.py
│
├── Practical_05_Knapsack_DP.py
│
├── Practical_06_Chain_Matrix_Multiplication_DP.py
│
├── Practical_07_Coin_Change_DP.py
│
├── Practical_08_BFS.py
├── Practical_08_DFS.py
│
├── Practical_09_Prims_Algorithm.py
│
├── Practical_10_Kruskals_Algorithm.py
│
├── Sorting_Project_Summary.docx
└── README.md
```

---

## ⚙️ Prerequisites & Running Instructions

### Prerequisites
- **Python 3.x** (Standard Library only; no external third-party dependencies required).

### How to Run Any Practical
Execute the corresponding Python file directly from the terminal:

```bash
# Practical 01: Sorting Algorithms
python Practical_01_Bubble_Sort.py
python Practical_01_Insertion_Sort.py
python Practical_01_Selection_Sort.py
python Practical_01_Merge_Sort.py
python Practical_01_Quick_Sort.py

# Practical 02: Searching Algorithms
python Practical_02_Linear_Search.py
python Practical_02_Binary_Search.py

# Practical 03: Heap Sort
python Practical_03_Max_Heap_Sort.py

# Practical 04: Factorial
python Practical_04_Iterative_Factorial.py
python Practical_04_Recursive_Factorial.py

# Practical 05: 0/1 Knapsack
python Practical_05_Knapsack_DP.py

# Practical 06: Matrix Chain Multiplication
python Practical_06_Chain_Matrix_Multiplication_DP.py

# Practical 07: Coin Change
python Practical_07_Coin_Change_DP.py

# Practical 08: Graph Traversals
python Practical_08_BFS.py
python Practical_08_DFS.py

# Practical 09: Prim's Algorithm (MST)
python Practical_09_Prims_Algorithm.py

# Practical 10: Kruskal's Algorithm (MST)
python Practical_10_Kruskals_Algorithm.py
```

### High-Precision Runtime Measurement
Each script measures real-world wall-clock execution time using:
```python
import time

start_time = time.perf_counter()
# Execute algorithm
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 📖 Comprehensive Practical Documentation

---

### Practical 01: Sorting Algorithms

#### 1. Bubble Sort
- **File**: `Practical_01_Bubble_Sort.py`
- **Concept**: Repeatedly passes through the list, compares adjacent elements, and swaps them if they are in the wrong order. Larger elements bubble up to the end of the array.
- **Optimization**: Uses a boolean `swapped` flag to terminate early in $O(n)$ time if the array is already sorted.
- **Complexity**:
  - **Best Case**: $O(n)$
  - **Average Case**: $O(n^2)$
  - **Worst Case**: $O(n^2)$
  - **Auxiliary Space**: $O(1)$ (In-place, Stable)
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
- **Sample Output**: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`

#### 2. Insertion Sort
- **File**: `Practical_01_Insertion_Sort.py`
- **Concept**: Builds the sorted array one element at a time by picking an element (`key`) and shifting larger preceding elements one position to the right.
- **Characteristics**: Extremely efficient on small datasets and nearly-sorted arrays.
- **Complexity**:
  - **Best Case**: $O(n)$
  - **Average Case**: $O(n^2)$
  - **Worst Case**: $O(n^2)$
  - **Auxiliary Space**: $O(1)$ (In-place, Stable)
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
- **Sample Output**: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`

#### 3. Selection Sort
- **File**: `Practical_01_Selection_Sort.py`
- **Concept**: Divides the array into sorted and unsorted subarrays. Repeatedly finds the minimum element in the unsorted portion and swaps it with the first unsorted element.
- **Characteristics**: Performs at most $O(n)$ memory writes (swaps), optimal when write operations are expensive.
- **Complexity**:
  - **Best Case**: $O(n^2)$
  - **Average Case**: $O(n^2)$
  - **Worst Case**: $O(n^2)$
  - **Auxiliary Space**: $O(1)$ (In-place, Unstable)
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
- **Sample Output**: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`

#### 4. Merge Sort
- **File**: `Practical_01_Merge_Sort.py`
- **Concept**: Classic Divide-and-Conquer algorithm. Recursively halves the array until base subarrays of length $\le 1$ remain, then merges two sorted halves using a two-pointer linear scan.
- **Recurrence**: $T(n) = 2T(n/2) + \Theta(n) \implies \Theta(n \log n)$ by Master Theorem.
- **Complexity**:
  - **Best / Average / Worst Case**: $O(n \log n)$
  - **Auxiliary Space**: $O(n)$ (Stable)
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
- **Sample Output**: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`

#### 5. Quick Sort
- **File**: `Practical_01_Quick_Sort.py`
- **Concept**: Selects a pivot element, partitions the array into elements strictly smaller, equal, and strictly greater than the pivot, and recursively sorts the sub-partitions.
- **Complexity**:
  - **Best Case**: $O(n \log n)$ (Balanced partitioning)
  - **Average Case**: $O(n \log n)$
  - **Worst Case**: $O(n^2)$ (Degenerate unbalanced partitioning)
  - **Auxiliary Space**: $O(\log n)$ call stack space ($O(n)$ worst-case)
- **Sample Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
- **Sample Output**: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`

---

### Practical 02: Searching Algorithms

#### 1. Linear Search
- **File**: `Practical_02_Linear_Search.py`
- **Concept**: Sequentially checks every item in the dataset from index $0$ to $n-1$ until a match is found or the collection is exhausted.
- **Preconditions**: None (works on unsorted/arbitrary data).
- **Complexity**:
  - **Best Case**: $O(1)$ (Target at index 0)
  - **Average Case**: $O(n)$ ($ (n+1)/2 $ comparisons)
  - **Worst Case**: $O(n)$ (Target at end or absent)
  - **Auxiliary Space**: $O(1)$
- **Sample Dataset**: `[45, 12, 89, 34, 67, 23, 78, 90, 11, 56]`
- **Sample Queries**:
  - Search `67` $\to$ Found at index 4 (Position 5)
  - Search `99` $\to$ Target not found (returns `-1`)

#### 2. Binary Search
- **File**: `Practical_02_Binary_Search.py`
- **Concept**: Operates on a sorted dataset. Computes midpoint $mid = low + \lfloor (high - low)/2 \rfloor$, compares target with $A[mid]$, and halves the search space in each iteration.
- **Preconditions**: Dataset must be sorted in monotonic non-decreasing order.
- **Complexity**:
  - **Best Case**: $O(1)$ (Target at initial middle index)
  - **Average Case**: $O(\log n)$
  - **Worst Case**: $O(\log n)$
  - **Auxiliary Space**: $O(1)$ iterative, $O(\log n)$ recursive
- **Sample Dataset**: `[11, 12, 23, 34, 45, 56, 67, 78, 89, 90]`
- **Sample Queries**:
  - Search `67` $\to$ Found at index 6 (Position 7)
  - Search `99` $\to$ Target not found (returns `-1`)

---

### Practical 03: Max-Heap Sort

- **File**: `Practical_03_Max_Heap_Sort.py`
- **Concept**:
  1. **Binary Heap**: Array representation of a complete binary tree where node $i$ has children at $2i+1$ and $2i+2$, parent at $(i-1)//2$.
  2. **Max-Heap Property**: Parent key $\ge$ child keys ($A[\text{parent}] \ge A[\text{child}]$).
  3. **`heapify`**: Restores the max-heap property in $O(\log n)$ time by sifting down root $i$.
  4. **`build_max_heap`**: Transforms an arbitrary array into a valid Max Heap in $O(n)$ time by calling `heapify` from $\lfloor n/2 \rfloor - 1$ down to $0$.
  5. **Sort Loop**: Repeatedly swaps the root maximum element $A[0]$ with $A[i]$, reduces heap size by 1, and calls `heapify` on root.
- **Complexity**:
  - **Building Max-Heap**: $O(n)$
  - **$n-1$ Root Extractions**: $(n-1) \times O(\log n) = O(n \log n)$
  - **Overall Time Complexity**: $O(n \log n)$ (Best, Average, and Worst Case)
  - **Auxiliary Space**: $O(1)$ (In-place sort)
- **Sample Input**: `[12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]`
- **Max-Heap Built**: `[45, 23, 33, 12, 19, 7, 13, 1, 5, 11, 6]`
- **Sorted Array**: `[1, 5, 6, 7, 11, 12, 13, 19, 23, 33, 45]`

---

### Practical 04: Factorial Computation

#### 1. Iterative Factorial
- **File**: `Practical_04_Iterative_Factorial.py`
- **Concept**: Computes $n! = \prod_{i=1}^{n} i$ using a single `for` loop with an accumulator variable initialized to 1.
- **Complexity**:
  - **Time Complexity**: $O(n)$ ($O(1)$ for $n \le 1$)
  - **Auxiliary Space**: $O(1)$
- **Sample Input**: $n = 20$
- **Calculated Factorial**: $20! = 2,432,902,008,176,640,000$

#### 2. Recursive Factorial
- **File**: `Practical_04_Recursive_Factorial.py`
- **Concept**: Computes $n!$ via recurrence:
  $$fact(n) = \begin{cases} 1 & \text{if } n \le 1 \\ n \times fact(n - 1) & \text{if } n > 1 \end{cases}$$
- **Complexity**:
  - **Time Complexity**: $O(n)$
  - **Auxiliary Space**: $O(n)$ (Depth of $n$ call stack activation records)
- **Sample Input**: $n = 20$
- **Calculated Factorial**: $20! = 2,432,902,008,176,640,000$

---

### Practical 05: 0/1 Knapsack Problem (Dynamic Programming)

- **File**: `Practical_05_Knapsack_DP.py`
- **Problem**: Given $n$ items with weights $w_i$ and values $v_i$, maximize total value in a knapsack of weight capacity $W$. Each item must be taken entirely (1) or left behind (0).
- **DP State & Recurrence**:
  Let $dp[i][w]$ be the maximum value attainable using a subset of the first $i$ items with capacity $w$:
  $$dp[i][w] = \begin{cases}
  \max(v_{i-1} + dp[i-1][w - w_{i-1}],\; dp[i-1][w]) & \text{if } w_{i-1} \le w \\
  dp[i-1][w] & \text{if } w_{i-1} > w
  \end{cases}$$
- **Backtracking**: Traces backwards from $dp[n][W]$: if $dp[i][w] \ne dp[i-1][w]$, item $i-1$ was chosen and $w \leftarrow w - w_{i-1}$.
- **Complexity**:
  - **Time Complexity**: $O(n \cdot W)$ (Pseudo-polynomial)
  - **Auxiliary Space**: $O(n \cdot W)$ for 2D DP table ($O(W)$ if only optimal value needed)
- **Sample Input**:
  - Items: Laptop ($w=2, v=3$), Camera ($w=3, v=4$), Watch ($w=4, v=5$), Headphones ($w=5, v=6$)
  - Capacity $W = 5$
- **DP Tabulation Matrix**:
  ```text
  Item \ W |    0    1    2    3    4    5
  ------------------------------------------
  Item  0  |    0    0    0    0    0    0
  Item  1  |    0    0    3    3    3    3
  Item  2  |    0    0    3    4    4    7
  Item  3  |    0    0    3    4    5    7
  Item  4  |    0    0    3    4    5    7
  ```
- **Optimal Output**: Maximum Value = **7**, Selected Items: Item 1 (Laptop) & Item 2 (Camera), Total Weight = 5/5.

---

### Practical 06: Matrix Chain Multiplication (Dynamic Programming)

- **File**: `Practical_06_Chain_Matrix_Multiplication_DP.py`
- **Problem**: Given a chain of $n$ matrices $\langle A_1, A_2, \dots, A_n \rangle$ where $A_i$ has dimension $p_{i-1} \times p_i$, find the parenthesization that minimizes scalar multiplications.
- **Recurrence Relation**:
  Let $m[i][j]$ be the minimum scalar multiplications for computing $A_i \dots A_j$:
  $$m[i][j] = \begin{cases}
  0 & \text{if } i = j \\
  \min_{i \le k < j} \left( m[i][k] + m[k+1][j] + p_{i-1} p_k p_j \right) & \text{if } i < j
  \end{cases}$$
  Optimal split index $k$ is stored in $s[i][j]$.
- **Evaluation Order**: Solves subchains in order of increasing length $L = 2, 3, \dots, n$.
- **Complexity**:
  - **Time Complexity**: $O(n^3)$ (Three nested loops for length $L$, start $i$, split $k$)
  - **Auxiliary Space**: $O(n^2)$ for $m$ and $s$ tables
- **Sample Input**: Dimensions $p = [10, 20, 30, 40, 30]$ (4 matrices: $A_1: 10\times20, A_2: 20\times30, A_3: 30\times40, A_4: 40\times30$)
- **Optimal Output**:
  - Minimum Scalar Multiplications: **30,000**
  - Optimal Parenthesization: `(((A1 x A2) x A3) x A4)`

---

### Practical 07: Coin Change / Making Change (Dynamic Programming)

- **File**: `Practical_07_Coin_Change_DP.py`
- **Problem**: Given coin denominations $C = \{c_1, c_2, \dots, c_n\}$ with unlimited supply, find the minimum number of coins to form target amount $V$. If impossible, return $-1$.
- **Why DP over Greedy**: Greedy choices fail for non-canonical coin systems (e.g., coins $\{1, 5, 6, 8\}$, target $11$: Greedy gives $8+1+1+1 = 4$ coins; DP gives optimal $5+6 = 2$ coins).
- **DP State & Recurrence**:
  $$dp[a] = \begin{cases}
  0 & \text{if } a = 0 \\
  \min_{c \in C, c \le a} (dp[a - c] + 1) & \text{if } a > 0
  \end{cases}$$
  Parent array $parent[a]$ stores chosen coin denomination $c$.
- **Complexity**:
  - **Time Complexity**: $O(n \cdot V)$ where $n = |C|$ and $V$ is target amount
  - **Auxiliary Space**: $O(V)$ for 1D DP table
- **Sample Test Cases**:
  1. Standard: Coins `[1, 2, 5, 10, 20, 50]`, Target = 43 $\to$ **4 coins** `[1, 2, 20, 20]`
  2. Non-Greedy Case: Coins `[1, 5, 6, 8]`, Target = 11 $\to$ **2 coins** `[5, 6]`
  3. Impossible Case: Coins `[2, 4, 6]`, Target = 7 $\to$ **IMPOSSIBLE (-1)**

---

### Practical 08: Graph Traversals

#### 1. Breadth First Search (BFS)
- **File**: `Practical_08_BFS.py`
- **Concept**: Explores graph vertices level-by-level (by shortest hop distance) starting from source $S$ using a FIFO Queue (`collections.deque`) and a `visited` set.
- **Complexity**:
  - **Time Complexity**: $O(V + E)$ (Each vertex queued once, each edge explored twice)
  - **Auxiliary Space**: $O(V)$ for queue and visited set
- **Sample Graph**: Vertices $\{A, B, C, D, E, F, G\}$, Start = $A$
- **Traversal Sequence**: `A -> B -> C -> D -> E -> F -> G`

#### 2. Depth First Search (DFS)
- **File**: `Practical_08_DFS.py`
- **Concept**: Explores graph as deep as possible along each branch before backtracking, using recursion / explicit LIFO stack and a `visited` set.
- **Complexity**:
  - **Time Complexity**: $O(V + E)$
  - **Auxiliary Space**: $O(V)$ for recursion stack and visited set
- **Sample Graph**: Vertices $\{A, B, C, D, E, F, G\}$, Start = $A$
- **Traversal Sequence**: `A -> B -> D -> E -> F -> C -> G`

---

### Practical 09: Prim's Algorithm (Minimum Spanning Tree)

- **File**: `Practical_09_Prims_Algorithm.py`
- **Problem**: Find a tree connecting all vertices in a weighted, connected, undirected graph $G=(V, E)$ with minimum total edge weight.
- **Greedy Cut Strategy**:
  - Maintains visited set $S$ and unvisited set $V \setminus S$.
  - Uses a Min-Heap (Priority Queue via `heapq`) to greedily extract the minimum weight "light edge" crossing the cut $(S, V \setminus S)$.
  - Incorporates the new vertex into $S$ and pushes all its incident edges to unvisited neighbors onto the heap.
- **Complexity**:
  - **Time Complexity**: $O(E \log V)$ with Binary Min-Heap and Adjacency List ($O(V^2)$ with Adjacency Matrix)
  - **Auxiliary Space**: $O(V + E)$
- **Sample Graph**:
  - Edges: $(A, B, 4), (A, C, 4), (B, C, 2), (B, D, 5), (C, D, 8), (C, E, 6), (D, E, 3), (D, F, 6), (E, F, 2)$
- **MST Result**:
  - Selected Edges: `A - B (4)`, `B - C (2)`, `B - D (5)`, `D - E (3)`, `E - F (2)`
  - **Total MST Cost**: **16**

---

### Practical 10: Kruskal's Algorithm (Minimum Spanning Tree)

- **File**: `Practical_10_Kruskals_Algorithm.py`
- **Problem**: Find a Minimum Spanning Tree using edge-centric greedy selection and Disjoint Set Union (DSU / Union-Find).
- **Core Mechanism**:
  1. **Edge Sorting**: Sorts all $E$ edges in non-decreasing order of weight ($O(E \log E)$).
  2. **Greedy Addition**: Inspects edges in ascending order.
  3. **Cycle Prevention via DSU**:
     - `find(u)` with **Path Compression** identifies the root representative.
     - `union(u, v)` with **Union by Rank** merges trees efficiently.
     - If `find(u) == find(v)`, edge $(u, v)$ is discarded to prevent cycle formation.
     - If `find(u) != find(v)`, edge $(u, v)$ is included in MST and sets are merged.
  4. Stops once $V-1$ edges are selected.
- **Complexity**:
  - **Time Complexity**: $O(E \log E) = O(E \log V)$ (Dominated by edge sorting; DSU operations run in near-linear $O(E \cdot \alpha(V))$)
  - **Auxiliary Space**: $O(V + E)$
- **Sample Graph**: Same 6-vertex, 9-edge weighted graph as Practical 09.
- **MST Result**:
  - Selected Edges: `B - C (2)`, `E - F (2)`, `D - E (3)`, `A - B (4)`, `B - D (5)`
  - **Total MST Cost**: **16** (Matches Prim's MST cost)

---

## ⚡ Master Complexity Comparison Table

| Practical | Algorithm | Best Case Time | Average Case Time | Worst Case Time | Auxiliary Space | In-Place? | Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **01** | Bubble Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **01** | Insertion Sort | $O(n)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | Yes |
| **01** | Selection Sort | $O(n^2)$ | $O(n^2)$ | $O(n^2)$ | $O(1)$ | Yes | No |
| **01** | Merge Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(n)$ | No | Yes |
| **01** | Quick Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n^2)$ | $O(\log n)$ | Yes | No |
| **02** | Linear Search | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | Yes | N/A |
| **02** | Binary Search | $O(1)$ | $O(\log n)$ | $O(\log n)$ | $O(1)$ | Yes | N/A |
| **03** | Max-Heap Sort | $O(n \log n)$ | $O(n \log n)$ | $O(n \log n)$ | $O(1)$ | Yes | No |
| **04** | Iterative Factorial | $O(1)$ | $O(n)$ | $O(n)$ | $O(1)$ | N/A | N/A |
| **04** | Recursive Factorial | $O(1)$ | $O(n)$ | $O(n)$ | $O(n)$ stack | N/A | N/A |
| **05** | 0/1 Knapsack DP | $O(n \cdot W)$ | $O(n \cdot W)$ | $O(n \cdot W)$ | $O(n \cdot W)$ | No | N/A |
| **06** | Matrix Chain DP | $O(n^3)$ | $O(n^3)$ | $O(n^3)$ | $O(n^2)$ | No | N/A |
| **07** | Coin Change DP | $O(n \cdot V)$ | $O(n \cdot V)$ | $O(n \cdot V)$ | $O(V)$ | No | N/A |
| **08** | BFS Graph Traversal | $O(V + E)$ | $O(V + E)$ | $O(V + E)$ | $O(V)$ | No | N/A |
| **08** | DFS Graph Traversal | $O(V + E)$ | $O(V + E)$ | $O(V + E)$ | $O(V)$ | No | N/A |
| **09** | Prim's MST Algorithm | $O(E \log V)$ | $O(E \log V)$ | $O(E \log V)$ | $O(V + E)$ | No | N/A |
| **10** | Kruskal's MST Algorithm | $O(E \log E)$ | $O(E \log E)$ | $O(E \log E)$ | $O(V + E)$ | No | N/A |

---

## 📜 License & Usage
This repository is developed for academic, educational, and reference purposes under the DAA Laboratory Curriculum. You are free to study, execute, and extend these implementations.
