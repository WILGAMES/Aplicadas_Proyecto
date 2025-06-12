import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import Polygon
import seaborn as sns

# Configurar estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class DroneVisualization:
    def __init__(self):
        self.c_A = 1.2
        self.c_B = 0.9  
        self.c_C = 1.5
        
    def objective_function(self, s, w, j):
        return self.c_A * s + self.c_B * w + self.c_C * j
    
    def plot_3d_surface(self):
        """
        Gráfica 3D de la función objetivo y restricciones
        """
        fig = plt.figure(figsize=(15, 5))
        
        # Solución óptima
        j_opt = 45/17
        s_opt = 2 * j_opt
        w_opt = (8/3) * j_opt
        
        # Subplot 1: Superficie de la función objetivo
        ax1 = fig.add_subplot(131, projection='3d')
        
        # Crear malla para la superficie
        s_range = np.linspace(0, 10, 50)
        j_range = np.linspace(0, 5, 50)
        S, J = np.meshgrid(s_range, j_range)
        
        # Calcular w usando la restricción w = (4/3)s
        W = (4/3) * S
        
        # Función objetivo
        Z = self.objective_function(S, W, J)
        
        # Superficie
        surf = ax1.plot_surface(S, J, Z, alpha=0.7, cmap='viridis')
        
        # Punto óptimo
        z_opt = self.objective_function(s_opt, w_opt, j_opt)
        ax1.scatter([s_opt], [j_opt], [z_opt], color='red', s=100, label='Óptimo')
        
        ax1.set_xlabel('s (km) - Zona A')
        ax1.set_ylabel('j (km) - Zona C')
        ax1.set_zlabel('Consumo Energético')
        ax1.set_title('Superficie de la Función Objetivo')
        ax1.legend()
        
        # Subplot 2: Restricciones en el plano s-j
        ax2 = fig.add_subplot(132)
        
        # Restricción s = 2j
        j_line = np.linspace(0, 8, 100)
        s_line = 2 * j_line
        ax2.plot(j_line, s_line, 'b-', linewidth=2, label='s = 2j')
        
        # Restricción de autonomía proyectada
        # s + w + j = 15, con w = (4/3)s
        # s + (4/3)s + j = 15
        # (7/3)s + j = 15
        j_autonomy = np.linspace(0, 15, 100)
        s_autonomy = (15 - j_autonomy) * 3/7
        ax2.plot(j_autonomy, s_autonomy, 'g--', linewidth=2, label='Restricción de autonomía')
        
        # Punto óptimo
        ax2.plot(j_opt, s_opt, 'ro', markersize=10, label=f'Óptimo ({j_opt:.2f}, {s_opt:.2f})')
        
        ax2.set_xlabel('j (km) - Zona C')
        ax2.set_ylabel('s (km) - Zona A')
        ax2.set_title('Restricciones en el Plano s-j')
        ax2.grid(True, alpha=0.3)
        ax2.legend()
        ax2.set_xlim(0, 8)
        ax2.set_ylim(0, 12)
        
        # Subplot 3: Distribución de distancias
        ax3 = fig.add_subplot(133)
        
        zones = ['Zona A\n(Plano)', 'Zona B\n(Urbano)', 'Zona C\n(Montañoso)']
        distances = [s_opt, w_opt, j_opt]
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        
        bars = ax3.bar(zones, distances, color=colors, alpha=0.8, edgecolor='black')
        ax3.set_ylabel('Distancia (km)')
        ax3.set_title('Distribución Óptima de Distancias')
        ax3.grid(True, alpha=0.3, axis='y')
        
        # Añadir valores en las barras
        for bar, dist in zip(bars, distances):
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                    f'{dist:.2f} km', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.show()
        
    def plot_contour_analysis(self):
        """
        Análisis de contornos y gradientes
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
        
        # Solución óptima
        j_opt = 45/17
        s_opt = 2 * j_opt
        w_opt = (8/3) * j_opt
        
        # Crear malla
        s_range = np.linspace(0, 12, 100)
        j_range = np.linspace(0, 6, 100)
        S, J = np.meshgrid(s_range, j_range)
        
        # Subplot 1: Contornos de la función objetivo
        W = (4/3) * S  # Usando la restricción w = (4/3)s
        Z = self.objective_function(S, W, J)
        
        contour1 = ax1.contour(S, J, Z, levels=20, colors='blue', alpha=0.6)
        ax1.clabel(contour1, inline=True, fontsize=8)
        
        # Restricción s = 2j
        j_line = np.linspace(0, 6, 100)
        s_line = 2 * j_line
        ax1.plot(s_line, j_line, 'r-', linewidth=3, label='s = 2j')
        
        # Punto óptimo
        ax1.plot(s_opt, j_opt, 'ro', markersize=12, label=f'Óptimo')
        
        ax1.set_xlabel('s (km) - Zona A')
        ax1.set_ylabel('j (km) - Zona C')
        ax1.set_title('Contornos de la Función Objetivo')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Subplot 2: Región factible
        # Crear región factible considerando todas las restricciones
        s_feas = np.linspace(0, 10, 1000)
        j_feas = s_feas / 2  # De s = 2j
        w_feas = (4/3) * s_feas  # De w = (4/3)s
        
        # Filtrar por restricción de autonomía
        total_dist = s_feas + w_feas + j_feas
        feasible_mask = total_dist <= 15
        
        s_feasible = s_feas[feasible_mask]
        j_feasible = j_feas[feasible_mask]
        
        ax2.fill_between(s_feasible, 0, j_feasible, alpha=0.3, color='green', label='Región Factible')
        ax2.plot(s_feasible, j_feasible, 'g-', linewidth=2, label='Frontera Factible')
        ax2.plot(s_opt, j_opt, 'ro', markersize=12, label='Óptimo')
        
        ax2.set_xlabel('s (km) - Zona A')
        ax2.set_ylabel('j (km) - Zona C')
        ax2.set_title('Región Factible del Problema')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        # Subplot 3: Análisis de sensibilidad
        # Variar el límite de autonomía
        autonomy_limits = np.linspace(10, 20, 50)
        optimal_energies = []
        
        for limit in autonomy_limits:
            # j = limit * 3/17 (de la solución analítica generalizada)
            j_temp = limit * 3/17
            s_temp = 2 * j_temp
            w_temp = (8/3) * j_temp
            energy = self.objective_function(s_temp, w_temp, j_temp)
            optimal_energies.append(energy)
        
        ax3.plot(autonomy_limits, optimal_energies, 'b-', linewidth=2)
        ax3.axvline(x=15, color='r', linestyle='--', label='Límite actual (15 km)')
        ax3.axhline(y=self.objective_function(s_opt, w_opt, j_opt), color='r', linestyle='--', alpha=0.5)
        
        ax3.set_xlabel('Límite de Autonomía (km)')
        ax3.set_ylabel('Consumo Energético Óptimo')
        ax3.set_title('Análisis de Sensibilidad - Autonomía')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Subplot 4: Comparación de consumos por zona
        zones = ['Zona A', 'Zona B', 'Zona C']
        distances = [s_opt, w_opt, j_opt]
        unit_costs = [self.c_A, self.c_B, self.c_C]
        total_costs = [d * c for d, c in zip(distances, unit_costs)]
        
        x = np.arange(len(zones))
        width = 0.35
        
        bars1 = ax4.bar(x - width/2, distances, width, label='Distancia (km)', alpha=0.8)
        bars2 = ax4.bar(x + width/2, total_costs, width, label='Consumo Energético', alpha=0.8)
        
        ax4.set_xlabel('Zonas')
        ax4.set_ylabel('Valores')
        ax4.set_title('Comparación: Distancias vs Consumos')
        ax4.set_xticks(x)
        ax4.set_xticklabels(zones)
        ax4.legend()
        ax4.grid(True, alpha=0.3, axis='y')
        
        # Añadir valores en las barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                        f'{height:.2f}', ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.show()
        
    def plot_optimization_summary(self):
        """
        Resumen visual de la optimización
        """
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
        
        # Solución óptima
        j_opt = 45/17
        s_opt = 2 * j_opt
        w_opt = (8/3) * j_opt
        total_energy = self.objective_function(s_opt, w_opt, j_opt)
        
        # Subplot 1: Diagrama de barras con desglose
        categories = ['Distancia\n(km)', 'Costo Unitario\n(energía/km)', 'Costo Total\n(energía)']
        zona_a = [s_opt, self.c_A, s_opt * self.c_A]
        zona_b = [w_opt, self.c_B, w_opt * self.c_B]
        zona_c = [j_opt, self.c_C, j_opt * self.c_C]
        
        x = np.arange(len(categories))
        width = 0.25
        
        ax1.bar(x - width, zona_a, width, label='Zona A (Plano)', color='#FF6B6B', alpha=0.8)
        ax1.bar(x, zona_b, width, label='Zona B (Urbano)', color='#4ECDC4', alpha=0.8)
        ax1.bar(x + width, zona_c, width, label='Zona C (Montañoso)', color='#45B7D1', alpha=0.8)
        
        ax1.set_ylabel('Valores')
        ax1.set_title('Desglose de la Solución Óptima')
        ax1.set_xticks(x)
        ax1.set_xticklabels(categories)
        ax1.legend()
        ax1.grid(True, alpha=0.3, axis='y')
        
        # Subplot 2: Gráfico de pastel - Distribución de distancias
        sizes = [s_opt, w_opt, j_opt]
        labels = [f'Zona A\n{s_opt:.2f} km', f'Zona B\n{w_opt:.2f} km', f'Zona C\n{j_opt:.2f} km']
        colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
        
        wedges, texts, autotexts = ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                          startangle=90, textprops={'fontsize': 10})
        ax2.set_title('Distribución de Distancias por Zona')
        
        # Subplot 3: Gráfico de pastel - Distribución de consumo energético
        energy_sizes = [s_opt * self.c_A, w_opt * self.c_B, j_opt * self.c_C]
        energy_labels = [f'Zona A\n{energy_sizes[0]:.2f}', f'Zona B\n{energy_sizes[1]:.2f}', f'Zona C\n{energy_sizes[2]:.2f}']
        
        wedges2, texts2, autotexts2 = ax3.pie(energy_sizes, labels=energy_labels, colors=colors, 
                                             autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
        ax3.set_title('Distribución de Consumo Energético')
        
        # Subplot 4: Métricas clave
        ax4.axis('off')
        
        # Crear tabla de métricas
        metrics_data = [
            ['Métrica', 'Valor', 'Unidad'],
            ['Distancia Zona A', f'{s_opt:.3f}', 'km'],
            ['Distancia Zona B', f'{w_opt:.3f}', 'km'],
            ['Distancia Zona C', f'{j_opt:.3f}', 'km'],
            ['Distancia Total', f'{s_opt + w_opt + j_opt:.3f}', 'km'],
            ['Consumo Total', f'{total_energy:.3f}', 'unidades'],
            ['Eficiencia', f'{total_energy/(s_opt + w_opt + j_opt):.3f}', 'energía/km']
        ]
        
        table = ax4.table(cellText=metrics_data[1:], colLabels=metrics_data[0],
                         cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1, 2)
        
        # Colorear encabezados
        for i in range(3):
            table[(0, i)].set_facecolor('#E8E8E8')
            table[(0, i)].set_text_props(weight='bold')
        
        ax4.set_title('Métricas de la Solución Óptima', pad=20, fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.show()

# Crear visualizaciones
print("GENERANDO VISUALIZACIONES...")
print("="*50)

visualizer = DroneVisualization()

print("\n1. Generando gráficas 3D y análisis de superficie...")
visualizer.plot_3d_surface()

print("\n2. Generando análisis de contornos y sensibilidad...")
visualizer.plot_contour_analysis()

print("\n3. Generando resumen de optimización...")
visualizer.plot_optimization_summary()

print("\n¡Visualizaciones completadas!")
