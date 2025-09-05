"""
DSA Project: PageRank Algorithm Performance Analysis
Main program to demonstrate and compare different data structure implementations
Student Project - Data Structures and Algorithms Course
"""

from data_structures import Graph, ArrayGraph, DictGraph, SparseGraph
from pagerank_algorithms import (
    pagerank_hashtable, pagerank_array, pagerank_dict, pagerank_matrix,
    measure_performance
)
from graph_generators import create_original_graph, print_graph_info
from performance_analyzer import PerformanceAnalyzer


def demonstrate_original_implementation():
    """
    Demonstrate the corrected version of the original implementation.
    """
    print("=" * 70)
    print("ORIGINAL IMPLEMENTATION DEMONSTRATION")
    print("=" * 70)
    
    # Create the original graph
    graph = create_original_graph(Graph)
    
    print("\nOriginal Graph Structure:")
    graph.display_graph()
    
    print_graph_info(graph, "Original Graph")
    
    # Run the corrected PageRank algorithm
    print("\n" + "="*50)
    print("CORRECTED PAGERANK RESULTS")
    print("="*50)
    
    # Test with HashTable (closest to original)
    measure_performance(pagerank_hashtable, graph, "HashTable-based PageRank")
    
    print("\n" + "="*50)
    print("COMPARISON WITH OTHER DATA STRUCTURES")
    print("="*50)
    
    # Test with Array implementation
    measure_performance(pagerank_array, graph, "Array-based PageRank")
    
    # Test with Dictionary implementation
    measure_performance(pagerank_dict, graph, "Dictionary-based PageRank")
    
    # Test with Matrix implementation
    measure_performance(pagerank_matrix, graph, "Matrix-based PageRank")


def compare_graph_representations():
    """
    Compare different graph data structure representations.
    """
    print("\n" + "=" * 70)
    print("GRAPH REPRESENTATION COMPARISON")
    print("=" * 70)
    
    graph_types = {
        'LinkedList (Original)': Graph,
        'Adjacency Matrix': ArrayGraph,
        'Dictionary': DictGraph,
        'Sparse Representation': SparseGraph
    }
    
    for name, graph_class in graph_types.items():
        print(f"\n--- {name} ---")
        graph = create_original_graph(graph_class)
        
        # Show structure for small graphs
        if hasattr(graph, 'display_graph'):
            print("Structure:")
            graph.display_graph()
        
        # Run PageRank with array implementation (most compatible)
        try:
            measure_performance(pagerank_array, graph, f"{name} + Array PageRank")
        except Exception as e:
            print(f"Error with {name}: {str(e)}")


def interactive_menu():
    """
    Interactive menu for the user to choose what to run.
    """
    while True:
        print("\n" + "=" * 60)
        print("PAGERANK PERFORMANCE ANALYSIS PROJECT")
        print("=" * 60)
        print("Based on DSA_Project.ipynb with improvements")
        print("\nChoose an option:")
        print("1. Demonstrate Original Implementation (Fixed)")
        print("2. Compare Graph Data Structure Representations")
        print("3. Run Quick Performance Demo")
        print("4. Run Comprehensive Performance Analysis")
        print("5. Show Project Information")
        print("6. Exit")
        
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                demonstrate_original_implementation()
            elif choice == '2':
                compare_graph_representations()
            elif choice == '3':
                analyzer = PerformanceAnalyzer()
                analyzer.run_quick_demo()
            elif choice == '4':
                analyzer = PerformanceAnalyzer()
                analyzer.run_comprehensive_analysis()
            elif choice == '5':
                show_project_info()
            elif choice == '6':
                print("\nThank you for using the PageRank Performance Analysis Project!")
                break
            else:
                print("\nInvalid choice. Please enter a number between 1-6.")
                
        except KeyboardInterrupt:
            print("\n\nExiting...")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")
            print("Please try again.")


def show_project_info():
    """
    Display project information and structure.
    """
    print("\n" + "=" * 70)
    print("DSA PROJECT INFORMATION")
    print("=" * 70)

    print("""
DSA Course Project: PageRank Algorithm Performance Analysis

OBJECTIVE:
To study how different data structures affect the performance of PageRank
algorithm by implementing and comparing various approaches.

PROBLEM SOLVED:
The original notebook had incorrect PageRank implementation using BFS/DFS.
We fixed it to use proper iterative rank distribution method.

PROJECT STRUCTURE:
├── main.py                 # Main program (this file)
├── data_structures.py      # Custom data structure implementations
├── pagerank_algorithms.py  # PageRank algorithm variants
├── graph_generators.py     # Graph creation utilities
├── performance_analyzer.py # Performance analysis tools
├── test_pagerank.py       # Unit tests for validation
└── DSA_Project.ipynb      # Original notebook (reference)

CUSTOM DATA STRUCTURES IMPLEMENTED:
- LinkedList-based Graph with manual pointer management
- Adjacency Matrix Graph using 2D arrays
- Dictionary-based Graph for flexibility
- Sparse Graph for memory efficiency
- Custom HashTable with collision handling

PAGERANK STORAGE METHODS COMPARED:
- Custom HashTable (educational purpose)
- Python Arrays (built-in lists)
- Python Dictionaries (built-in dicts)
- Matrix Operations (2D arrays)

KEY FINDINGS:
- Python Arrays are 4.6x faster than Custom HashTable
- Custom HashTable uses least memory but is slowest
- All methods converge to identical results in 43 iterations
- Built-in optimizations often beat custom implementations

EDUCATIONAL VALUE:
- Understanding data structure implementation from scratch
- Learning performance trade-offs between custom vs built-in
- Proper algorithm implementation and validation
- Systematic performance analysis methodology
    """)


def main():
    """
    Main function - entry point of the program.
    """
    try:
        interactive_menu()
    except Exception as e:
        print(f"Fatal error: {str(e)}")
        print("\nRunning basic demonstration instead...")
        demonstrate_original_implementation()


if __name__ == "__main__":
    main()
