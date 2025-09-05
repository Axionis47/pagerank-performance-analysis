"""
Setup script for PageRank Performance Analysis Project
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pagerank-performance-analysis",
    version="1.0.0",
    author="DSA Project Team",
    description="Performance analysis of PageRank algorithm using different data structures",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pagerank-performance-analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.6",
    install_requires=[
        # No external dependencies - uses only Python standard library
    ],
    extras_require={
        "dev": [
            "flake8>=3.8.0",
            "black>=20.8b1",
            "mypy>=0.800",
        ],
    },
    entry_points={
        "console_scripts": [
            "pagerank-analysis=main:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
