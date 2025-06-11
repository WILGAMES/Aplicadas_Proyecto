# src/optimization.py

import networkx as nx
from networkx.algorithms import approximation as approx



def solve_tsp_nearest_neighbor(graph, start_node=None):
    """Resuelve el TSP usando la heurística del vecino más cercano."""
    if start_node is None:
        start_node = list(graph.nodes())[0]

    visited = [start_node]
    current_node = start_node
    total_cost = 0

    while len(visited) < len(graph.nodes()):
        neighbors = [
            (neighbor, data['weight'])
            for neighbor, data in graph[current_node].items()
            if neighbor not in visited
        ]

        if not neighbors:
            break  # No hay más nodos alcanzables

        # Seleccionar el vecino más cercano
        next_node, weight = min(neighbors, key=lambda x: x[1])
        visited.append(next_node)
        total_cost += weight
        current_node = next_node

    # Volver al nodo de inicio
    if len(visited) == len(graph.nodes()):
        if graph.has_edge(current_node, start_node):
            total_cost += graph[current_node][start_node]['weight']
            visited.append(start_node)

    return visited, total_cost

def solve_tsp_approximation(graph):
    """Resuelve el TSP usando la función de aproximación de NetworkX."""
    path = approx.traveling_salesman_problem(graph, cycle=True, weight='weight')
    # Calcular costo total
    total_cost = sum(
        graph[path[i]][path[i+1]]['weight']
        for i in range(len(path)-1)
    )
    return path, total_cost

def shortest_path(graph, source, target):
    """Encuentra el camino mínimo entre dos nodos usando Dijkstra."""
    path = nx.dijkstra_path(graph, source, target, weight='weight')
    cost = nx.dijkstra_path_length(graph, source, target, weight='weight')
    return path, cost
