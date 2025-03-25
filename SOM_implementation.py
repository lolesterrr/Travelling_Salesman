import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Estimated city coordinates based on distances (these are illustrative)
city_coords = {
    "City1": (0, 0),   # Starting city
    "City2": (2, 4),
    "City3": (5, 2),
    "City4": (7, 5),
    "City5": (3, 6),
    "City6": (9, 3),
    "City7": (4, 1)
}

# Convert to NumPy arrays
city_names = list(city_coords.keys())
coordinates = np.array(list(city_coords.values()))

# Initialize SOM nodes (random positions)
num_nodes = len(city_coords)
som_nodes = np.random.rand(num_nodes, 2) * 10  # Scale within map

# SOM parameters
learning_rate = 0.8
radius = num_nodes / 2
decay = 0.99
iterations = 200

# Setup plot
fig, ax = plt.subplots(figsize=(8, 6))
sc_cities = ax.scatter(coordinates[:, 0], coordinates[:, 1], c='red', marker='o', label="Cities")
sc_nodes, = ax.plot(som_nodes[:, 0], som_nodes[:, 1], 'bo-', alpha=0.5, label="SOM Nodes")
ax.legend()
ax.set_title("Self-Organizing Map Training for TSP")

# Animation function
def update(frame):
    global som_nodes, learning_rate, radius

    city = coordinates[np.random.randint(len(city_coords))]  # Random city selection
    distances = np.linalg.norm(som_nodes - city, axis=1)  # Distance to all nodes
    winner_idx = np.argmin(distances)  # Closest SOM node

    # Adjust nodes in the neighborhood
    for j in range(num_nodes):
        distance_factor = np.exp(-np.linalg.norm(j - winner_idx) / radius)
        som_nodes[j] += learning_rate * distance_factor * (city - som_nodes[j])

    # Update learning rate and radius
    learning_rate *= decay
    radius *= decay

    # Update visualization
    sc_nodes.set_data(som_nodes[:, 0], som_nodes[:, 1])
    return sc_nodes,

# Run animation
ani = animation.FuncAnimation(fig, update, frames=iterations, interval=50, repeat=False)
plt.show()

# Extract the tour from SOM nodes
def extract_tour(som_nodes, coordinates):
    tour = []
    current_idx = np.argmin(np.linalg.norm(som_nodes - coordinates[0], axis=1))
    tour.append(current_idx)
    visited = set([current_idx])

    while len(tour) < num_nodes:
        distances = np.linalg.norm(som_nodes[current_idx] - som_nodes, axis=1)
        next_idx = np.argmin(distances)
        if next_idx not in visited:
            tour.append(next_idx)
            visited.add(next_idx)
            current_idx = next_idx

    tour.append(tour[0])  # Return to the starting city
    return tour

tour = extract_tour(som_nodes, coordinates)
tour_names = [city_names[i] for i in tour]

print("SOM Tour:", " → ".join(tour_names))
