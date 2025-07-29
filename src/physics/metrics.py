import sympy as sp

class AlcubierreMetrics:
    def __init__(self):
        # Variables simbólicas
        self.x, self.y, self.R, self.sigma = sp.symbols('x y R sigma', real=True, positive=True)
        self.rs = sp.sqrt(self.x**2 + self.y**2)

        # Definir f(rs)
        self.f_rs = (sp.tanh(self.sigma * (self.rs + self.R)) - sp.tanh(self.sigma * (self.rs - self.R))) / (2 * sp.tanh(self.sigma * self.R))

    def compute_derivatives(self):
        df_dx = sp.simplify(sp.diff(self.f_rs, self.x))
        df_dy = sp.simplify(sp.diff(self.f_rs, self.y))
        laplacian = sp.simplify(sp.diff(df_dx, self.x) + sp.diff(df_dy, self.y))
        return df_dx, df_dy, laplacian

    def energy_density_negative_condition(self):
        _, _, laplacian = self.compute_derivatives()
        rho_condition = sp.simplify(laplacian < 0)
        return rho_condition

    def evaluate_numeric(self, R_val=2, sigma_val=10, x_val=1.0, y_val=0.0):
        # Sustituir y evaluar simbólicamente
        _, _, laplacian = self.compute_derivatives()
        subs_dict = {self.R: R_val, self.sigma: sigma_val, self.x: x_val, self.y: y_val}
        rho_val = laplacian.evalf(subs=subs_dict)
        return rho_val

    def get_metric_equation(self):
        v_s, f = sp.symbols('v_s f', real=True)
        # Métrica simplificada 1D de Alcubierre
        ds2 = -sp.Symbol('c')**2 * sp.Symbol('dt')**2 + (sp.Symbol('dx') - v_s * f * sp.Symbol('dt'))**2
        return sp.simplify(ds2)