"""
Custom Data Structures for PageRank Implementation
Based on the original DSA_Project.ipynb implementation
"""

class LinkedListNode:
    """Node for linked list to store edges."""
    def __init__(self, value):
        self.value = value
        self.next = None


class Graph:
    """Graph implemented with adjacency list using linked lists."""
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_list = [None for _ in range(num_nodes)]

    def add_edge(self, from_node, to_node):
        """Add a directed edge from 'from_node' to 'to_node'."""
        new_node = LinkedListNode(to_node)
        new_node.next = self.adj_list[from_node]
        self.adj_list[from_node] = new_node

    def get_neighbors(self, node):
        """Get outgoing neighbors of a node."""
        neighbors = []
        current = self.adj_list[node]
        while current:
            neighbors.append(current.value)
            current = current.next
        return neighbors

    def get_out_degree(self, node):
        """Get the out-degree of a node."""
        return len(self.get_neighbors(node))

    def display_graph(self):
        """Display the adjacency list of the graph."""
        for i in range(self.num_nodes):
            print(f"Node {i}:", end=" ")
            current = self.adj_list[i]
            while current:
                print(f"{current.value}", end=" -> ")
                current = current.next
            print("None")


class HashTable:
    """Custom Hash Table implementation to store node ranks."""
    def __init__(self, size=100):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Generate a hash for a given key."""
        return hash(key) % self.size

    def set(self, key, value):
        """Set a key-value pair in the hash table."""
        hashed_key = self._hash(key)
        for i, (k, _) in enumerate(self.table[hashed_key]):
            if k == key:
                self.table[hashed_key][i] = (key, value)
                return
        self.table[hashed_key].append((key, value))

    def get(self, key):
        """Get the value associated with a key in the hash table."""
        hashed_key = self._hash(key)
        for k, v in self.table[hashed_key]:
            if k == key:
                return v
        raise KeyError(f"Key {key} not found in HashTable.")

    def keys(self):
        """Get all the keys in the hash table."""
        return [k for bucket in self.table for k, _ in bucket]

    def items(self):
        """Get all key-value pairs in the hash table."""
        return [(k, v) for bucket in self.table for k, v in bucket]

    def __contains__(self, key):
        """Check if the key exists in the hash table."""
        hashed_key = self._hash(key)
        return any(k == key for k, _ in self.table[hashed_key])


class ArrayGraph:
    """Graph implemented with adjacency matrix using arrays."""
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

    def add_edge(self, from_node, to_node):
        """Add a directed edge from 'from_node' to 'to_node'."""
        self.adj_matrix[from_node][to_node] = 1

    def get_neighbors(self, node):
        """Get outgoing neighbors of a node."""
        neighbors = []
        for i in range(self.num_nodes):
            if self.adj_matrix[node][i] == 1:
                neighbors.append(i)
        return neighbors

    def get_out_degree(self, node):
        """Get the out-degree of a node."""
        return sum(self.adj_matrix[node])

    def display_graph(self):
        """Display the adjacency matrix of the graph."""
        print("Adjacency Matrix:")
        for i in range(self.num_nodes):
            print(f"Node {i}: {self.adj_matrix[i]}")


class DictGraph:
    """Graph implemented with dictionary-based adjacency list."""
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_dict = {i: [] for i in range(num_nodes)}

    def add_edge(self, from_node, to_node):
        """Add a directed edge from 'from_node' to 'to_node'."""
        self.adj_dict[from_node].append(to_node)

    def get_neighbors(self, node):
        """Get outgoing neighbors of a node."""
        return self.adj_dict[node].copy()

    def get_out_degree(self, node):
        """Get the out-degree of a node."""
        return len(self.adj_dict[node])

    def display_graph(self):
        """Display the dictionary-based adjacency list."""
        for node, neighbors in self.adj_dict.items():
            print(f"Node {node}: {neighbors}")


class SparseGraph:
    """Graph implemented with sparse representation (list of edges)."""
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.edges = []
        self.out_neighbors = {i: [] for i in range(num_nodes)}

    def add_edge(self, from_node, to_node):
        """Add a directed edge from 'from_node' to 'to_node'."""
        self.edges.append((from_node, to_node))
        self.out_neighbors[from_node].append(to_node)

    def get_neighbors(self, node):
        """Get outgoing neighbors of a node."""
        return self.out_neighbors[node].copy()

    def get_out_degree(self, node):
        """Get the out-degree of a node."""
        return len(self.out_neighbors[node])

    def display_graph(self):
        """Display the edge list representation."""
        print(f"Edges: {self.edges}")
        print("Adjacency representation:")
        for node, neighbors in self.out_neighbors.items():
            print(f"Node {node}: {neighbors}")
