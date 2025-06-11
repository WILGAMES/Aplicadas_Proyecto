# tests/test_graph_utils.py

import pytest
from src.graph_utils import load_graph_from_json, get_graph_info

def test_load_graph_from_json():
    graph = load_graph_from_json("data/sample_graph.json")
    info = get_graph_info(graph)

    # Verificamos que hay 4 nodos
    assert info['num_nodes'] == 4

    # Verificamos que hay 6 aristas
    assert info['num_edges'] == 6

    # Verificamos que los nodos contienen "Base", "A", "B", "C"
    node_ids = [node[0] for node in info['nodes']]
    assert set(node_ids) == {"Base", "A", "B", "C"}
