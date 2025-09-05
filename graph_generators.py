"""
Graph Generation Utilities for Performance Testing
Creates graphs of different sizes and structures for benchmarking
"""

import random


def create_original_graph(graph_class):
    """
    Create the original 10-node graph from the notebook.
    """
    graph = graph_class(10)
    
    # Add edges exactly as in the original
    edges = [
        (0, 1), (0, 3), (1, 2), (1, 4), (2, 5),
        (3, 4), (3, 6), (4, 5), (4, 7), (5, 8),
        (6, 7), (7, 8), (7, 9), (8, 9), (9, 6)
    ]
    
    for from_node, to_node in edges:
        graph.add_edge(from_node, to_node)
    
    return graph


def create_random_graph(graph_class, num_nodes, edge_probability=0.1, seed=42):
    """
    Create a random directed graph with given number of nodes.
    
    Args:
        graph_class: The graph class to instantiate
        num_nodes: Number of nodes in the graph
        edge_probability: Probability of edge between any two nodes
        seed: Random seed for reproducibility
    """
    random.seed(seed)
    graph = graph_class(num_nodes)
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j and random.random() < edge_probability:
                graph.add_edge(i, j)
    
    return graph


def create_scale_free_graph(graph_class, num_nodes, m=2, seed=42):
    """
    Create a scale-free graph using preferential attachment (simplified Barabási-Albert).
    
    Args:
        graph_class: The graph class to instantiate
        num_nodes: Number of nodes in the graph
        m: Number of edges to attach from a new node to existing nodes
        seed: Random seed for reproducibility
    """
    random.seed(seed)
    graph = graph_class(num_nodes)
    
    if num_nodes < m + 1:
        # For small graphs, create a complete graph
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    graph.add_edge(i, j)
        return graph
    
    # Start with a small complete graph
    for i in range(m + 1):
        for j in range(m + 1):
            if i != j:
                graph.add_edge(i, j)
    
    # Add remaining nodes with preferential attachment
    degrees = [m for _ in range(m + 1)]  # Track out-degrees
    
    for new_node in range(m + 1, num_nodes):
        # Calculate probabilities based on current degrees
        total_degree = sum(degrees)
        if total_degree == 0:
            probabilities = [1.0 / len(degrees) for _ in degrees]
        else:
            probabilities = [deg / total_degree for deg in degrees]
        
        # Select m nodes to connect to (with replacement allowed)
        targets = []
        for _ in range(m):
            # Weighted random selection
            r = random.random()
            cumulative = 0
            for i, prob in enumerate(probabilities):
                cumulative += prob
                if r <= cumulative:
                    targets.append(i)
                    break
        
        # Add edges from new node to selected targets
        degrees.append(0)
        for target in targets:
            graph.add_edge(new_node, target)
            degrees[new_node] += 1
    
    return graph


def create_chain_graph(graph_class, num_nodes):
    """
    Create a simple chain graph: 0 -> 1 -> 2 -> ... -> n-1 -> 0
    """
    graph = graph_class(num_nodes)
    
    for i in range(num_nodes):
        next_node = (i + 1) % num_nodes
        graph.add_edge(i, next_node)
    
    return graph


def create_star_graph(graph_class, num_nodes):
    """
    Create a star graph: center node (0) connects to all others, others connect back.
    """
    graph = graph_class(num_nodes)
    
    # Center node (0) connects to all others
    for i in range(1, num_nodes):
        graph.add_edge(0, i)
        graph.add_edge(i, 0)  # Make it bidirectional
    
    return graph


def create_complete_graph(graph_class, num_nodes):
    """
    Create a complete directed graph where every node connects to every other node.
    """
    graph = graph_class(num_nodes)
    
    for i in range(num_nodes):
        for j in range(num_nodes):
            if i != j:
                graph.add_edge(i, j)
    
    return graph


def get_graph_statistics(graph):
    """
    Calculate basic statistics about a graph.
    """
    num_nodes = graph.num_nodes
    total_edges = 0
    total_out_degree = 0
    max_out_degree = 0
    min_out_degree = float('inf')
    
    for node in range(num_nodes):
        out_degree = graph.get_out_degree(node)
        total_out_degree += out_degree
        total_edges += out_degree
        max_out_degree = max(max_out_degree, out_degree)
        min_out_degree = min(min_out_degree, out_degree)
    
    if min_out_degree == float('inf'):
        min_out_degree = 0
    
    avg_out_degree = total_out_degree / num_nodes if num_nodes > 0 else 0
    density = total_edges / (num_nodes * (num_nodes - 1)) if num_nodes > 1 else 0
    
    return {
        'num_nodes': num_nodes,
        'num_edges': total_edges,
        'avg_out_degree': avg_out_degree,
        'max_out_degree': max_out_degree,
        'min_out_degree': min_out_degree,
        'density': density
    }


def print_graph_info(graph, graph_name):
    """
    Print information about a graph.
    """
    stats = get_graph_statistics(graph)
    print(f"\n{graph_name} Statistics:")
    print(f"  Nodes: {stats['num_nodes']}")
    print(f"  Edges: {stats['num_edges']}")
    print(f"  Average Out-Degree: {stats['avg_out_degree']:.2f}")
    print(f"  Max Out-Degree: {stats['max_out_degree']}")
    print(f"  Min Out-Degree: {stats['min_out_degree']}")
    print(f"  Density: {stats['density']:.4f}")


# Test graph configurations for performance analysis
TEST_CONFIGURATIONS = [
    {"name": "Original (10 nodes)", "generator": create_original_graph, "size": 10},
    {"name": "Small Random (50 nodes)", "generator": lambda gc: create_random_graph(gc, 50, 0.1), "size": 50},
    {"name": "Medium Random (200 nodes)", "generator": lambda gc: create_random_graph(gc, 200, 0.05), "size": 200},
    {"name": "Large Random (500 nodes)", "generator": lambda gc: create_random_graph(gc, 500, 0.02), "size": 500},
    {"name": "Chain (100 nodes)", "generator": lambda gc: create_chain_graph(gc, 100), "size": 100},
    {"name": "Star (100 nodes)", "generator": lambda gc: create_star_graph(gc, 100), "size": 100},
    {"name": "Scale-Free (100 nodes)", "generator": lambda gc: create_scale_free_graph(gc, 100, 3), "size": 100},
]
