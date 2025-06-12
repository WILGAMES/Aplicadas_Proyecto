import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DroneOptimization:
    def __init__(self):
        # Coeficientes de la función objetivo (consumo energético por km)
        self.c_A = 1.2  # Zona A (terreno plano)
        self.c_B = 0.9  # Zona B (terreno urbano)  
        self.c_C = 1.5  # Zona C (terreno montañoso)
        
    def objective_function(self, x):
        """
        Función objetivo: minimizar el consumo energético total
        f(s, w, j) = 1.2s + 0.9w + 1.5j
        """
        s, w, j = x
        return self.c_A * s + self.c_B * w + self.c_C * j
    
    def constraint_autonomy(self, x):
        """
        Restricción de autonomía: s + w + j <= 15
        """
        s, w, j = x
        return 15 - (s + w + j)
    
    def constraint_priority(self, x):
        """
        Restricción de cobertura prioritaria: s = 2j
        """
        s, w, j = x
        return s - 2 * j
    
    def constraint_energy_balance(self, x):
        """
        Restricción de equilibrio energético: 0.9w = 1.2s
        """
        s, w, j = x
        return 0.9 * w - 1.2 * s
    
    def solve_optimization(self):
        """
        Resuelve el problema de optimización usando scipy
        """
        # Punto inicial
        x0 = [5, 7, 2.5]
        
        # Definir restricciones
        constraints = [
            {'type': 'ineq', 'fun': self.constraint_autonomy},
            {'type': 'eq', 'fun': self.constraint_priority},
            {'type': 'eq', 'fun': self.constraint_energy_balance}
        ]
        
        # Límites para las variables (no negativas)
        bounds = [(0, None), (0, None), (0, None)]
        
        # Resolver
        result = minimize(
            self.objective_function,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints
        )
        
        return result
    
    def analytical_solution(self):
        """
        Solución analítica del problema
        """
        # De las restricciones de igualdad:
        # s = 2j
        # w = (4/3)s = (8/3)j
        # Sustituyendo en la restricción de autonomía:
        # 2j + (8/3)j + j = 15
        # (17/3)j = 15
        # j = 45/17
        
        j = 45/17
        s = 2 * j
        w = (8/3) * j
        
        return s, w, j
    
    def verify_solution(self, s, w, j):
        """
        Verifica que la solución cumple todas las restricciones
        """
        print("=== VERIFICACIÓN DE LA SOLUCIÓN ===")
        print(f"s = {s:.4f} km (Zona A)")
        print(f"w = {w:.4f} km (Zona B)")  
        print(f"j = {j:.4f} km (Zona C)")
        print()
        
        # Verificar restricción de autonomía
        total_distance = s + w + j
        print(f"Restricción de autonomía: {total_distance:.4f} ≤ 15")
        print(f"Cumple: {total_distance <= 15.001}")  # Tolerancia numérica
        print()
        
        # Verificar restricción de prioridad
        priority_check = abs(s - 2*j)
        print(f"Restricción de prioridad: |s - 2j| = {priority_check:.6f}")
        print(f"Cumple: {priority_check < 0.001}")
        print()
        
        # Verificar equilibrio energético
        energy_balance = abs(0.9*w - 1.2*s)
        print(f"Equilibrio energético: |0.9w - 1.2s| = {energy_balance:.6f}")
        print(f"Cumple: {energy_balance < 0.001}")
        print()
        
        # Consumo total
        total_energy = self.objective_function([s, w, j])
        print(f"Consumo energético total: {total_energy:.4f} unidades")
        
        return total_energy

# Ejecutar optimización
print("OPTIMIZACIÓN DEL RECORRIDO DEL DRON")
print("="*50)

optimizer = DroneOptimization()

# Solución numérica
print("\n1. SOLUCIÓN NUMÉRICA (scipy.optimize)")
result = optimizer.solve_optimization()

if result.success:
    s_num, w_num, j_num = result.x
    print(f"Solución encontrada:")
    print(f"s = {s_num:.4f} km")
    print(f"w = {w_num:.4f} km") 
    print(f"j = {j_num:.4f} km")
    print(f"Consumo mínimo: {result.fun:.4f} unidades")
else:
    print("No se pudo encontrar una solución óptima")

print("\n" + "="*50)

# Solución analítica
print("\n2. SOLUCIÓN ANALÍTICA")
s_ana, w_ana, j_ana = optimizer.analytical_solution()
print(f"s = {s_ana:.4f} km")
print(f"w = {w_ana:.4f} km")
print(f"j = {j_ana:.4f} km")

print("\n" + "="*50)

# Verificación
optimizer.verify_solution(s_ana, w_ana, j_ana)
