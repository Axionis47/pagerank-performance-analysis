"""
Unit Tests for PageRank Performance Analysis Project
Tests all major components for correctness and robustness
"""

import unittest
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_structures import Graph, ArrayGraph, DictGraph, SparseGraph, HashTable
from pagerank_algorithms import pagerank_array, pagerank_dict, pagerank_hashtable, pagerank_matrix
from graph_generators import create_original_graph, create_random_graph, create_chain_graph


class TestDataStructures(unittest.TestCase):
    """Test custom data structure implementations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.num_nodes = 5
        
    def test_graph_creation(self):
        """Test graph creation and basic operations."""
        graph = Graph(self.num_nodes)
        self.assertEqual(graph.num_nodes, self.num_nodes)
        
        # Test adding edges
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        
        neighbors = graph.get_neighbors(0)
        self.assertIn(1, neighbors)
        self.assertIn(2, neighbors)
        self.assertEqual(len(neighbors), 2)
        
    def test_array_graph(self):
        """Test array-based graph implementation."""
        graph = ArrayGraph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        
        self.assertEqual(graph.get_neighbors(0), [1])
        self.assertEqual(graph.get_neighbors(1), [2])
        self.assertEqual(graph.get_neighbors(2), [])
        
    def test_dict_graph(self):
        """Test dictionary-based graph implementation."""
        graph = DictGraph(3)
        graph.add_edge(0, 1)
        graph.add_edge(0, 2)
        
        neighbors = graph.get_neighbors(0)
        self.assertIn(1, neighbors)
        self.assertIn(2, neighbors)
        
    def test_sparse_graph(self):
        """Test sparse graph implementation."""
        graph = SparseGraph(3)
        graph.add_edge(0, 1)
        graph.add_edge(1, 2)
        
        self.assertEqual(graph.get_neighbors(0), [1])
        self.assertEqual(graph.get_neighbors(1), [2])
        
    def test_hashtable(self):
        """Test custom HashTable implementation."""
        ht = HashTable(10)
        
        # Test basic operations
        ht.set("key1", "value1")
        ht.set("key2", "value2")
        
        self.assertEqual(ht.get("key1"), "value1")
        self.assertEqual(ht.get("key2"), "value2")
        
        # Test key existence
        self.assertIn("key1", ht)
        self.assertNotIn("key3", ht)
        
        # Test key error
        with self.assertRaises(KeyError):
            ht.get("nonexistent")


class TestPageRankAlgorithms(unittest.TestCase):
    """Test PageRank algorithm implementations."""
    
    def setUp(self):
        """Set up test graphs."""
        # Simple 3-node chain: 0 -> 1 -> 2 -> 0
        self.simple_graph = Graph(3)
        self.simple_graph.add_edge(0, 1)
        self.simple_graph.add_edge(1, 2)
        self.simple_graph.add_edge(2, 0)
        
        # Original test graph
        self.original_graph = create_original_graph(Graph)
        
    def test_pagerank_convergence(self):
        """Test that all PageRank implementations converge."""
        algorithms = [
            pagerank_array,
            pagerank_dict,
            pagerank_hashtable,
            pagerank_matrix
        ]
        
        for algo in algorithms:
            with self.subTest(algorithm=algo.__name__):
                ranks, iterations = algo(self.simple_graph, max_iter=100)
                self.assertLess(iterations, 100, f"{algo.__name__} should converge")
                
    def test_pagerank_consistency(self):
        """Test that all implementations give same results."""
        # Run all algorithms on the same graph
        array_ranks, _ = pagerank_array(self.simple_graph)
        dict_ranks, _ = pagerank_dict(self.simple_graph)
        matrix_ranks, _ = pagerank_matrix(self.simple_graph)
        
        # Convert to lists for comparison
        if isinstance(dict_ranks, dict):
            dict_ranks = [dict_ranks[i] for i in range(len(dict_ranks))]
        
        # Check that results are approximately equal
        for i in range(len(array_ranks)):
            self.assertAlmostEqual(array_ranks[i], dict_ranks[i], places=5)
            self.assertAlmostEqual(array_ranks[i], matrix_ranks[i], places=5)
            
    def test_pagerank_properties(self):
        """Test mathematical properties of PageRank."""
        ranks, _ = pagerank_array(self.simple_graph)
        
        # Sum of ranks should be approximately 1
        total_rank = sum(ranks)
        self.assertAlmostEqual(total_rank, 1.0, places=5)
        
        # All ranks should be positive
        for rank in ranks:
            self.assertGreater(rank, 0)
            
    def test_single_node_graph(self):
        """Test PageRank on single node graph."""
        single_graph = Graph(1)
        ranks, iterations = pagerank_array(single_graph)
        
        self.assertEqual(len(ranks), 1)
        self.assertAlmostEqual(ranks[0], 1.0, places=5)
        
    def test_disconnected_graph(self):
        """Test PageRank on disconnected graph."""
        disconnected = Graph(4)
        disconnected.add_edge(0, 1)
        disconnected.add_edge(2, 3)
        # Nodes 1 and 3 have no outgoing edges
        
        ranks, _ = pagerank_array(disconnected)
        
        # Should still converge and sum to 1
        self.assertAlmostEqual(sum(ranks), 1.0, places=5)
        self.assertEqual(len(ranks), 4)


class TestGraphGenerators(unittest.TestCase):
    """Test graph generation utilities."""
    
    def test_original_graph(self):
        """Test original graph creation."""
        graph = create_original_graph(Graph)
        self.assertEqual(graph.num_nodes, 10)
        
        # Test that it has the expected structure
        neighbors_0 = graph.get_neighbors(0)
        self.assertIn(1, neighbors_0)
        self.assertIn(3, neighbors_0)
        
    def test_random_graph(self):
        """Test random graph generation."""
        graph = create_random_graph(Graph, 10, edge_probability=0.5, seed=42)
        self.assertEqual(graph.num_nodes, 10)
        
        # With seed=42, should be reproducible
        graph2 = create_random_graph(Graph, 10, edge_probability=0.5, seed=42)
        
        # Check that graphs are identical
        for i in range(10):
            neighbors1 = set(graph.get_neighbors(i))
            neighbors2 = set(graph2.get_neighbors(i))
            self.assertEqual(neighbors1, neighbors2)
            
    def test_chain_graph(self):
        """Test chain graph generation."""
        graph = create_chain_graph(Graph, 5)
        self.assertEqual(graph.num_nodes, 5)
        
        # Check chain structure: 0->1->2->3->4->0
        for i in range(5):
            neighbors = graph.get_neighbors(i)
            expected_neighbor = (i + 1) % 5
            self.assertEqual(neighbors, [expected_neighbor])


class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases."""
    
    def test_invalid_graph_size(self):
        """Test handling of invalid graph sizes."""
        # Zero nodes should work but be empty
        graph = Graph(0)
        self.assertEqual(graph.num_nodes, 0)
        
    def test_invalid_edge(self):
        """Test adding invalid edges."""
        graph = Graph(3)
        
        # Adding edge to non-existent node should not crash
        # (Implementation dependent - some might allow, others might not)
        try:
            graph.add_edge(0, 5)  # Node 5 doesn't exist
        except (IndexError, ValueError):
            pass  # Expected behavior
            
    def test_empty_graph_pagerank(self):
        """Test PageRank on empty graph."""
        empty_graph = Graph(0)
        
        # Should handle gracefully
        try:
            ranks, _ = pagerank_array(empty_graph)
            self.assertEqual(len(ranks), 0)
        except (ValueError, ZeroDivisionError):
            pass  # Acceptable to raise error for empty graph


def run_tests():
    """Run all tests and return results."""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    test_classes = [
        TestDataStructures,
        TestPageRankAlgorithms,
        TestGraphGenerators,
        TestErrorHandling
    ]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    print("Running PageRank Project Tests...")
    print("=" * 50)
    
    success = run_tests()
    
    print("\n" + "=" * 50)
    if success:
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED!")
        sys.exit(1)
