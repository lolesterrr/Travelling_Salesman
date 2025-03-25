import numpy as np
import pandas as pd

# Define city names and corresponding labels
city_names = ["Austin", "Birmingham", "Chicago", "Denver", "Edinburgh", "Frankfurt", "Glasgow"]
labels = ["A", "B", "C", "D", "E", "F", "G"]

# Define adjacency matrix (distances) with np.inf for no direct route
distances = np.array([
  [np.inf,12,10,np.inf,np.inf,np.inf,12],#city 1
  [12,np.inf,8,np.inf,np.inf,np.inf,np.inf],#city 2
  [10,8,np.inf,11,3,np.inf,9],#city 3
  [np.inf,12,11,np.inf,11,10,np.inf],#city 4
  [np.inf,np.inf,3,11,np.inf,6,7],#city 5
  [np.inf,np.inf,np.inf,10,6,np.inf,9],#city 6
  [12,np.inf,9,np.inf,7,9,np.inf]#city 7
])

# Convert to Pandas DataFrame for better visualization
adj_matrix = pd.DataFrame(distances, index=city_names, columns=labels)
print(adj_matrix)



import numpy as np
from itertools import permutations

# Define the TSP function using Dynamic Programming
def tsp_dynamic(matrix):
    n = len(matrix)
    all_sets = 1 << n  # Total subsets (2^n)
    
    # Memoization table for DP (set all values to infinity initially)
    dp = np.full((all_sets, n), np.inf)
    dp[1][0] = 0  # Starting at city 0 (Austin)
    
    # Iterate over all subsets of cities
    for subset in range(all_sets):
        for current in range(n):
            if not (subset & (1 << current)):  # If current city is not in subset
                continue
            
            # Check possible previous cities
            for prev in range(n):
                if prev == current or not (subset & (1 << prev)):  
                    continue
                
                prev_subset = subset & ~(1 << current)  # Remove current from subset
                dp[subset][current] = min(
                    dp[subset][current], 
                    dp[prev_subset][prev] + matrix[prev][current]
                )
    
    # Find the optimal route by returning to the start city
    final_state = (1 << n) - 1
    min_cost = np.inf
    last_index = -1
    
    for i in range(1, n):
        cost = dp[final_state][i] + matrix[i][0]  # Return to start
        if cost < min_cost:
            min_cost = cost
            last_index = i
    
    # Reconstruct the path
    path = [0]  # Start at city 0
    subset = final_state
    current = last_index
    
    while current != 0:
        path.append(current)
        prev_subset = subset & ~(1 << current)
        
        # Find the previous city in optimal path
        for prev in range(n):
            if subset & (1 << prev) and dp[subset][current] == dp[prev_subset][prev] + matrix[prev][current]:
                current = prev
                subset = prev_subset
                break

    path.append(0)  # Return to start city
    
    return path, min_cost

# Run the algorithm
optimal_path, optimal_cost = tsp_dynamic(distances)
optimal_path_named = [city_names[i] for i in optimal_path]

print("Optimal Route:", " → ".join(optimal_path_named))
print("Minimum Cost:", optimal_cost)
