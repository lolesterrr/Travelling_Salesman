#(1)Graph representation but using Adjacency Matrix for the TSP with distance between cities
Graph =[
  [0,12,10,0,0,0,12],#city 1
  [12,0,8,0,0,0,0],#city 2
  [10,8,0,11,3,0,9],#city 3
  [0,12,11,0,11,10,0],#city 4
  [0,0,3,11,0,6,7],#city 5
  [0,0,0,10,6,0,9],#city 6
  [12,0,9,0,7,9,0]#city 7
]
#The above matrix is the distance between the cities
#The matrix is symmetric because the distance between city i and city j is the same as the distance between city j and city i
#The diagonal elements are 0 because the distance between a city and itself is 0
#The matrix is complete because the distance between city i and city j is always known

#The graph is represented as a list of lists where the index of the outer list represents the city and the inner list represents the distance between the city and all other cities
#The distance between city i and city j is given by Graph[i][j]
#If the distance is 0, it means that there is no direct connection between the cities


#(2)Classical solution to the TSP problem used is the Dynammic Programmming(Held-Karp algorithm)
# lru_cache is used to cache the results of the subproblems to avoid redundant computations

from functools import lru_cache
def tsp_held_karp(Graph):
    n = len(Graph)
    #Memoization table to store to computed values of visiting each city(State-Space Reduction)
    @lru_cache(None)
    def visit(mask, last):
        if mask == (1 << n) - 1:#Base case: All cities have been visited
            return Graph[last][0],[last,0]  # Return to starting city
        
        min_cost = float('inf')
        best_path = []
        for city in range(n):
            #Bounding step: Skip if city has already been visited and only visit unvisited cities
            if not (mask & (1 << city)):
                new_mask = mask | (1 << city)#Mark city as visited in the State-Space
                new_cost, path = visit(new_mask, city)  # Recursive Call (Recursion Step)
                new_cost += Graph[last][city]
                if new_cost < min_cost:
                    min_cost = new_cost
                    best_path = path + [last] # Store the best path

        return min_cost, best_path
    
    cost, path = visit(1, 0) # Start from city 0
    return cost, path # Return to starting city
    
#The function tsp_held_karp takes the Graph as input and returns the cost of the shortest TSP tour and the path of the tour
print("\nGRAPH REPRESENTATION USING ADJACENCY MATRIX")
print("\nThe distance between the cities is represented by the Adjajency matrix below")
for i in Graph:
    print(i)

cost, path = tsp_held_karp(Graph)
print("\nOptimal TSP Tour Cost:", cost)
print("\nOptimal TSP Tour Path:", path)   

#The time complexity of the Held-Karp algorithm is O(n^2 * 2^n) where n is the number of cities


#(3) Self-Organizing Map(SOM) Approach used to solve the TSP problem
#The SOM is a type of artificial neural network that is trained using unsupervised learning to produce a low-dimensional representation of the input space. It approximates the shortest TSP Path by learning city coordinates and distances between cities(locations) in the input space.
import random
def generate_city_coordinates(n):
    return [(random.uniform(0, 1), random.uniform(0, 1)) for _ in range(n)]

def calculate_distance(city1, city2):
    #This function calculates the distance between two cities
    x1, y1 = city1
    x2, y2 = city2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
def find_closest_neuron(neurons, city):
    return min(range(len(neurons)), key=lambda i: calculate_distance(neurons[i], city))

def tsp_som_approximation(cities, iterations=1000, learning_rate=0.5):
    #Learning rate is the step size for adjusting neuron weights
    # This function trains the SOM to approximate a TSP route.
    # 'iterations' determines how many times the training loop runs.
    # 'learning_rate' controls how much neurons move towards cities.
    # The learning rate decays over time to fine-tune adjustments.
    n = len(cities)
    neurons = cities[:]
    for t in range(iterations):
        city = random.choice(cities)
        winner = find_closest_neuron(neurons, city)
        for i in range(n):
            neurons[i] = (
                neurons[i][0] + learning_rate * (city[0] - neurons[i][0]),
                neurons[i][1] + learning_rate * (city[1] - neurons[i][1])
            )
        learning_rate *= 0.99  # Decay learning rate
    return neurons

def tsp_som_approximation(cities):
    n = len(cities)
    route = list(range(n))
    for _ in range(1000):  # Iterative approximation to improve the route thru trial and error
        random.shuffle(route)
        for i in range(n - 1):
            if calculate_distance(cities[route[i]], cities[route[i + 1]]) > calculate_distance(cities[route[i]], cities[route[-1]]):
                route[i + 1], route[-1] = route[-1], route[i + 1]
    return route + [route[0]]  # Returning to starting city

cities = generate_city_coordinates(7)
route = tsp_som_approximation(cities)
print("\nSOM Approximate TSP Route:", route)
print("\nSOM Approximate TSP Cost:", sum(calculate_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)))
print("\nSOM Apprxoximate TSP Route Total Distance:", sum(calculate_distance(cities[route[i]], cities[route[i + 1]]) for i in range(len(route) - 1)))
