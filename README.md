# Travelling_Salesman

**Data Structure of choice**: _ADJACENCY MATRIX_

![Image](https://github.com/user-attachments/assets/6d362e32-8020-44d3-b221-e458746efd79)

**Justification**:
We chose to represent the graph using an adjacency matrix because it provides a straightforward way to store and access the distances between cities. The adjacency matrix allows for constant-time lookup of distances, which is crucial for efficiently implementing TSP algorithms. Given the small size of the graph (7 cities), the adjacency matrix is both simple to implement and effective in terms of performance. Additionally, the symmetry of the matrix reflects the bidirectional nature of the distances, further simplifying the implementation.


**Using Dynammic programming as the classical solution**:
