"""
Main Entry Point for PageRank Performance Analysis Project
Based on the original DSA_Project.ipynb implementation
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
    result = measure_performance(pagerank_hashtable, graph, "HashTable-based PageRank")
    
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
            result = measure_performance(pagerank_array, graph, f"{name} + Array PageRank")
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
    print("PROJECT INFORMATION")
    print("=" * 70)
    
    print("""
This project implements and analyzes PageRank algorithm performance using
different data structures, based on the original DSA_Project.ipynb.

KEY IMPROVEMENTS MADE:
1. Fixed the PageRank algorithm (original had BFS/DFS issues)
2. Implemented multiple data structure variants
3. Added comprehensive performance analysis
4. Created modular, professional code structure
5. Added multiple graph types for testing

PROJECT STRUCTURE:
├── main.py                 # Main entry point (this file)
├── data_structures.py      # Custom data structure implementations
├── pagerank_algorithms.py  # PageRank algorithm variants
├── graph_generators.py     # Graph creation utilities
├── performance_analyzer.py # Performance analysis tools
└── DSA_Project.ipynb      # Original notebook (preserved)

DATA STRUCTURES IMPLEMENTED:
- LinkedList-based Graph (original)
- Adjacency Matrix Graph
- Dictionary-based Graph
- Sparse Graph representation
- Custom HashTable
- Custom Queue and Stack (from original)

PAGERANK ALGORITHMS:
- HashTable-based (closest to original)
- Array-based (most efficient)
- Dictionary-based (Python native)
- Matrix-based (mathematical approach)

PERFORMANCE METRICS:
- Execution time
- Memory usage
- Convergence iterations
- Scalability analysis

GRAPH TYPES FOR TESTING:
- Original 10-node graph
- Random graphs (various sizes)
- Scale-free networks
- Chain and star topologies
- Complete graphs
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
