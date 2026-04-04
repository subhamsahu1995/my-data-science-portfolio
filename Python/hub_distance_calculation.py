import itertools
import numpy as np

# Define the distance matrix (7 locations including "Hub" as 0)
distances = np.array([
    [0, 132, 217, 164, 58, 20, 30],  # Hub (0)
    [132, 0, 290, 201, 74, 50, 60],  # 1
    [217, 290, 0, 113, 303, 70, 80],  # 2
    [164, 201, 113, 0, 196, 90, 100], # 3
    [58, 74, 303, 196, 0, 110, 120],  # 4
    [20, 50, 70, 90, 110, 0, 180],    # 5
    [30, 60, 80, 100, 120, 180, 0]    # 6
])

# Function to calculate the total distance of a route
def total_distance(route):
    distance = 0
    for index in range(len(route) - 1):
        current_city = route[index]
        next_city = route[index + 1]
        distance += distances[current_city, next_city]  # Adding distances
    distance += distances[route[-1], route[0]]  # Returning to start
    return distance
'''
def total_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += distances[route[i], route[i + 1]]
    distance += distances[route[-1], route[0]]  # Return to starting hub
    return distance
'''
# Generate all possible routes (permutations of hubs 1-6)
hubs = [1, 2, 3, 4, 5, 6]
all_routes = list(itertools.permutations(hubs))

# Store route distances
route_distances = []
for route in all_routes:
    route_with_start = [0] + list(route) + [0]  # Start & end at Hub 0
    dist = total_distance(route_with_start) # Calling the function
    route_distances.append((route_with_start, dist))

# Sort routes by distance (ascending)
sorted_routes = sorted(route_distances, key=lambda x: x[1])

# Remove duplicate distances while keeping order
unique_routes = []
seen_distances = set()
# top 5 unique shortest routes from the sorted list of routes.
#sorted_routes = [([0, 1, 2, 3, 4, 5, 6, 0], 300),...,...,]
for route, dist in sorted_routes:  
    if dist not in seen_distances:
        unique_routes.append((route, dist))
        seen_distances.add(dist)
    if len(unique_routes) == 5:  # Stop once we have 5 unique routes
        break


# Display the top 5 unique shortest routes
print("\nTop 5 shortest unique routes (ascending order of distance):")
for i, (route, dist) in enumerate(unique_routes):
    print(f"Top {i+1} Route: {route} with distance {dist}")
