# PageRank Performance Analysis Project

## Overview
This project implements and analyzes the PageRank algorithm using different data structures to compare their performance characteristics. It's based on the original `DSA_Project.ipynb` implementation but with significant improvements and fixes.

## Key Features
- **Multiple Data Structure Implementations**: LinkedList, Array, Dictionary, Sparse representations
- **Corrected PageRank Algorithm**: Fixed the original BFS/DFS-based implementation
- **Comprehensive Performance Analysis**: Time, memory, and convergence comparisons
- **Multiple Graph Types**: Random, scale-free, chain, star, and complete graphs
- **Professional Code Structure**: Modular design with separate files for different components

## Project Structure
```
├── main.py                 # Main entry point with interactive menu
├── data_structures.py      # Custom data structure implementations
├── pagerank_algorithms.py  # PageRank algorithm variants
├── graph_generators.py     # Graph creation utilities
├── performance_analyzer.py # Performance analysis and benchmarking
├── README.md              # This file
└── DSA_Project.ipynb      # Original notebook (preserved)
```

## What Was Fixed from Original
The original implementation had several issues that were corrected:

1. **Algorithm Correctness**: The original used BFS/DFS traversal which doesn't implement PageRank correctly. Fixed to use proper iterative rank distribution.

2. **Code Organization**: Moved from single notebook to modular Python files.

3. **Performance Analysis**: Added comprehensive benchmarking and comparison tools.

4. **Data Structure Variety**: Implemented multiple graph representations for comparison.

## Data Structures Implemented

### Graph Representations
- **LinkedList Graph**: Original adjacency list with custom linked list nodes
- **Array Graph**: Adjacency matrix using 2D arrays
- **Dictionary Graph**: Python dictionary-based adjacency list
- **Sparse Graph**: Edge list representation for sparse graphs

### PageRank Storage
- **HashTable**: Custom hash table implementation (from original)
- **Array**: Simple Python list
- **Dictionary**: Python dict
- **Matrix**: 2D array for matrix operations

## Algorithms Implemented

### PageRank Variants
1. **HashTable-based**: Uses custom HashTable (closest to original)
2. **Array-based**: Uses Python lists (most efficient)
3. **Dictionary-based**: Uses Python dictionaries (most readable)
4. **Matrix-based**: Matrix multiplication approach (most mathematical)

All implementations include:
- Proper damping factor handling
- Dangling node treatment
- Convergence detection
- Teleportation probability

## Usage

### Quick Start
```bash
python main.py
```

This will launch an interactive menu with options:
1. Demonstrate Original Implementation (Fixed)
2. Compare Graph Data Structure Representations
3. Run Quick Performance Demo
4. Run Comprehensive Performance Analysis
5. Show Project Information
6. Exit

### Direct Performance Analysis
```bash
python performance_analyzer.py
```

### Example Output
```
=== PAGERANK PERFORMANCE ANALYSIS ===

--- HashTable-based PageRank ---
Execution Time: 0.000123 seconds
Iterations to Converge: 43
Memory Usage (approx): 1024 bytes
Top 5 Ranked Nodes:
  1. Node 9: 0.237389
  2. Node 6: 0.225865
  3. Node 7: 0.221082
  4. Node 8: 0.151093
  5. Node 5: 0.049568
```

## Performance Metrics

The project analyzes:
- **Execution Time**: How long each algorithm takes
- **Memory Usage**: Memory footprint of different implementations
- **Convergence Speed**: Number of iterations to reach convergence
- **Scalability**: Performance on graphs of different sizes

## Graph Types for Testing

1. **Original Graph**: 10-node graph from the original notebook
2. **Random Graphs**: Various sizes with different edge probabilities
3. **Scale-Free Networks**: Preferential attachment graphs
4. **Chain Graphs**: Linear connectivity
5. **Star Graphs**: Central hub connectivity
6. **Complete Graphs**: All-to-all connectivity

## Key Improvements Made

### Algorithm Correctness
- Fixed PageRank to use proper rank distribution instead of graph traversal
- Added proper handling of dangling nodes
- Implemented correct teleportation probability

### Performance Analysis
- Multiple runs with statistical analysis
- Memory usage tracking
- Convergence analysis
- Scalability testing

### Code Quality
- Modular design with clear separation of concerns
- Comprehensive error handling
- Detailed documentation
- Professional code structure

## Educational Value

This project demonstrates:
- **Data Structure Impact**: How different data structures affect algorithm performance
- **Algorithm Implementation**: Correct implementation of a famous algorithm
- **Performance Analysis**: Systematic benchmarking and comparison
- **Software Engineering**: Professional code organization and documentation

## Requirements
- Python 3.6+
- No external dependencies (uses only standard library)

## Future Enhancements
- Visualization of graphs and algorithm convergence
- More graph algorithms (shortest path, centrality measures)
- Parallel implementations
- Real-world dataset integration
- Web interface for interactive analysis

## Academic Context
This project is suitable for:
- Data Structures and Algorithms courses
- Algorithm analysis assignments
- Performance comparison studies
- Software engineering best practices demonstration

## License
Educational use - based on original DSA course project.
