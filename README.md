
# Optimización de Recorrido de Drones para Monitoreo Agrícola

---

## 📋 Descripción del Proyecto

Este proyecto implementa un sistema de **optimización matemática** para determinar el recorrido más eficiente de un dron al monitorear tres zonas agrícolas distintas. Usando **programación lineal con restricciones**, se minimiza el consumo energético total, considerando las particularidades de cada terreno.

---

### 🧩 Problema a Resolver

Un dron debe monitorear tres zonas agrícolas con diferentes características de terreno:

* **Zona A**: Terreno plano *(consumo: 1.2 unidades/km)*
* **Zona B**: Terreno urbano *(consumo: 0.9 unidades/km)*
* **Zona C**: Terreno montañoso *(consumo: 1.5 unidades/km)*

**Objetivo:** Determinar las distancias óptimas a recorrer en cada zona, minimizando el consumo energético bajo las siguientes restricciones:

1. **Autonomía limitada:** El dron puede recorrer máximo **15 km**
2. **Cobertura prioritaria:** La distancia hacia la Zona A debe ser el **doble** que hacia la Zona C
3. **Equilibrio energético:** El consumo energético hacia las Zonas A y B debe ser **igual**

---

## 🎯 Objetivos

* **Objetivo Principal:**
  Minimizar la función de consumo energético
  $f(s,w,j) = 1.2s + 0.9w + 1.5j$

* **Objetivos Secundarios:**

  * Validar la solución con diferentes métodos matemáticos
  * Proporcionar visualizaciones comprensivas del problema
  * Realizar análisis de sensibilidad y optimización

---

## 🔧 Características del Sistema

### Módulos Principales

1. **Solver de Optimización** (`optimization_solver.py`)

   * Solución numérica (SciPy)
   * Solución analítica por sustitución directa
   * Verificación automática de restricciones
   * Comparación de métodos de solución

2. **Sistema de Visualización** (`visualization.py`)

   * Gráficas 3D de la función objetivo
   * Análisis de contornos y regiones factibles
   * Análisis de sensibilidad paramétrica
   * Dashboard de métricas y resultados

3. **Análisis de Lagrange** (`lagrange_analysis.py`)

   * Implementación simbólica (SymPy)
   * Resolución del sistema Karush-Kuhn-Tucker (KKT)
   * Verificación de condiciones de optimalidad
   * Análisis de la matriz Hessiana

---

### 🧪 Metodologías Implementadas

* Programación Lineal con Restricciones
* Multiplicadores de Lagrange
* Condiciones KKT (Karush-Kuhn-Tucker)
* Análisis de Sensibilidad
* Verificación de Optimalidad

---

## 📊 Resultados Esperados

### Solución Óptima (Ejemplo)

| Zona              | Distancia (km) |
| ----------------- | -------------- |
| **A (Plano)**     | 5.29           |
| **B (Urbano)**    | 7.06           |
| **C (Montañoso)** | 2.65           |
| **Total**         | **15.00**      |

* **Consumo Energético Total:** 16.68 unidades

### Validación de Restricciones

* ✅ **Autonomía:** 15.00 ≤ 15 km
* ✅ **Cobertura prioritaria:** s = 2j (5.29 = 2 × 2.65)
* ✅ **Equilibrio energético:** 0.9w = 1.2s (6.35 ≈ 6.35)

---

## 🛠️ Instalación y Configuración

### Requisitos del Sistema

* **Python:** 3.8 o superior
* **SO:** Windows, macOS o Linux
* **RAM:** 4GB mínimo recomendado
* **Espacio en disco:** 500MB

### Dependencias Requeridas

Instalar con:

```bash
pip install numpy scipy matplotlib seaborn sympy
```

#### Descripción de dependencias

| Biblioteca | Versión mínima | Propósito                                      |
| ---------- | -------------- | ---------------------------------------------- |
| NumPy      | ≥ 1.19.0       | Cálculos numéricos y operaciones matriciales   |
| SciPy      | ≥ 1.7.0        | Algoritmos de optimización y métodos numéricos |
| Matplotlib | ≥ 3.3.0        | Gráficos y visualizaciones                     |
| Seaborn    | ≥ 0.11.0       | Mejoras estéticas para visualizaciones         |
| SymPy      | ≥ 1.8.0        | Cálculos simbólicos y álgebra                  |

---

### Instalación Paso a Paso

1. **Clonar el proyecto**

   ```bash
   git clone [URL_DEL_REPOSITORIO]
   cd drone-optimization-project
   ```

2. **Crear entorno virtual (opcional y recomendado)**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**

   ```bash
   pip install -r requirements.txt
   # O instalar manualmente:
   pip install numpy scipy matplotlib seaborn sympy
   ```

4. **Verificar instalación**

   ```bash
   python -c "import numpy; import scipy; import matplotlib; import seaborn; import sympy; print('✅ Todas las dependencias instaladas correctamente')"
   ```

---

## 🚀 Uso del Sistema

### Ejecución de Scripts

Ejecutar en este orden:

#### 1. Análisis de Optimización

```bash
python scripts/optimization_solver.py
```

*Salida esperada:*

* Solución numérica y analítica
* Verificación de restricciones
* Métricas de convergencia

#### 2. Generación de Visualizaciones

```bash
python scripts/visualization.py
```

*Salida esperada:*

* Gráficas 3D
* Contornos y regiones factibles
* Dashboard de métricas

#### 3. Análisis de Lagrange

```bash
python scripts/lagrange_analysis.py
```

*Salida esperada:*

* Sistema de ecuaciones KKT
* Análisis de matriz Hessiana

---

### Interpretación de Resultados

* **Función Objetivo:** Valor mínimo de consumo energético
* **Variables de Decisión:** Distancias óptimas (s, w, j)
* **Multiplicadores de Lagrange:** Sensibilidad de restricciones
* **Visualizaciones:** Superficie 3D, contornos, región factible, análisis de sensibilidad

---

## 📁 Estructura del Proyecto

```text
drone-optimization-project/
│
├── scripts/
│   ├── optimization_solver.py   # Solver principal
│   ├── visualization.py         # Visualizaciones
│   └── lagrange_analysis.py     # Análisis Lagrange
│
├── README.md                    # Documentación
├── requirements.txt             # Dependencias
└── .gitignore                   # Exclusiones de Git
```

---

## 🔍 Solución de Problemas

### Errores Comunes

* **ModuleNotFoundError: No module named 'numpy'**

  * Solución:

    ```bash
    pip install numpy scipy matplotlib seaborn sympy
    ```

* **ImportError: cannot import name 'minimize' from 'scipy.optimize'**

  * Causa: SciPy obsoleta
  * Solución:

    ```bash
    pip install --upgrade scipy
    ```

* **Las gráficas no se muestran**

  * Causa: backend de Matplotlib
  * Solución:

    ```python
    import matplotlib
    matplotlib.use('TkAgg')  # o 'Qt5Agg'
    import matplotlib.pyplot as plt
    ```

* **RuntimeError: Python is not installed as a framework** *(macOS)*

  * Solución:

    ```bash
    pip install --upgrade matplotlib
    # O con conda:
    conda install matplotlib
    ```

### Verificación de Funcionamiento

```bash
# Verificar Python
python --version

# Verificar dependencias
python -c "
import sys
print(f'Python: {sys.version}')
import numpy as np
print(f'NumPy: {np.__version__}')
import scipy
print(f'SciPy: {scipy.__version__}')
import matplotlib
print(f'Matplotlib: {matplotlib.__version__}')
import seaborn as sns
print(f'Seaborn: {sns.__version__}')
import sympy
print(f'SymPy: {sympy.__version__}')
print('✅ Todas las dependencias funcionan correctamente')
"
```
