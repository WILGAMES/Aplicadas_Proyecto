import numpy as np
import sympy as sp
from sympy import symbols, diff, solve, Matrix, pprint
import matplotlib.pyplot as plt

class LagrangeAnalysis:
    def __init__(self):
        # Definir símbolos
        self.s, self.w, self.j = symbols('s w j', real=True, positive=True)
        self.lambda1, self.lambda2, self.lambda3 = symbols('lambda1 lambda2 lambda3', real=True)
        
        # Función objetivo
        self.f = 1.2*self.s + 0.9*self.w + 1.5*self.j
        
        # Restricciones
        self.g1 = self.s + self.w + self.j - 15  # Autonomía
        self.g2 = self.s - 2*self.j              # Cobertura prioritaria  
        self.g3 = self.w - (4/3)*self.s          # Equilibrio energético
        
    def setup_lagrangian(self):
        """
        Configura el Lagrangiano del problema
        """
        print("ANÁLISIS CON MULTIPLICADORES DE LAGRANGE")
        print("="*60)
        
        # Lagrangiano
        L = self.f - self.lambda1*self.g1 - self.lambda2*self.g2 - self.lambda3*self.g3
        
        print("\n1. FUNCIÓN OBJETIVO:")
        print("f(s, w, j) =", self.f)
        
        print("\n2. RESTRICCIONES:")
        print("g₁(s, w, j) = s + w + j - 15 = 0")
        print("g₂(s, w, j) = s - 2j = 0") 
        print("g₃(s, w, j) = w - (4/3)s = 0")
        
        print("\n3. LAGRANGIANO:")
        print("L(s, w, j, λ₁, λ₂, λ₃) = f - λ₁g₁ - λ₂g₂ - λ₃g₃")
        
        return L
    
    def compute_gradients(self):
        """
        Calcula los gradientes necesarios
        """
        print("\n4. GRADIENTES:")
        print("-" * 30)
        
        # Gradiente de f
        grad_f = [diff(self.f, var) for var in [self.s, self.w, self.j]]
        print("∇f =", grad_f)
        
        # Gradientes de las restricciones
        grad_g1 = [diff(self.g1, var) for var in [self.s, self.w, self.j]]
        grad_g2 = [diff(self.g2, var) for var in [self.s, self.w, self.j]]
        grad_g3 = [diff(self.g3, var) for var in [self.s, self.w, self.j]]
        
        print("∇g₁ =", grad_g1)
        print("∇g₂ =", grad_g2)
        print("∇g₃ =", grad_g3)
        
        return grad_f, grad_g1, grad_g2, grad_g3
    
    def solve_kkt_conditions(self):
        """
        Resuelve las condiciones KKT
        """
        print("\n5. CONDICIONES DE KARUSH-KUHN-TUCKER:")
        print("-" * 45)
        
        # Sistema de ecuaciones KKT
        L = self.setup_lagrangian()
        
        # Derivadas parciales del Lagrangiano
        dL_ds = diff(L, self.s)
        dL_dw = diff(L, self.w)
        dL_dj = diff(L, self.j)
        
        print("∂L/∂s = 0:", dL_ds, "= 0")
        print("∂L/∂w = 0:", dL_dw, "= 0")
        print("∂L/∂j = 0:", dL_dj, "= 0")
        
        # Sistema de ecuaciones
        equations = [
            dL_ds,  # 1.2 - lambda1 - lambda2 + (4/3)*lambda3 = 0
            dL_dw,  # 0.9 - lambda1 - lambda3 = 0
            dL_dj,  # 1.5 - lambda1 + 2*lambda2 = 0
            self.g1,  # s + w + j - 15 = 0
            self.g2,  # s - 2*j = 0
            self.g3   # w - (4/3)*s = 0
        ]
        
        print("\nSistema de ecuaciones a resolver:")
        for i, eq in enumerate(equations, 1):
            print(f"Ecuación {i}: {eq} = 0")
        
        # Resolver el sistema
        variables = [self.s, self.w, self.j, self.lambda1, self.lambda2, self.lambda3]
        
        try:
            solution = solve(equations, variables)
            print("\n6. SOLUCIÓN DEL SISTEMA:")
            print("-" * 30)
            
            if solution:
                for var, val in solution.items():
                    print(f"{var} = {val} = {float(val):.6f}")
                
                # Extraer valores de las variables principales
                s_val = float(solution[self.s])
                w_val = float(solution[self.w])
                j_val = float(solution[self.j])
                
                return s_val, w_val, j_val, solution
            else:
                print("No se encontró solución única")
                return None
                
        except Exception as e:
            print(f"Error al resolver el sistema: {e}")
            return None
    
    def verify_optimality_conditions(self, solution):
        """
        Verifica las condiciones de optimalidad
        """
        if not solution:
            return
            
        print("\n7. VERIFICACIÓN DE CONDICIONES DE OPTIMALIDAD:")
        print("-" * 50)
        
        s_val = float(solution[self.s])
        w_val = float(solution[self.w])
        j_val = float(solution[self.j])
        
        # Verificar que es un punto crítico
        grad_f, grad_g1, grad_g2, grad_g3 = self.compute_gradients()
        
        # Evaluar gradientes en el punto óptimo
        grad_f_val = [float(g.subs([(self.s, s_val), (self.w, w_val), (self.j, j_val)])) for g in grad_f]
        grad_g1_val = [float(g.subs([(self.s, s_val), (self.w, w_val), (self.j, j_val)])) for g in grad_g1]
        grad_g2_val = [float(g.subs([(self.s, s_val), (self.w, w_val), (self.j, j_val)])) for g in grad_g2]
        grad_g3_val = [float(g.subs([(self.s, s_val), (self.w, w_val), (self.j, j_val)])) for g in grad_g3]
        
        print("Gradientes evaluados en el punto óptimo:")
        print(f"∇f = {grad_f_val}")
        print(f"∇g₁ = {grad_g1_val}")
        print(f"∇g₂ = {grad_g2_val}")
        print(f"∇g₃ = {grad_g3_val}")
        
        # Verificar condición ∇f = λ₁∇g₁ + λ₂∇g₂ + λ₃∇g₃
        lambda1_val = float(solution[self.lambda1])
        lambda2_val = float(solution[self.lambda2])
        lambda3_val = float(solution[self.lambda3])
        
        combination = [
            lambda1_val * grad_g1_val[i] + lambda2_val * grad_g2_val[i] + lambda3_val * grad_g3_val[i]
            for i in range(3)
        ]
        
        print(f"\nλ₁∇g₁ + λ₂∇g₂ + λ₃∇g₃ = {combination}")
        print(f"∇f = {grad_f_val}")
        
        # Verificar si son iguales (con tolerancia numérica)
        tolerance = 1e-10
        is_equal = all(abs(combination[i] - grad_f_val[i]) < tolerance for i in range(3))
        print(f"¿Se cumple ∇f = λ₁∇g₁ + λ₂∇g₂ + λ₃∇g₃? {is_equal}")
        
    def analyze_hessian(self, solution):
        """
        Análisis de la matriz Hessiana para verificar optimalidad
        """
        if not solution:
            return
            
        print("\n8. ANÁLISIS DE LA MATRIZ HESSIANA:")
        print("-" * 40)
        
        # Hessiana de la función objetivo (es constante = 0 para función lineal)
        H_f = Matrix([
            [diff(self.f, self.s, 2), diff(self.f, self.s, self.w), diff(self.f, self.s, self.j)],
            [diff(self.f, self.w, self.s), diff(self.f, self.w, 2), diff(self.f, self.w, self.j)],
            [diff(self.f, self.j, self.s), diff(self.f, self.j, self.w), diff(self.f, self.j, 2)]
        ])
        
        print("Hessiana de f:")
        pprint(H_f)
        
        # Para un problema lineal con restricciones lineales, 
        # la optimalidad se determina por la factibilidad
        print("\nNota: Como f es lineal, H_f = 0.")
        print("La optimalidad se determina por las restricciones activas.")
        
    def comparative_analysis(self):
        """
        Análisis comparativo de métodos
        """
        print("\n9. ANÁLISIS COMPARATIVO DE MÉTODOS:")
        print("-" * 45)
        
        # Método de sustitución directa
        print("Método de sustitución directa:")
        print("De g₂: s = 2j")
        print("De g₃: w = (4/3)s = (8/3)j")
        print("Sustituyendo en g₁: 2j + (8/3)j + j = 15")
        print("(17/3)j = 15 → j = 45/17")
        
        j_direct = 45/17
        s_direct = 2 * j_direct
        w_direct = (8/3) * j_direct
        
        print(f"Solución directa: s = {s_direct:.6f}, w = {w_direct:.6f}, j = {j_direct:.6f}")
        
        # Comparar con solución de Lagrange
        solution = self.solve_kkt_conditions()
        if solution:
            s_lag, w_lag, j_lag, _ = solution
            print(f"Solución Lagrange: s = {s_lag:.6f}, w = {w_lag:.6f}, j = {j_lag:.6f}")
            
            # Diferencias
            print(f"Diferencias: Δs = {abs(s_direct - s_lag):.10f}")
            print(f"            Δw = {abs(w_direct - w_lag):.10f}")
            print(f"            Δj = {abs(j_direct - j_lag):.10f}")

# Ejecutar análisis de Lagrange
print("INICIANDO ANÁLISIS CON MULTIPLICADORES DE LAGRANGE")
print("="*60)

analyzer = LagrangeAnalysis()

# Configurar y resolver
L = analyzer.setup_lagrangian()
grad_f, grad_g1, grad_g2, grad_g3 = analyzer.compute_gradients()
solution_data = analyzer.solve_kkt_conditions()

if solution_data:
    s_opt, w_opt, j_opt, full_solution = solution_data
    analyzer.verify_optimality_conditions(full_solution)
    analyzer.analyze_hessian(full_solution)

analyzer.comparative_analysis()

print("\n" + "="*60)
print("ANÁLISIS COMPLETADO")
