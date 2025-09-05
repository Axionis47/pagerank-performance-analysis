"""
PageRank Algorithm Implementations using Different Data Structures
Fixed and optimized versions based on the original implementation
"""

import time
import sys
from data_structures import HashTable


def pagerank_hashtable(graph, damping=0.85, max_iter=100, tol=1e-6):
    """
    Corrected PageRank implementation using HashTable.
    This fixes the algorithmic issues in the original BFS/DFS versions.
    """
    num_nodes = graph.num_nodes
    ranks = HashTable(size=num_nodes)
    
    # Initialize ranks for each node to 1 / num_nodes
    for node in range(num_nodes):
        ranks.set(node, 1.0 / num_nodes)

    teleport_prob = (1 - damping) / num_nodes
    
    for iteration in range(max_iter):
        new_ranks = HashTable(size=num_nodes)
        
        # Initialize with teleportation probability
        for node in range(num_nodes):
            new_ranks.set(node, teleport_prob)
        
        # Distribute rank from each node to its neighbors
        for node in range(num_nodes):
            neighbors = graph.get_neighbors(node)
            out_degree = len(neighbors)
            
            if out_degree > 0:
                rank_contribution = damping * ranks.get(node) / out_degree
                for neighbor in neighbors:
                    current_rank = new_ranks.get(neighbor)
                    new_ranks.set(neighbor, current_rank + rank_contribution)
            else:
                # Handle dangling nodes (no outgoing edges)
                dangling_contribution = damping * ranks.get(node) / num_nodes
                for n in range(num_nodes):
                    current_rank = new_ranks.get(n)
                    new_ranks.set(n, current_rank + dangling_contribution)
        
        # Check for convergence
        diff = sum(abs(new_ranks.get(node) - ranks.get(node)) for node in range(num_nodes))
        
        if diff < tol:
            return new_ranks, iteration + 1
        
        ranks = new_ranks
    
    return ranks, max_iter


def pagerank_array(graph, damping=0.85, max_iter=100, tol=1e-6):
    """
    PageRank implementation using simple arrays.
    """
    num_nodes = graph.num_nodes
    ranks = [1.0 / num_nodes for _ in range(num_nodes)]
    
    teleport_prob = (1 - damping) / num_nodes
    
    for iteration in range(max_iter):
        new_ranks = [teleport_prob for _ in range(num_nodes)]
        
        # Distribute rank from each node to its neighbors
        for node in range(num_nodes):
            neighbors = graph.get_neighbors(node)
            out_degree = len(neighbors)
            
            if out_degree > 0:
                rank_contribution = damping * ranks[node] / out_degree
                for neighbor in neighbors:
                    new_ranks[neighbor] += rank_contribution
            else:
                # Handle dangling nodes
                dangling_contribution = damping * ranks[node] / num_nodes
                for n in range(num_nodes):
                    new_ranks[n] += dangling_contribution
        
        # Check for convergence
        diff = sum(abs(new_ranks[i] - ranks[i]) for i in range(num_nodes))
        
        if diff < tol:
            return new_ranks, iteration + 1
        
        ranks = new_ranks
    
    return ranks, max_iter


def pagerank_dict(graph, damping=0.85, max_iter=100, tol=1e-6):
    """
    PageRank implementation using Python dictionaries.
    """
    num_nodes = graph.num_nodes
    ranks = {i: 1.0 / num_nodes for i in range(num_nodes)}
    
    teleport_prob = (1 - damping) / num_nodes
    
    for iteration in range(max_iter):
        new_ranks = {i: teleport_prob for i in range(num_nodes)}
        
        # Distribute rank from each node to its neighbors
        for node in range(num_nodes):
            neighbors = graph.get_neighbors(node)
            out_degree = len(neighbors)
            
            if out_degree > 0:
                rank_contribution = damping * ranks[node] / out_degree
                for neighbor in neighbors:
                    new_ranks[neighbor] += rank_contribution
            else:
                # Handle dangling nodes
                dangling_contribution = damping * ranks[node] / num_nodes
                for n in range(num_nodes):
                    new_ranks[n] += dangling_contribution
        
        # Check for convergence
        diff = sum(abs(new_ranks[i] - ranks[i]) for i in range(num_nodes))
        
        if diff < tol:
            return new_ranks, iteration + 1
        
        ranks = new_ranks
    
    return ranks, max_iter


def pagerank_matrix(graph, damping=0.85, max_iter=100, tol=1e-6):
    """
    PageRank implementation using matrix operations (simulated with lists).
    """
    num_nodes = graph.num_nodes
    
    # Build transition matrix
    transition_matrix = [[0.0 for _ in range(num_nodes)] for _ in range(num_nodes)]
    
    for node in range(num_nodes):
        neighbors = graph.get_neighbors(node)
        out_degree = len(neighbors)
        
        if out_degree > 0:
            for neighbor in neighbors:
                transition_matrix[neighbor][node] = 1.0 / out_degree
        else:
            # Dangling node - distribute equally to all nodes
            for n in range(num_nodes):
                transition_matrix[n][node] = 1.0 / num_nodes
    
    # Initialize ranks
    ranks = [1.0 / num_nodes for _ in range(num_nodes)]
    teleport_prob = (1 - damping) / num_nodes
    
    for iteration in range(max_iter):
        new_ranks = [teleport_prob for _ in range(num_nodes)]
        
        # Matrix-vector multiplication: new_ranks = damping * M * ranks + teleport
        for i in range(num_nodes):
            for j in range(num_nodes):
                new_ranks[i] += damping * transition_matrix[i][j] * ranks[j]
        
        # Check for convergence
        diff = sum(abs(new_ranks[i] - ranks[i]) for i in range(num_nodes))
        
        if diff < tol:
            return new_ranks, iteration + 1
        
        ranks = new_ranks
    
    return ranks, max_iter


def measure_performance(pagerank_func, graph, algorithm_name):
    """
    Measure the performance of a PageRank algorithm.
    """
    print(f"\n--- {algorithm_name} ---")
    
    # Measure memory usage before
    initial_memory = sys.getsizeof(graph)
    
    # Measure execution time
    start_time = time.time()
    ranks, iterations = pagerank_func(graph)
    end_time = time.time()
    
    execution_time = end_time - start_time
    
    # Calculate final memory usage (approximate)
    final_memory = sys.getsizeof(ranks) + initial_memory
    
    print(f"Execution Time: {execution_time:.6f} seconds")
    print(f"Iterations to Converge: {iterations}")
    print(f"Memory Usage (approx): {final_memory} bytes")
    
    # Display top 5 ranked nodes
    if isinstance(ranks, dict):
        sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
    elif hasattr(ranks, 'items'):  # HashTable
        sorted_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
    else:  # Array
        sorted_ranks = sorted(enumerate(ranks), key=lambda x: x[1], reverse=True)
    
    print("Top 5 Ranked Nodes:")
    for i, (node, rank) in enumerate(sorted_ranks[:5]):
        print(f"  {i+1}. Node {node}: {rank:.6f}")
    
    return {
        'execution_time': execution_time,
        'iterations': iterations,
        'memory_usage': final_memory,
        'ranks': ranks
    }
