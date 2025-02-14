pip install googlemaps

import networkx as nx
import googlemaps

# Initialize Google Maps Client with your API key
API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
gmaps = googlemaps.Client(key=API_KEY)

def get_distance_from_maps(origin, destination):
    directions = gmaps.directions(origin, destination, mode="driving")
    if directions:
        distance_text = directions[0]['legs'][0]['distance']['text']  # Example: "25 km"
        distance_km = float(distance_text.split()[0])  # Extract numeric value
        return distance_km
    return float('inf')  # If distance not found, set a very high value

# Create a graph and add real distances
G = nx.Graph()
G.add_edge("Warehouse", "City_A", distance=get_distance_from_maps("Warehouse", "City_A"))
G.add_edge("City_A", "City_B", distance=get_distance_from_maps("City_A", "City_B"))
G.add_edge("City_B", "Destination", distance=get_distance_from_maps("City_B", "Destination"))

# Find shortest path
def find_best_route(graph, source, target):
    return nx.shortest_path(graph, source=source, target=target, weight='distance')

def find_best_distance(graph, source, target):
    return nx.shortest_path_length(graph, source=source, target=target, weight='distance')

best_route = find_best_route(G, "Warehouse", "Destination")
best_distance = find_best_distance(G, "Warehouse", "Destination")

print("Optimized Route:", " ➝ ".join(best_route))
print(f"Total Distance: {best_distance} km")
