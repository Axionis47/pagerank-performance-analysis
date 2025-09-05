"""
Performance Analysis and Comparison Tool
Runs comprehensive benchmarks and generates detailed reports
"""

import time
import sys
import statistics
from data_structures import Graph, ArrayGraph, DictGraph, SparseGraph
from pagerank_algorithms import (
    pagerank_hashtable, pagerank_array, pagerank_dict, pagerank_matrix,
    measure_performance
)
from graph_generators import TEST_CONFIGURATIONS, print_graph_info


class PerformanceAnalyzer:
    """
    Comprehensive performance analysis tool for PageRank implementations.
    """
    
    def __init__(self):
        self.results = {}
        self.graph_classes = {
            'LinkedList': Graph,
            'Array': ArrayGraph,
            'Dictionary': DictGraph,
            'Sparse': SparseGraph
        }
        self.algorithms = {
            'HashTable': pagerank_hashtable,
            'Array': pagerank_array,
            'Dictionary': pagerank_dict,
            'Matrix': pagerank_matrix
        }
    
    def run_single_test(self, graph, algorithm_name, algorithm_func, runs=3):
        """
        Run a single performance test multiple times and return average results.
        """
        execution_times = []
        iterations_list = []
        memory_usages = []
        
        for run in range(runs):
            start_time = time.time()
            ranks, iterations = algorithm_func(graph)
            end_time = time.time()
            
            execution_time = end_time - start_time
            memory_usage = sys.getsizeof(ranks) + sys.getsizeof(graph)
            
            execution_times.append(execution_time)
            iterations_list.append(iterations)
            memory_usages.append(memory_usage)
        
        return {
            'avg_execution_time': statistics.mean(execution_times),
            'std_execution_time': statistics.stdev(execution_times) if len(execution_times) > 1 else 0,
            'avg_iterations': statistics.mean(iterations_list),
            'avg_memory_usage': statistics.mean(memory_usages),
            'all_execution_times': execution_times
        }
    
    def run_comprehensive_analysis(self, test_configs=None, runs_per_test=3):
        """
        Run comprehensive performance analysis across all combinations.
        """
        if test_configs is None:
            test_configs = TEST_CONFIGURATIONS[:4]  # Use first 4 to avoid too long execution
        
        print("=" * 80)
        print("COMPREHENSIVE PAGERANK PERFORMANCE ANALYSIS")
        print("=" * 80)
        
        for config in test_configs:
            graph_name = config['name']
            graph_generator = config['generator']
            
            print(f"\n{'='*60}")
            print(f"TESTING: {graph_name}")
            print(f"{'='*60}")
            
            # Test each graph representation
            for graph_type, graph_class in self.graph_classes.items():
                print(f"\n--- Graph Representation: {graph_type} ---")
                
                try:
                    # Create graph
                    graph = graph_generator(graph_class)
                    print_graph_info(graph, f"{graph_name} ({graph_type})")
                    
                    # Test each algorithm
                    graph_results = {}
                    for algo_name, algo_func in self.algorithms.items():
                        print(f"\nTesting {algo_name} algorithm...")
                        try:
                            result = self.run_single_test(graph, algo_name, algo_func, runs_per_test)
                            graph_results[algo_name] = result
                            
                            print(f"  Avg Execution Time: {result['avg_execution_time']:.6f} ± {result['std_execution_time']:.6f} seconds")
                            print(f"  Avg Iterations: {result['avg_iterations']:.1f}")
                            print(f"  Avg Memory Usage: {result['avg_memory_usage']:.0f} bytes")
                            
                        except Exception as e:
                            print(f"  ERROR: {str(e)}")
                            graph_results[algo_name] = {'error': str(e)}
                    
                    # Store results
                    key = f"{graph_name}_{graph_type}"
                    self.results[key] = graph_results
                    
                except Exception as e:
                    print(f"ERROR creating {graph_type} graph: {str(e)}")
        
        self.generate_summary_report()
    
    def generate_summary_report(self):
        """
        Generate a comprehensive summary report of all results.
        """
        print(f"\n{'='*80}")
        print("PERFORMANCE SUMMARY REPORT")
        print(f"{'='*80}")
        
        # Collect all successful results
        successful_results = {}
        for test_key, algorithms in self.results.items():
            successful_results[test_key] = {}
            for algo_name, result in algorithms.items():
                if 'error' not in result:
                    successful_results[test_key][algo_name] = result
        
        if not successful_results:
            print("No successful test results to analyze.")
            return
        
        # Find fastest algorithm for each test
        print("\n--- FASTEST ALGORITHM BY TEST ---")
        for test_key, algorithms in successful_results.items():
            if algorithms:
                fastest = min(algorithms.items(), key=lambda x: x[1]['avg_execution_time'])
                print(f"{test_key:30} | {fastest[0]:12} | {fastest[1]['avg_execution_time']:.6f}s")
        
        # Overall algorithm performance ranking
        print("\n--- OVERALL ALGORITHM PERFORMANCE RANKING ---")
        algo_performance = {}
        for test_key, algorithms in successful_results.items():
            for algo_name, result in algorithms.items():
                if algo_name not in algo_performance:
                    algo_performance[algo_name] = []
                algo_performance[algo_name].append(result['avg_execution_time'])
        
        # Calculate average performance for each algorithm
        algo_averages = {}
        for algo_name, times in algo_performance.items():
            algo_averages[algo_name] = statistics.mean(times)
        
        # Sort by average performance
        sorted_algos = sorted(algo_averages.items(), key=lambda x: x[1])
        
        print(f"{'Rank':<4} | {'Algorithm':<12} | {'Avg Time (s)':<12} | {'Tests':<6}")
        print("-" * 50)
        for rank, (algo_name, avg_time) in enumerate(sorted_algos, 1):
            test_count = len(algo_performance[algo_name])
            print(f"{rank:<4} | {algo_name:<12} | {avg_time:.6f}     | {test_count:<6}")
        
        # Memory usage analysis
        print("\n--- MEMORY USAGE ANALYSIS ---")
        print(f"{'Test':<30} | {'Algorithm':<12} | {'Memory (bytes)':<15}")
        print("-" * 60)
        for test_key, algorithms in successful_results.items():
            for algo_name, result in algorithms.items():
                memory = result['avg_memory_usage']
                print(f"{test_key:<30} | {algo_name:<12} | {memory:<15.0f}")
        
        # Convergence analysis
        print("\n--- CONVERGENCE ANALYSIS ---")
        print(f"{'Test':<30} | {'Algorithm':<12} | {'Avg Iterations':<15}")
        print("-" * 60)
        for test_key, algorithms in successful_results.items():
            for algo_name, result in algorithms.items():
                iterations = result['avg_iterations']
                print(f"{test_key:<30} | {algo_name:<12} | {iterations:<15.1f}")
    
    def run_quick_demo(self):
        """
        Run a quick demonstration with the original graph.
        """
        print("=" * 60)
        print("QUICK PAGERANK PERFORMANCE DEMO")
        print("=" * 60)
        
        # Use original graph configuration
        original_config = TEST_CONFIGURATIONS[0]
        graph_generator = original_config['generator']
        
        print(f"\nTesting with: {original_config['name']}")
        
        # Test with LinkedList graph (original implementation)
        graph = graph_generator(Graph)
        print_graph_info(graph, "Original Graph")
        
        print(f"\n{'Algorithm':<15} | {'Time (s)':<10} | {'Iterations':<12} | {'Memory (bytes)':<15}")
        print("-" * 65)
        
        for algo_name, algo_func in self.algorithms.items():
            try:
                start_time = time.time()
                ranks, iterations = algo_func(graph)
                end_time = time.time()
                
                execution_time = end_time - start_time
                memory_usage = sys.getsizeof(ranks)
                
                print(f"{algo_name:<15} | {execution_time:<10.6f} | {iterations:<12} | {memory_usage:<15}")
                
            except Exception as e:
                print(f"{algo_name:<15} | ERROR: {str(e)}")


def main():
    """
    Main function to run performance analysis.
    """
    analyzer = PerformanceAnalyzer()
    
    print("PageRank Performance Analysis Tool")
    print("Choose an option:")
    print("1. Quick Demo (Original graph only)")
    print("2. Comprehensive Analysis (All configurations)")
    print("3. Custom Analysis (Selected configurations)")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            analyzer.run_quick_demo()
        elif choice == '2':
            print("\nRunning comprehensive analysis...")
            analyzer.run_comprehensive_analysis()
        elif choice == '3':
            print("\nAvailable configurations:")
            for i, config in enumerate(TEST_CONFIGURATIONS):
                print(f"  {i+1}. {config['name']}")
            
            selected = input("\nEnter configuration numbers (comma-separated, e.g., 1,2,3): ").strip()
            indices = [int(x.strip()) - 1 for x in selected.split(',') if x.strip().isdigit()]
            selected_configs = [TEST_CONFIGURATIONS[i] for i in indices if 0 <= i < len(TEST_CONFIGURATIONS)]
            
            if selected_configs:
                analyzer.run_comprehensive_analysis(selected_configs)
            else:
                print("No valid configurations selected.")
        else:
            print("Invalid choice. Running quick demo...")
            analyzer.run_quick_demo()
            
    except KeyboardInterrupt:
        print("\n\nAnalysis interrupted by user.")
    except Exception as e:
        print(f"\nError during analysis: {str(e)}")
        print("Running quick demo instead...")
        analyzer.run_quick_demo()


if __name__ == "__main__":
    main()
