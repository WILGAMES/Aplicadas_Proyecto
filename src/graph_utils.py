# src/graph_utils.py

import networkx as nx
import json
import csv

def create_empty_graph(directed=False):
    """Crea un grafo vacío."""
    if directed:
        return nx.DiGraph()
    else:
        return nx.Graph()

def add_node(graph, node_id, **attributes):
    """Agrega un nodo con atributos opcionales."""
    graph.add_node(node_id, **attributes)

def add_edge(graph, node1, node2, weight=1.0):
    """Agrega una arista con peso."""
    graph.add_edge(node1, node2, weight=weight)

def load_graph_from_json(filepath):
    """Carga un grafo desde un archivo JSON."""
    with open(filepath, 'r') as f:
        data = json.load(f)
    
    graph = create_empty_graph(directed=data.get("directed", False))
    
    # Añadir nodos
    for node in data["nodes"]:
        add_node(graph, node["id"], **node.get("attributes", {}))
    
    # Añadir aristas
    for edge in data["edges"]:
        add_edge(graph, edge["source"], edge["target"], weight=edge.get("weight", 1.0))
    
    return graph

def load_graph_from_csv(filepath):
    """Carga un grafo desde un archivo CSV con formato:
    source,target,weight
    """
    graph = create_empty_graph(directed=False)
    
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            source = row['source']
            target = row['target']
            weight = float(row.get('weight', 1.0))
            add_edge(graph, source, target, weight)
    
    return graph

def get_graph_info(graph):
    """Devuelve información básica del grafo."""
    info = {
        "num_nodes": graph.number_of_nodes(),
        "num_edges": graph.number_of_edges(),
        "nodes": list(graph.nodes(data=True)),
        "edges": list(graph.edges(data=True))
    }
    return info
