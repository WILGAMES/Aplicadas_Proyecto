# Aplicadas_Proyecto

---

# Optimización de Rutas de Drones para Monitoreo de Zonas Agrícolas

Este proyecto implementa un sistema de optimización de rutas para un dron que debe recorrer distintas zonas agrícolas de manera eficiente.

El terreno agrícola se modela como un grafo, donde:
- **Nodos** representan zonas agrícolas o la base del dron.
- **Aristas** representan las posibles conexiones entre zonas, con un peso que indica la distancia o el consumo energético.

El objetivo es:
- Encontrar la **ruta óptima** que minimice el costo total (distancia o energía).
- Cumplir con restricciones operativas como la autonomía del dron.

---

## Estructura del proyecto

```

data/                 → Grafo de ejemplo (JSON)
notebooks/            → Notebook original del trabajo
src/
graph\_utils.py    → Carga y manejo de grafos
optimization.py   → Algoritmos de optimización (TSP, camino mínimo)
visualization.py  → Visualización gráfica de rutas
tests/                 → Tests automáticos (con pytest)
main.py                → Script principal (flujo completo)
requirements.txt       → Librerías necesarias
README.md              → Este documento

````

---

### Instalar dependencias

```bash
python -m pip install -r requirements.txt
```

---

## Uso

### Ejecutar el flujo completo:

```bash
python main.py
```

Esto cargará el grafo, resolverá el TSP con dos algoritmos, mostrará los resultados en consola y visualizará los grafos con las rutas resaltadas.

---

## Ejecutar tests automáticos

```bash
pytest tests/
```

---

## Metodología

Este proyecto implementa:

 Representación del terreno agrícola como grafo.
 Resolución del **Problema del Viajante (TSP)**:

* Heurística de **vecino más cercano**.
* Algoritmo de **aproximación**.

 Visualización gráfica con NetworkX + Matplotlib.
 Estructura de proyecto profesional con tests.

---

## Ejemplo de salida

```
Resolviendo TSP con vecino más cercano...
Ruta: ['Base', 'A', 'B', 'C', 'Base']
Costo total: 80
```
![image](https://github.com/user-attachments/assets/d0e03119-1d80-4f4b-a983-4e572390e6aa)



---

## Autores

* Smir Estiven Magin Mamian
* Wilder García Muñoz
* Jesús David Tascón

Trabajo final para el curso de Matemáticas Aplicadas II.

---

