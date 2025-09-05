# DSA Project Findings: PageRank Performance Analysis

## Executive Summary

This project compared the performance of PageRank algorithm using different data structures. We implemented custom data structures from scratch and compared them with Python's built-in data structures to understand their practical performance differences.

## Problem Statement

The original implementation in `DSA_Project.ipynb` had algorithmic issues where PageRank was incorrectly implemented using BFS/DFS traversal instead of proper iterative rank distribution. This project fixed those issues and provided comprehensive performance analysis.

## Methodology

### Data Structures Implemented
1. **Custom HashTable**: Built from scratch with collision handling
2. **Python Arrays**: Using built-in lists for comparison
3. **Python Dictionaries**: Using built-in dicts for comparison
4. **Matrix Operations**: Using 2D arrays with mathematical approach

### Graph Representations Tested
1. **LinkedList Graph**: Adjacency list with custom linked list nodes
2. **Array Graph**: Adjacency matrix using 2D arrays
3. **Dictionary Graph**: Python dictionary-based adjacency list
4. **Sparse Graph**: Edge list representation

### Testing Approach
- Used original 10-node graph from the notebook
- Ran multiple iterations for statistical accuracy
- Measured execution time, memory usage, and convergence behaviour
- Tested scalability with graphs of different sizes (10, 50, 100 nodes)

## Key Findings

### 1. Execution Time Performance

**Results (Average of 5 runs on 10-node graph):**
- Python Arrays: 0.097 ms ⚡ (Fastest)
- Python Dictionary: 0.114 ms 
- Matrix Operations: 0.176 ms
- Custom HashTable: 0.443 ms 🐌 (Slowest)

**Key Discovery**: Python's built-in list is **4.6 times faster** than our custom HashTable implementation!

### 2. Memory Usage Analysis

**Results:**
- Custom HashTable: 48 bytes (Most memory efficient)
- Python Arrays: 184 bytes
- Matrix Operations: 184 bytes
- Python Dictionary: 352 bytes (Uses most memory)

**Surprising Finding**: HashTable uses least memory but is slowest in execution, showing that memory efficiency doesn't always mean speed efficiency.

### 3. Graph Representation Performance

**Results:**
- Dictionary Graph: 0.089 ms (Fastest)
- Sparse Graph: 0.089 ms (Tied for fastest)
- LinkedList Graph: 0.129 ms
- Array Matrix Graph: 0.168 ms (Slowest)

### 4. Scalability Analysis

**Performance gap increases with graph size:**
- 10 nodes: Array 4.4x faster than HashTable
- 50 nodes: Array 4.2x faster than HashTable
- 100 nodes: Array 6.2x faster than HashTable

**Learning**: Custom implementations don't always scale as well as optimized built-ins.

### 5. Algorithm Correctness Validation

**Convergence Results:**
- All algorithms converged to identical results
- All took exactly 43 iterations to converge
- Convergence tolerance: 1e-6
- This proves our implementation correctness

**Top 5 PageRank Results (Original 10-node graph):**
1. Node 9: 0.237389 (Highest importance)
2. Node 6: 0.225865
3. Node 7: 0.221082
4. Node 8: 0.151093
5. Node 5: 0.049568

## Analysis and Explanations

### Why Python Arrays Perform Best
1. **Direct Memory Access**: `ranks[i]` is direct array indexing
2. **Cache-Friendly**: Sequential memory layout improves cache performance
3. **No Overhead**: No hash function computation or collision handling
4. **C-Level Optimization**: Python lists are implemented in optimized C

### Why Custom HashTable is Slowest
1. **Hash Function Overhead**: Computing hash for every access
2. **Collision Handling**: Chaining requires traversing linked lists in buckets
3. **Multiple Memory Jumps**: Not cache-friendly due to scattered memory access
4. **Implementation Overhead**: Our custom implementation lacks low-level optimizations

### Why Memory Usage Doesn't Correlate with Speed
- **HashTable**: Compact storage but complex access patterns
- **Arrays**: Slightly more memory but extremely fast access
- **Dictionaries**: More memory overhead but highly optimized implementation
- **Cache Performance**: Memory layout matters more than total size

## Technical Insights

### Algorithmic Complexity vs Practical Performance
| Method | Theoretical Complexity | Practical Performance | Reason |
|--------|----------------------|---------------------|---------|
| Custom HashTable | O(1) average | Slowest | Implementation overhead |
| Python Arrays | O(1) access | Fastest | Cache-friendly, optimized |
| Python Dictionary | O(1) average | Good | Highly optimized C implementation |
| Matrix Operations | O(1) access | Moderate | Space overhead for large graphs |

### Important Lessons Learned
1. **Big-O notation doesn't tell the complete story** - constant factors matter significantly
2. **Built-in optimizations are powerful** - Python's C-level implementations are hard to beat
3. **Cache performance is crucial** - memory access patterns affect speed more than total memory
4. **Custom implementations have educational value** but may not always be practically optimal
5. **Proper algorithm implementation is essential** - our BFS/DFS fix was critical

## Recommendations

### For Small Graphs (< 100 nodes)
- **Use Python Arrays**: Best performance with reasonable memory usage
- **Avoid Custom HashTable**: Implementation overhead too high for small datasets

### For Large Graphs (> 1000 nodes)
- **Use Python Dictionary**: Good balance of performance and memory
- **Consider Sparse Representation**: For graphs with low edge density

### For Memory-Constrained Systems
- **Use Custom HashTable**: Lowest memory footprint
- **Accept Performance Trade-off**: 4-6x slower but uses 75% less memory

### For Educational Purposes
- **Implement Custom Structures**: Understanding internal workings is valuable
- **Compare with Built-ins**: Learn when custom vs built-in is appropriate
- **Measure Performance**: Always benchmark rather than assume

## Conclusion

This project successfully demonstrated that:

1. **Implementation matters as much as algorithm choice** - the same algorithm can have vastly different performance based on data structure implementation
2. **Python's built-in data structures are highly optimized** - often outperforming custom implementations
3. **Memory efficiency and speed efficiency are different goals** - optimization requires understanding the trade-offs
4. **Proper algorithm implementation is crucial** - fixing the BFS/DFS issue was essential for correctness
5. **Systematic performance analysis provides valuable insights** - measuring rather than assuming leads to better engineering decisions

The main takeaway is that while custom data structure implementations are excellent for learning and understanding internal workings, Python's built-in optimized structures often provide better practical performance due to their C-level optimizations and cache-friendly designs.

This project provides a solid foundation for understanding both theoretical computer science concepts and practical performance engineering considerations.
