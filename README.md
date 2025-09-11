# DSA Project: PageRank Algorithm Performance Analysis

## Project Overview
This is a Data Structures and Algorithms (DSA) project that implements PageRank algorithm using different data structures and compares their performance. 

## Objective
To understand how different data structures affect the performance of PageRank algorithm by implementing and comparing:
- Custom Hash Table vs Python Lists vs Python Dictionaries
- Different graph representations (LinkedList, Array Matrix, Dictionary, Sparse)
- Performance metrics like execution time, memory usage, and convergence behaviour

## Project Structure
```
DSA_Project/
├── main.py                 # Main program with interactive menu
├── data_structures.py      # Custom data structure implementations
├── pagerank_algorithms.py  # PageRank algorithm variants
├── graph_generators.py     # Graph creation utilities
├── performance_analyzer.py # Performance analysis tools
├── test_pagerank.py       # Unit tests for validation
├── README.md              # This documentation
└── DSA_Project.ipynb      # Original notebook (reference)
```

## Problem Statement
The original implementation had algorithmic issues where PageRank was incorrectly implemented using BFS/DFS traversal instead of proper iterative rank distribution. This project fixes those issues and provides comprehensive performance analysis.

## Data Structures Implemented

### Custom Graph Representations
1. **LinkedList Graph**: Adjacency list using custom linked list nodes with manual pointer management
2. **Array Graph**: Adjacency matrix using 2D arrays for direct access
3. **Dictionary Graph**: Python dictionary-based adjacency list for flexibility
4. **Sparse Graph**: Edge list representation for memory efficiency

### PageRank Storage Methods
1. **Custom HashTable**: Our own hash table with collision handling (educational purpose)
2. **Python Arrays**: Built-in lists for comparison
3. **Python Dictionaries**: Built-in dictionaries for comparison
4. **Matrix Operations**: 2D arrays with mathematical approach

## Algorithm Implementation

### Corrected PageRank Algorithm
The original notebook had incorrect implementation using BFS/DFS. We fixed it to use proper iterative rank distribution:

```python
# Correct approach: Distribute rank from each node to its neighbours
for node in range(num_nodes):
    neighbours = graph.get_neighbors(node)
    if len(neighbours) > 0:
        rank_contribution = damping * ranks[node] / len(neighbours)
        for neighbour in neighbours:
            new_ranks[neighbour] += rank_contribution
```

### Features Implemented
- Proper damping factor (0.85)
- Dangling node handling
- Convergence detection (tolerance = 1e-6)
- Teleportation probability calculation

## How to Run the Project

### Method 1: Interactive Menu
```bash
python main.py
```
This will show you a menu with different options:
1. Show corrected implementation results
2. Compare different graph representations
3. Run quick performance demo
4. Run detailed performance analysis
5. Show project information

### Method 2: Run Tests
```bash
python test_pagerank.py
```
This will run all unit tests to verify correctness.

### Method 3: Direct Performance Analysis
```bash
python performance_analyzer.py
```
This will run comprehensive benchmarking.

## Key Findings and Results

### Performance Comparison Results
After running extensive tests on the original 10-node graph, we found significant differences:

#### Execution Time Comparison (Average of 5 runs)
1. **Python Arrays**: 0.097 ms ⚡ (Fastest)
2. **Python Dictionary**: 0.114 ms
3. **Matrix Operations**: 0.176 ms
4. **Custom HashTable**: 0.443 ms 🐌 (Slowest)

**Key Finding**: Python's built-in list is **4.6 times faster** than our custom HashTable!

#### Memory Usage Comparison
1. **Custom HashTable**: 48 bytes (Most memory efficient)
2. **Python Arrays**: 184 bytes
3. **Matrix Operations**: 184 bytes
4. **Python Dictionary**: 352 bytes (Uses most memory)

**Surprising Discovery**: HashTable uses least memory but is slowest in execution!

#### Graph Representation Performance
1. **Dictionary Graph**: 0.089 ms (Fastest)
2. **Sparse Graph**: 0.089 ms (Tied for fastest)
3. **LinkedList Graph**: 0.129 ms
4. **Array Matrix Graph**: 0.168 ms (Slowest)

### Scalability Analysis
When we tested with different graph sizes, the performance gap increased:
- **10 nodes**: Array 4.4x faster than HashTable
- **50 nodes**: Array 4.2x faster than HashTable
- **100 nodes**: Array 6.2x faster than HashTable

**Learning**: Custom implementations don't always scale as well as optimized built-ins.

### Convergence Behaviour
All algorithms converged to identical results in exactly **43 iterations**, proving our implementation correctness.

**Top 5 PageRank Results** (for original 10-node graph):
1. Node 9: 0.237389 (Highest importance)
2. Node 6: 0.225865
3. Node 7: 0.221082
4. Node 8: 0.151093
5. Node 5: 0.049568

## Important Learnings

### What We Discovered
1. **Custom vs Built-in**: Sometimes Python's optimized built-ins perform better than custom implementations
2. **Memory vs Speed**: Less memory usage doesn't always mean faster execution
3. **Implementation Overhead**: Custom data structures have overhead costs
4. **Cache Performance**: Array access is more cache-friendly than hash table lookups
5. **Algorithm Correctness**: Proper mathematical implementation is crucial

### Why These Differences Occur
- **Python Lists**: Optimized C implementation, cache-friendly memory layout
- **Custom HashTable**: Hash function overhead, collision handling, multiple memory jumps
- **Python Dictionary**: Highly optimized hash table implementation in C
- **Matrix Operations**: Simple but requires more memory for large graphs

## Technical Implementation Details

### Custom Data Structures Built
1. **LinkedListNode**: Manual pointer management for graph edges
2. **HashTable**: Custom hash function with collision handling using chaining
3. **Graph Classes**: Four different graph representations from scratch
4. **No External Libraries**: Used only Python standard library

### Algorithm Complexity Analysis
| Method | Time Complexity | Space Complexity | Practical Performance |
|--------|----------------|------------------|---------------------|
| Custom HashTable | O(1) average | O(n) | Slowest (hash overhead) |
| Python Arrays | O(1) access | O(n) | Fastest (cache-friendly) |
| Python Dictionary | O(1) average | O(n) | Good (optimized) |
| Matrix Operations | O(1) access | O(n²) | Moderate (space overhead) |

## Project Validation

### Testing Results
- **16 unit tests** implemented and all passing ✅
- **Algorithm correctness** verified against mathematical properties
- **Edge cases** handled (empty graphs, single nodes, disconnected components)
- **Reproducible results** with consistent random seeds

### Code Quality
- **Modular design** with clear separation of concerns
- **Comprehensive documentation** with inline comments
- **Error handling** for invalid inputs
- **Professional structure** suitable for academic submission

## Conclusion

This project successfully demonstrates:
1. **Implementation Skills**: Built complex data structures from scratch
2. **Performance Analysis**: Systematic comparison of different approaches
3. **Algorithm Understanding**: Corrected and optimized PageRank implementation
4. **Engineering Insights**: When to use custom vs built-in implementations

**Main Takeaway**: While custom implementations are educational and give us control, Python's built-in optimized data structures often perform better in practice due to their C-level optimizations and cache-friendly designs.

## Requirements
- Python 3.6 or higher
- No external dependencies required
- All implementations use only Python standard library

## Author
DSA Course Project - Performance Analysis of PageRank Algorithm using Different Data Structures
