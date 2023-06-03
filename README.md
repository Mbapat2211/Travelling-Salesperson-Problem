# Travelling Salesperson Problem

The Travelling Salesperson Problem (also called the Travelling Salesman Problem or TSP) is an NP-Hard problem which asks the following question: Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city exactly once and returns to the origin city?

Several approaches have been formulated to solve TSP including the Brute Force method, the branch and bound method and the nearest neighbour method. Given the computation intensivity of these algorithms, various AI techniques were developed to solve the problem. This repository contains the solution to TSP using the following three algorithms: 
    
    1. Best First Search 
    2. A Star Algorithm
    3. Genetic Algorithm
    
## Best First Search

The idea of Best First Search is to use an heuristic function to decide which path is most promising and then explore. In this solution, the costs of the MST graphs are used as heuristics to decide on the next node to be chosen in the path. At every step, the MST costs are compared and nodes are selected accordingly till all the nodes are traversed.

## A Star Algorithm

A* or A Star Algorithm is a searching algorithm that searches for the shortest path between the initial and the final state using a herusistic function. Once again the MST graph costs are used as heuristics to determine the shortest path. Unlike Best First Search, A star algorithm explores the path till a much greater depth thereby resulting in an optimal solution in all cases depending on the appropriateness of the heuristic function.

## Genetic Algorithm

Genetic Algorithm is a search-based optimization technique based on the principles of Genetics and Natural Selection. Parent Generations are initalised by creating random solution paths. Few of these solutions are selected for mutation and cross over in order to produce the next generation of solution. At each generation, the solution with the least cost is considered. After multiple successive generations, the path with least cost is declared as the final solution to the problem.