# main.py

from src.graph_utils import load_graph_from_json
from src.optimization import solve_tsp_nearest_neighbor, solve_tsp_approximation
from src.visualization import plot_graph, plot_graph_with_path

def main():
    # Cargar grafo
    graph = load_graph_from_json("data/sample_graph.json")
    print("Grafo cargado correctamente.\n")

    # Mostrar grafo completo
    plot_graph(graph, title="Terreno agrícola - Grafo")

    # Resolver TSP (vecino más cercano)
    print("Resolviendo TSP con vecino más cercano...")
    path_nn, cost_nn = solve_tsp_nearest_neighbor(graph, start_node="Base")
    print(f"Ruta (Vecino más cercano): {path_nn}")
    print(f"Costo total: {cost_nn}\n")
    plot_graph_with_path(graph, path_nn, title=f"Ruta TSP - Vecino más cercano (Costo: {cost_nn})")

    # Resolver TSP (aproximación)
    print("Resolviendo TSP con algoritmo de aproximación...")
    path_ap, cost_ap = solve_tsp_approximation(graph)
    print(f"Ruta (Aproximación): {path_ap}")
    print(f"Costo total: {cost_ap}\n")
    plot_graph_with_path(graph, path_ap, title=f"Ruta TSP - Aproximación (Costo: {cost_ap})")

if __name__ == "__main__":
    main()
