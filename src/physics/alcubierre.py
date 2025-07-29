import numpy as np
import matplotlib.pyplot as plt

class AlcubierreDrive:
    def __init__(self):
        self.curvature = 0

    def calculate_curvature(self, mass, energy_density):
        # Simplified formula for curvature based on mass and energy density
        self.curvature = mass / energy_density
        return self.curvature

    def explain_concept(self):
        explanation = (
            "El motor de curvatura de Alcubierre es una solución teórica a las ecuaciones de "
            "Einstein que permite viajar más rápido que la luz al expandir el espacio detrás de "
            "una nave y contraerlo frente a ella. Esto crea una 'burbuja' que se mueve a través "
            "del espacio-tiempo, permitiendo que la nave se desplace sin violar las leyes de la "
            "relatividad."
        )
        return explanation

    def simulate_drive(self, mass, energy_density):
        curvature = self.calculate_curvature(mass, energy_density)
        simulation_result = (
            f"Simulación del motor de curvatura:\n"
            f" - Masa: {mass} kg\n"
            f" - Densidad de energía: {energy_density} J/m³\n"
            f" - Curvatura calculada: {curvature}\n"
            "La nave puede potencialmente viajar a velocidades superlumínicas."
        )
        return simulation_result
    
    def plot_curvature(self, mass, energy_density):
        x = np.linspace(-10, 10, 400)
        # Ejemplo de deformación: una función gaussiana que representa la burbuja
        curvature = np.exp(-((x)**2) / (2 * (mass / (energy_density+1e-6))**2))
        plt.figure(figsize=(8,4))
        plt.plot(x, curvature, label='Curvatura del espacio-tiempo')
        plt.title('Deformación del espacio-tiempo (Burbuja de Alcubierre)')
        plt.xlabel('Posición')
        plt.ylabel('Curvatura relativa')
        plt.legend()
        plt.grid(True)
        plt.show()