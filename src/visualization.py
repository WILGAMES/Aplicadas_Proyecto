# src/visualization.py

import matplotlib.pyplot as plt
import networkx as nx
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

def plot_cost_surface_3d():
    """Grafica 3D simulada de una función objetivo de optimización."""
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(111, projection='3d')

    # Simular dos variables de decisión (por ejemplo, distancia y energía)
    X = np.linspace(0, 100, 100)
    Y = np.linspace(0, 100, 100)
    X, Y = np.meshgrid(X, Y)

    # Función de costo: se puede ajustar al modelo real
    Z = np.sqrt(X**2 + Y**2) + 10 * np.sin(X / 10) + 5 * np.cos(Y / 10)

    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
    ax.set_title("Superficie de Costo")
    ax.set_xlabel("Distancia acumulada")
    ax.set_ylabel("Consumo energético")
    ax.set_zlabel("Costo total")

    plt.show()

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
