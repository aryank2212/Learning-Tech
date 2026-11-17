# DSA syllabus

Tick items in [progress/TRACKER.md](../../../progress/TRACKER.md). Each phase needs about 10–15 problems, plus one project.

## Part A – Core DSA

### Phase 1 – Complexity and arrays
- [ ] Big-O, Big-Ω, Big-Θ; counting operations
- [ ] Amortised analysis (dynamic arrays)
- [ ] Two pointers, sliding window, prefix sums
- [ ] Binary search on sorted arrays and on answers

🛠️ Project: benchmark O(n²) against O(n log n) on real input sizes and plot the results.

### Phase 2 – Strings and hashing
- [ ] String operations, immutability, builders
- [ ] Hash maps and sets: frequency counting, anagrams
- [ ] Collisions and load factor
- [ ] Rolling hash introduction

🛠️ Project: find duplicate files in a folder using hashes.

### Phase 3 – Linked lists, stacks, queues
- [ ] Singly and doubly linked lists; reversing a list
- [ ] Stacks: bracket matching, undo history
- [ ] Queues and deques; a first look at BFS
- [ ] Monotonic stack (next greater element)

🛠️ Project: an undo/redo text buffer built from two stacks.

### Phase 4 – Trees and heaps
- [ ] Binary trees: pre-, in-, post- and level-order traversal
- [ ] Binary search trees: insert, search, delete
- [ ] Heaps and priority queues; heapify
- [ ] Tries (prefix trees)

🛠️ Project: autocomplete with a trie.

### Phase 5 – Sorting
- [ ] Insertion and selection sort (know them, and why they are slow)
- [ ] Merge sort, quicksort, heap sort
- [ ] Counting and radix sort; the Ω(n log n) lower bound for comparison sorts
- [ ] Stability

🛠️ Project: implement and benchmark four sorts on ten million numbers.

### Phase 6 – Graphs
- [ ] Adjacency lists vs matrices
- [ ] BFS and DFS; connected components; cycle detection
- [ ] Topological sort
- [ ] Union-find (disjoint set) with path compression
- [ ] Dijkstra and Bellman-Ford
- [ ] Minimum spanning trees: Kruskal and Prim

🛠️ Project: a shortest-route planner on a grid map you draw yourself.

### Phase 7 – Dynamic programming
- [ ] Recursion and memoisation (top-down)
- [ ] Tabulation (bottom-up)
- [ ] 1-D DP: climbing stairs, house robber, coin change
- [ ] 2-D DP: grid paths, longest common subsequence, edit distance
- [ ] Knapsack (0/1 and unbounded)
- [ ] DP on trees

🛠️ Project: a text-diff tool built on longest common subsequence.

### Phase 8 – Greedy and backtracking
- [ ] Greedy choice property; interval scheduling
- [ ] Huffman coding
- [ ] Backtracking: subsets, permutations, N-Queens
- [ ] Pruning and constraint checking

🛠️ Project: a sudoku solver with backtracking.

## Part B – Advanced DSA

### Phase 9 – Advanced trees
- [ ] AVL and red-black trees (balancing and rotations)
- [ ] B-trees and B+ trees (why databases use them)
- [ ] Fenwick tree (BIT) for prefix sums with updates
- [ ] Segment tree with lazy propagation
- [ ] Sparse table; lowest common ancestor (LCA)

🛠️ Project: a range-query and range-update service.

### Phase 10 – Advanced graphs
- [ ] Strongly connected components (Tarjan, Kosaraju)
- [ ] Bridges and articulation points
- [ ] Max flow: Ford–Fulkerson, Edmonds–Karp, Dinic
- [ ] Bipartite matching; min-cost flow (introduction)
- [ ] Floyd–Warshall: all-pairs shortest paths

🛠️ Project: assign tasks to workers with bipartite matching.

### Phase 11 – Advanced strings
- [ ] KMP and the prefix function
- [ ] Z-algorithm
- [ ] Rabin–Karp and rolling hashes
- [ ] Aho–Corasick (many patterns at once)
- [ ] Suffix arrays and LCP arrays

🛠️ Project: a mini grep that searches for thousands of patterns in one pass.

### Phase 12 – Advanced DP and number theory
- [ ] Bitmask DP (travelling salesman on small inputs)
- [ ] Digit DP; DP optimisation (divide and conquer, Knuth)
- [ ] Sieve of Eratosthenes; modular inverse; Chinese Remainder Theorem
- [ ] Combinatorics modulo a prime; matrix exponentiation

🛠️ Project: count valid numbers in a range with digit DP.

### Phase 13 – Randomised and geometric algorithms
- [ ] Las Vegas vs Monte Carlo algorithms
- [ ] Randomised quicksort; skip lists
- [ ] Convex hull (Graham scan, monotone chain)
- [ ] Segment intersection; point-in-polygon

🛠️ Project: draw the convex hull of random points and animate it.

### Phase 14 – Complexity theory
- [ ] P, NP, NP-complete, NP-hard
- [ ] Reductions: SAT → 3-SAT → Clique → Vertex Cover
- [ ] Approximation algorithms (2-approximation for vertex cover; TSP heuristics)
- [ ] Online algorithms and competitive ratio

🛠️ Project: reduce a puzzle to SAT and solve it with a SAT solver (for example `pycosat` or MiniSat).

## Capstone
Write a small library with tested implementations of every structure in Phases 1–9. Benchmark each one. Publish it with a README that explains the complexity of each operation.
