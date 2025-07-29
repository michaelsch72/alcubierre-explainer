import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from physics.alcubierre import AlcubierreDrive
from physics.metrics import AlcubierreMetrics
from visual.plots import CurvaturePlots
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

class UserInterface:
    def __init__(self):
        self.last_mass = 5
        self.last_energy = 10
        self.drive = AlcubierreDrive()
        self.metrics = AlcubierreMetrics()
        self.plots = CurvaturePlots()
        self.root = tk.Tk()
        self.root.title("Explorador del Motor de Curvatura de Alcubierre")
        self.root.geometry("600x550")
        self.style_widgets()
        self.create_widgets()

    def style_widgets(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TLabel", font=("Segoe UI", 11))
        style.configure("TButton", font=("Segoe UI", 11), padding=6)
        style.configure("TScale", troughcolor='#e6e6e6', sliderlength=20)

    def create_widgets(self):
        ttk.Label(self.root, text="Motor de Curvatura de Alcubierre", font=("Segoe UI", 16, "bold")).pack(pady=10)
        ttk.Label(self.root, text="¿Qué deseas explorar?").pack(pady=5)

        btns = [
            ("📘 Concepto básico", self.show_concept),
            ("📐 Cálculo de curvatura", self.calculate_curvature),
            ("🧪 Simulación del motor", self.simulate_drive),
            ("📈 Ver gráfica de curvatura (1D)", self.plot_curvature),
            ("🗺️ Mapa de curvatura 2D", self.plot_2d_field),
            ("🎞️ Animación de burbuja", self.animate_bubble),
            ("⚛️ Análisis simbólico", self.show_symbolic_analysis),
            ("📝 Exportar resultados a PDF", self.export_to_pdf),
            ("❌ Salir", self.root.quit),
        ]

        for txt, cmd in btns:
            ttk.Button(self.root, text=txt, width=40, command=cmd).pack(pady=4)

    def show_concept(self):
        explanation = (
            "El motor de curvatura de Alcubierre es una propuesta teórica dentro de la relatividad general que permitiría el viaje superlumínico "
            "sin violar las leyes físicas conocidas. En lugar de acelerar una nave más allá de la velocidad de la luz en su entorno local, el espacio "
"tiempo mismo se contrae delante de la nave y se expande detrás de ella, creando una 'burbuja' que puede desplazarse a velocidades "
"aparentemente superiores a la luz.\n\n"
"Esto es posible porque la relatividad permite la deformación del espacio-tiempo, no imponiendo un límite de velocidad a la expansión "
"o contracción del propio espacio. Sin embargo, la teoría requiere la existencia de 'materia exótica' con densidad de energía negativa, "
"algo que aún no ha sido observado experimentalmente.\n\n"
"La idea fue propuesta por el físico mexicano Miguel Alcubierre en 1994 y ha inspirado tanto a científicos como a escritores de ciencia ficción."
        )
        self.show_custom_info("Concepto básico", explanation)

    def get_slider_input(self, title):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("400x300")
        window.grab_set()

        ttk.Label(window, text="Masa (kg):").pack(pady=(10, 0))
        mass_var = tk.DoubleVar(value=5)
        mass_slider = ttk.Scale(window, from_=1, to=50, variable=mass_var, orient='horizontal')
        mass_slider.pack(pady=2, fill='x', padx=20)
        mass_label = ttk.Label(window, text=f"{mass_var.get():.1f} kg")
        mass_label.pack(pady=(0, 10))

        ttk.Label(window, text="Densidad de Energía (J/m³):").pack()
        energy_var = tk.DoubleVar(value=10)
        energy_slider = ttk.Scale(window, from_=1, to=100, variable=energy_var, orient='horizontal')
        energy_slider.pack(pady=2, fill='x', padx=20)
        energy_label = ttk.Label(window, text=f"{energy_var.get():.1f} J/m³")
        energy_label.pack(pady=(0, 10))

        def update_labels(*_):
            mass_label.config(text=f"{mass_var.get():.1f} kg")
            energy_label.config(text=f"{energy_var.get():.1f} J/m³")

        mass_var.trace_add("write", update_labels)
        energy_var.trace_add("write", update_labels)

        result = {}

        def on_accept():
            result['mass'] = mass_var.get()
            result['energy'] = energy_var.get()
            window.destroy()

        ttk.Button(window, text="Aceptar", command=on_accept).pack(pady=10)
        window.wait_window()
        return result if result else None

    def calculate_curvature(self):
        values = self.get_slider_input("Cálculo de curvatura")
        if not values:
            return
        self.last_mass = values['mass']
        self.last_energy = values['energy']
        curvature = self.drive.calculate_curvature(values['mass'], values['energy'])
        explanation = (
            f"La curvatura calculada es: {curvature:.4f}\n\n"
            "Esto representa cómo la masa y la energía afectan la deformación del espacio-tiempo.\n"
            "Valores mayores de masa o menores de densidad de energía generan mayor curvatura."
        )
        self.show_custom_info("Curvatura calculada", explanation)

    def simulate_drive(self):
        values = self.get_slider_input("Simulación del motor")
        if not values:
            return
        self.last_mass = values['mass']
        self.last_energy = values['energy']
        result = self.drive.simulate_drive(values['mass'], values['energy'])
        explanation = result + ("\n\nLa burbuja de curvatura permite un desplazamiento superlumínico aparente sin violar la relatividad.")
        self.show_custom_info("Simulación del motor", explanation)

    def plot_curvature(self):
        self.show_custom_info("Gráfica 1D", "Gráfica generada usando la última masa y energía calculadas.")
        self.plots.plot_static_bubble(mass=self.last_mass, energy=self.last_energy)

    def plot_2d_field(self):
        self.show_custom_info("Mapa de curvatura 2D", "Mapa generado con los parámetros actuales de masa y energía.")
        self.plots.plot_2d_field(mass=self.last_mass, energy=self.last_energy)

    def animate_bubble(self):
        self.show_custom_info("Animación de burbuja", "Animación generada con los parámetros actuales de masa y energía.")
        self.plots.animate_bubble_motion(mass=self.last_mass, energy=self.last_energy)

    def show_symbolic_analysis(self):
        metric_eq = self.metrics.get_metric_equation()
        rho_at_point = self.metrics.evaluate_numeric(R_val=2, sigma_val=10, x_val=1, y_val=0)
        negative_cond = self.metrics.energy_density_negative_condition()

       
        explanation = (
"En este análisis simbólico examinamos la métrica propuesta por Miguel Alcubierre en un caso simplificado 1D, así como la curvatura del campo generado.\n\n"
"📐 Métrica 1D de Alcubierre simplificada:\n"
f"  ds² = {metric_eq}\n\n"
"Esta métrica describe cómo se deforma el espacio-tiempo por la función de curvatura f y la velocidad de la burbuja v_s.\n\n"
"📉 Evaluación del laplaciano (∇²f) en el punto x=1, y=0:\n"
f"  ρ ≈ {rho_at_point:.4f} (valor proporcional a la densidad de energía requerida)\n\n"
"❗ Condición simbólica para energía exótica (ρ < 0):\n"
f"  {negative_cond}\n\n"
"La región donde ∇²f < 0 implica que se necesita materia exótica, es decir, una densidad de energía negativa, para sostener la burbuja de curvatura.\n"
"Este es uno de los mayores desafíos físicos para construir un motor de este tipo."
        )
        self.show_custom_info("Análisis simbólico", explanation)

    def export_to_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if not file_path:
            return

        with PdfPages(file_path) as pdf:
            # Usar la función f_rs generada con los últimos valores
            f_rs = self.plots.generate_f(self.last_mass, self.last_energy)
            x_vals = np.linspace(-10, 10, 400)
            y_vals = f_rs(np.abs(x_vals))

            fig1 = plt.figure()
            plt.plot(x_vals, y_vals)
            plt.title("Curvatura del espacio-tiempo (1D)")
            plt.xlabel("Posición")
            plt.ylabel("Curvatura relativa")
            pdf.savefig(fig1)
            plt.close(fig1)

            # Capturar el gráfico 2D usando los mismos parámetros
            fig2 = plt.figure()
            self.plots.plot_2d_field(mass=self.last_mass, energy=self.last_energy)
            pdf.savefig(fig2)
            plt.close(fig2)

            fig3 = plt.figure()
            plt.axis('off')
            metric = self.metrics.get_metric_equation()
            plt.text(0.01, 0.8, "Métrica 1D de Alcubierre:", fontsize=12)
            plt.text(0.01, 0.6, str(metric), fontsize=10)
            plt.text(0.01, 0.4, "Condición para ρ < 0:", fontsize=12)
            plt.text(0.01, 0.2, str(self.metrics.energy_density_negative_condition()), fontsize=10)
            pdf.savefig(fig3)
            plt.close(fig3)

        self.show_custom_info("Exportación completa", f"El informe ha sido guardado en:\n{file_path}")

    def show_custom_info(self, title, content):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("500x400")
        window.configure(bg="#f9f9f9")
        window.grab_set()

        frame = ttk.Frame(window, padding=20)
        frame.pack(fill="both", expand=True)

        text = tk.Text(frame, wrap="word", font=("Segoe UI", 11), background="#ffffff", relief="solid", bd=1)
        text.insert("1.0", content)
        text.configure(state="disabled")
        text.pack(expand=True, fill="both")

        ttk.Button(window, text="Cerrar", command=window.destroy).pack(pady=10)


    def run(self):
        self.root.mainloop()
