import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class CurvaturePlots:
    def __init__(self):
        pass

    def generate_f(self, mass, energy):
        """Función de curvatura basada en masa y energía (simplificada)"""
        sigma = energy / 10.0
        R = mass / 2.0

        def f_rs(rs):
            return (np.tanh(sigma * (rs + R)) - np.tanh(sigma * (rs - R))) / (2 * np.tanh(sigma * R))

        return f_rs

    def plot_static_bubble(self, mass=5, energy=10):
        f_rs = self.generate_f(mass, energy)
        x = np.linspace(-10, 10, 400)
        y = f_rs(np.abs(x))

        plt.figure()
        plt.plot(x, y)
        plt.title(f"Curvatura 1D (masa={mass}, energía={energy})")
        plt.xlabel("Posición")
        plt.ylabel("Curvatura")
        plt.grid(True)
        plt.show()

    def plot_2d_field(self, mass=5, energy=10):
        f_rs = self.generate_f(mass, energy)
        x = np.linspace(-10, 10, 200)
        y = np.linspace(-10, 10, 200)
        X, Y = np.meshgrid(x, y)
        rs = np.sqrt(X**2 + Y**2)
        Z = f_rs(rs)

        plt.figure()
        plt.contourf(X, Y, Z, levels=50, cmap='plasma')
        plt.title(f"Mapa 2D de Curvatura (masa={mass}, energía={energy})")
        plt.colorbar(label="Curvatura")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.axis("equal")
        plt.show()

    def animate_bubble_motion(self, mass=5, energy=10, save_path=None):
        f_rs = self.generate_f(mass, energy)
        fig, ax = plt.subplots()
        x = np.linspace(-10, 10, 400)
        line, = ax.plot([], [], lw=2)
        ax.set_xlim(-10, 10)
        ax.set_ylim(0, 1.2)
        ax.set_title(f"Animación de Burbuja (masa={mass}, energía={energy})")
        ax.set_xlabel("x")
        ax.set_ylabel("Curvatura")

        def init():
            line.set_data([], [])
            return line,

        def update(frame):
            center = -5 + 0.1 * frame
            y = f_rs(np.abs(x - center))
            line.set_data(x, y)
            return line,

        ani = animation.FuncAnimation(fig, update, frames=100, init_func=init, blit=True, interval=50)

        if save_path:
            ani.save(save_path, writer='pillow')
        else:
            plt.show()
