# Graph Burning Problem

## Problem Description
The graph burning problem is an NP-hard combinatorial optimization problem that quantifies how vulnerable a graph is to contagion. The goal of the problem is to determine the minimum number of nodes needed to initiate a "burning" process in a given graph, such that the burning spreads to all other nodes in the graph. The burning process is defined as follows:
1. Initially, a set of nodes is marked as "burned."
2. At each time step, the burning spreads from the burned nodes to their neighbors.
3. The burning continues until all nodes in the graph are burned.

## Codes Overview
This repository contains four Python scripts to solve the "Graph Burning" problem using different algorithms:

### Code 1 (ILP - Integer Linear Programming)
- Dependencies: ortools, networkx
- Description: This code formulates the Graph Burning problem as an Integer Linear Programming (ILP) model using the Google OR-Tools library. It creates binary variables and constraints to model the burning process and uses SCIP solver to find the optimal solution.

### Code 2 (Brute Force)
- Dependencies: networkx
- Description: This code implements a brute force algorithm to solve the Graph Burning problem. It generates all possible permutations of nodes and simulates the burning process for each permutation to find the minimum burning number.

### Code 3 (Exact Algorithm)
- Dependencies: networkx, simpy, matplotlib
- Description: This code provides an exact algorithm to solve the Graph Burning problem. It generates the configuration graph of the input graph and then performs a breadth-first search (BFS) to find the minimum burning number. Additionally, it uses SimPy library to simulate the burning process and Matplotlib to visualize the burning animation.

### Code 4 (Exact Algorithm from File Input)
- Dependencies: networkx, ast, simpy, matplotlib
- Description: This code is similar to Code 3 but reads the input graph from a file (Tasks.txt). It parses the nodes and edges from the file and then solves the Graph Burning problem using the exact algorithm.

## How to Run the Codes
1. Install the required dependencies for each code using the following commands:
   - For Code 1: `pip install ortools networkx`
   - For Code 2: `pip install networkx`
   - For Code 3: `pip install networkx simpy matplotlib`
   - For Code 4: `pip install networkx ast simpy matplotlib`
   
2. Download the corresponding Python scripts (code1.py, code2.py, code3.py, code4.py) and place them in a local directory.

3. Run each code using the Python interpreter:
   - For Code 1: `python Brute_Force.py`
   - For Code 2: `python Exact_Algorithm_input_from_file.py`
   - For Code 3: `python Exact_Algorithm.py`
   - For Code 4: `python ILP.py`

Note: Code 4 requires the input graph to be present in the Tasks.txt file in the format of node IDs (one node per line) and edges (two nodes per line).

## Example Input (Tasks.txt)
```
1
2
3
4
1 2
2 3
3 4
```
The above input represents a graph with four nodes (1, 2, 3, 4) and three edges (1-2, 2-3, 3-4). The first line (1) indicates the optimal burning number, which is used in Code 4 for comparison.

## Explanation
The provided codes use different algorithms to solve the Graph Burning problem. Code 1 uses Integer Linear Programming, Code 2 uses Brute Force, and Code 3 and Code 4 use Exact Algorithms. Code 4 reads the input graph from a file.

Each code will output the minimum burning number, which represents the minimum number of nodes required to initiate the burning process in the graph. Additionally, Code 3 and Code 4 will generate a visualization of the burning animation to illustrate the burning process in the graph.

Remember to adjust the graph definition in the code (e.g., G = nx.path_graph(20)) or create a Tasks.txt file with your custom graph input for Code 4.

## Dependencies
- ortools (for Code 1)
- networkx (for all codes)
- simpy (for Code 3 and Code 4)
- matplotlib (for Code 3 and Code 4)

## Note
The Graph Burning problem is known to be NP-hard, so for large graphs, the brute force algorithm may take a significant amount of time to compute. The exact algorithms (Code 3 and Code 4) are more efficient but may still have limitations for very large graphs.

---

Please ensure you have the correct Python environments set up with the necessary dependencies to run the codes successfully. Feel free to reach out if you have any questions or need further assistance. Happy graph burning!