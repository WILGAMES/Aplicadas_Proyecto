# tests/test_optimization.py

import pytest
from src.graph_utils import load_graph_from_json
from src.optimization import solve_tsp_nearest_neighbor, solve_tsp_approximation, shortest_path

@pytest.fixture
def graph():
    """Fixture para cargar el grafo de prueba."""
    return load_graph_from_json("data/sample_graph.json")

def test_tsp_nearest_neighbor(graph):
    path, cost = solve_tsp_nearest_neighbor(graph, start_node="Base")
    
    # El path debe iniciar y terminar en Base
    assert path[0] == "Base"
    assert path[-1] == "Base"

    # Debe visitar todos los nodos al menos una vez
    unique_nodes_in_path = set(path)
    assert {"Base", "A", "B", "C"}.issubset(unique_nodes_in_path)

    # El costo debe ser mayor que cero
    assert cost > 0

def test_tsp_approximation(graph):
    path, cost = solve_tsp_approximation(graph)

    # El path debe ser un ciclo
    assert path[0] == path[-1]

    # Debe visitar todos los nodos al menos una vez
    unique_nodes_in_path = set(path)
    assert {"Base", "A", "B", "C"}.issubset(unique_nodes_in_path)

    # El costo debe ser mayor que cero
    assert cost > 0

def test_shortest_path(graph):
    path, cost = shortest_path(graph, "A", "C")

    # La ruta A-C debe ser directa o pasar por otro nodo
    assert path[0] == "A"
    assert path[-1] == "C"

    # El costo debe coincidir con el menor valor posible
    # A <-> C directo tiene peso 25
    assert cost == 25
