# Contributing to PageRank Performance Analysis Project

Thank you for your interest in contributing to this project! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/pagerank-performance-analysis.git`
3. Create a new branch: `git checkout -b feature-name`
4. Make your changes
5. Run tests: `python test_pagerank.py`
6. Commit your changes: `git commit -m "Description of changes"`
7. Push to your fork: `git push origin feature-name`
8. Create a Pull Request

## Development Setup

This project uses only Python standard library, so no additional dependencies are required for core functionality.

```bash
# Clone the repository
git clone https://github.com/Axionis47/pagerank-performance-analysis.git
cd pagerank-performance-analysis

# Run tests to ensure everything works
python test_pagerank.py

# Run the main program
python main.py
```

## Code Style

- Follow PEP 8 Python style guidelines
- Use descriptive variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and modular
- Add comments for complex algorithms

## Testing

- All new features should include unit tests
- Run the existing test suite before submitting changes
- Ensure all tests pass: `python test_pagerank.py`
- Add tests for edge cases and error conditions

## Types of Contributions

### Bug Reports
- Use the GitHub issue tracker
- Include steps to reproduce the bug
- Provide expected vs actual behavior
- Include Python version and OS information

### Feature Requests
- Use the GitHub issue tracker
- Describe the feature and its use case
- Explain how it fits with the project goals

### Code Contributions
- Data structure implementations
- Algorithm optimizations
- Performance improvements
- Additional graph generators
- Visualization features
- Documentation improvements

## Project Structure

```
├── main.py                 # Main entry point
├── data_structures.py      # Graph data structure implementations
├── pagerank_algorithms.py  # PageRank algorithm variants
├── graph_generators.py     # Graph creation utilities
├── performance_analyzer.py # Benchmarking and analysis tools
├── test_pagerank.py       # Unit tests
└── README.md              # Project documentation
```

## Coding Guidelines

### Adding New Data Structures
- Implement the same interface as existing graph classes
- Add corresponding tests in `test_pagerank.py`
- Update documentation

### Adding New Algorithms
- Follow the same signature pattern as existing algorithms
- Return `(ranks, iterations)` tuple
- Handle edge cases (empty graphs, single nodes, etc.)
- Add performance benchmarks

### Performance Considerations
- This project focuses on algorithmic performance comparison
- Maintain the educational value of implementations
- Document time and space complexity
- Avoid external dependencies when possible

## Documentation

- Update README.md for significant changes
- Add docstrings to new functions
- Include examples in docstrings
- Update comments for algorithm modifications

## Review Process

1. All contributions will be reviewed by maintainers
2. Tests must pass
3. Code must follow project style guidelines
4. Documentation must be updated for significant changes
5. Performance impact should be considered

## Questions?

Feel free to open an issue for questions about contributing or the project in general.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
