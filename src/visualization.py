# src/visualization.py

import matplotlib.pyplot as plt
import networkx as nx

def plot_graph(graph, title="Grafo"):
    """Dibuja el grafo completo con pesos."""
    pos = nx.spring_layout(graph)  # o nx.circular_layout(graph) o nx.planar_layout(graph)

    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=800, font_size=12, font_weight='bold')
    
    # Dibujar pesos
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

    plt.title(title)
    plt.axis('off')
    plt.show()

def plot_graph_with_path(graph, path, title="Ruta óptima"):
    """Dibuja el grafo y resalta una ruta dada (ciclo o camino)."""
    pos = nx.spring_layout(graph)

    plt.figure(figsize=(8, 6))
    # Dibujar todos los nodos y aristas
    nx.draw(graph, pos, with_labels=True, node_color='lightgray', node_size=800, font_size=12)

    # Dibujar pesos
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')

    # Dibujar ruta resaltada
    path_edges = list(zip(path[:-1], path[1:]))  # pares consecutivos
    nx.draw_networkx_edges(graph, pos, edgelist=path_edges, edge_color='blue', width=3)

    # Dibujar nodos del path en otro color
    nx.draw_networkx_nodes(graph, pos, nodelist=path, node_color='orange', node_size=800)

    plt.title(title)
    plt.axis('off')
    plt.show()
