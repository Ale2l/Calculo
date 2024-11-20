import numpy as np
from scipy.integrate import quad

# Definir las funciones en sus respectivos intervalos
def g(x):
    if 0 <= x <= 0.76:
        return -0.14 * x + 0.56
    return np.nan

def p(x):
    if 0.68 <= x <= 0.76:
        return -2.9 * (x) + 2.66
    return np.nan

def h(x):
    if 0.66 <= x <= 0.68:
        return -12.06 * x + 8.91
    return np.nan

def q(x):
    if 0.66 <= x <= 0.88:
        return -0.48 * x + 1.21
    return np.nan

def r(x):
    if 0.77 <= x <= 0.88:
        return 9.21 * x**2 - 17.44 * x + 9.01
    return np.nan

def s(x):
    if 0.77 <= x <= 0.8:
        return 10.03 * x - 6.62
    return np.nan

def t(x):
    if 0.8 <= x <= 1.05:
        return 1.35 * x**2 - 3.4 * x + 3.25
    return np.nan

def g_1(x):
    if 1 <= x <= 1.13:
        return -26.75 * x**2 + 59.63 * x - 31.49
    return np.nan

def h_1(x):
    if 1.13 <= x <= 1.61:
        return -2.44 * x**3 + 12.54 * x**2 - 21.74 * x + 13.81
    return np.nan

def p_1(x):
    if 1.61 <= x <= 1.62:
        return 14.28 * x - 21.88
    return np.nan

def q_1(x):
    if 1.62 <= x <= 1.67:
        return 2.25 * x - 2.36
    return np.nan

def r_1(x):
    if 1.67 <= x <= 1.93:
        return 1.37 * x**2 - 6.01 * x + 7.63
    return np.nan

def s_1(x):
    if 1.93 <= x <= 2.01:
        return -108.02 * (x)**2 + 430.48 * (x) - 427.39
    return np.nan

def t_1(x):
    if 2.01 <= x <= 2.21:
        return 6.54 * x**2 - 29.64 * x + 34.62
    return np.nan

def f_2(x):
    if 2.21 <= x <= 2.44:
        return -0.75 * x + 2.71
    return np.nan

def g_2(x):
    if 2.43 <= x <= 2.51:
        return -57.04 * (x - 0.01)**2 + 284.14 * (x - 0.01) - 352.77
    return np.nan

def h_2(x):
    if 2.49 <= x <= 2.73:
        return 4.11 * x**2 - 22.66 * x + 32.06
    return np.nan

def p_2(x):
    if 2.68 <= x <= 2.73:
        return -3.73 * x + 11.01
    return np.nan

def q_2(x):
    if 2.68 <= x <= 2.76:
        return 2.17 * x - 4.8
    return np.nan

def s_2(x):
    if 2.76 <= x <= 3.14:
        return 2.14 * (x)**2 - 13.94 * (x) + 23.36
    return np.nan

def r_2(x):
    if 3.14 <= x <= 3.34:
        return -0.64 * (x) + 2.7
    return np.nan

def t_4(x):
    if 3.33 <= x <= 3.39:
        return 1.73 * x - 5.21
    return np.nan

def f_3(x):
    if 3.39 <= x <= 3.55:
        return 5.26 * x**2 - 37.38 * x + 66.93
    return np.nan

def h_3(x):
    if 3.52 <= x <= 3.55:
        return -4.77 * x + 17.44
    return np.nan

def p_3(x):
    if 3.52 <= x <= 3.54:
        return 6 * (x) - 20.48
    return np.nan

def q_3(x):
    if 3.54 <= x <= 3.73:
        return -1.07 * (x) + 4.57
    return np.nan

def r_3(x):
    if 3.73 <= x <= 3.95:
        return -0.79 * (x) + 3.53
    return np.nan

def s_3(x):
    if 3.95 <= x <= 4.3:
        return -0.57 * (x) + 2.66
    return np.nan

def t_3(x):
    if 4.29 <= x <= 4.33:
        return 1.93 * x - 8.06
    return np.nan

def f_4(x):
    if 4.32 <= x <= 4.47:
        return 1.26 * x**2 - 11.65 * x + 27.1
    return np.nan

def g_4(x):
    if 4.42 <= x <= 4.47:
        return -2.72 * (x) + 12.36
    return np.nan

def h_4(x):
    if 4.42 <= x <= 4.44:
        return 6 * x - 26.18
    return np.nan

def p_4(x):
    if 4.44 <= x <= 4.65:
        return 3.81 * (x)**2 - 35.6 * (x) + 83.41
    return np.nan

def f_5(x):
    if 4.65 <= x <= 5.15:
        return -0.53 * (x + 0.02) + 2.73
    return np.nan

# Lista de funciones y sus intervalos
functions = [
    ("g", g, 0, 0.76),
    ("p", p, 0.68, 0.76),
    ("h", h, 0.66, 0.68),
    ("q", q, 0.66, 0.88),
    ("r", r, 0.77, 0.88),
    ("s", s, 0.77, 0.8),
    ("t", t, 0.8, 1.05),
    ("g_1", g_1, 1, 1.13),
    ("h_1", h_1, 1.13, 1.61),
    ("p_1", p_1, 1.61, 1.62),
    ("q_1", q_1, 1.62, 1.67),
    ("r_1", r_1, 1.67, 1.93),
    ("s_1", s_1, 1.93, 2.01),
    ("t_1", t_1, 2.01, 2.21),
    ("f_2", f_2, 2.21, 2.44),
    ("g_2", g_2, 2.43, 2.51),
    ("h_2", h_2, 2.49, 2.73),
    ("p_2", p_2, 2.68, 2.73),
    ("q_2", q_2, 2.68, 2.76),
    ("s_2", s_2, 2.76, 3.14),
    ("r_2", r_2, 3.14, 3.34),
    ("t_4", t_4, 3.33, 3.39),
    ("f_3", f_3, 3.39, 3.55),
    ("h_3", h_3, 3.52, 3.55),
    ("p_3", p_3, 3.52, 3.54),
    ("q_3", q_3, 3.54, 3.73),
    ("r_3", r_3, 3.73, 3.95),
    ("s_3", s_3, 3.95, 4.3),
    ("t_3", t_3, 4.29, 4.33),
    ("f_4", f_4, 4.32, 4.47),
    ("g_4", g_4, 4.42, 4.47),
    ("h_4", h_4, 4.42, 4.44),
    ("p_4", p_4, 4.44, 4.65),
    ("f_5", f_5, 4.65, 5.15)
]

# Función para calcular el volumen del sólido de revolución
def volume_of_revolution(func, a, b):
    integral, _ = quad(lambda x: func(x) ** 2, a, b)
    return integral

# Calcular el volumen total
total_integral = 0
for name, func, a, b in functions:
    integral_value = volume_of_revolution(func, a, b)
    total_integral += integral_value
    print(f"Función {name} en el intervalo [{a}, {b}]: Integral = {integral_value:.4f}")

# Imprimir el valor total de la sumatoria antes de multiplicar por pi
print(f"\nValor total de la sumatoria de las integrales: {total_integral:.4f}")

# Multiplicar el total de las integrales por pi para obtener el volumen total
total_volume = np.pi * total_integral
print(f"Volumen total del sólido de revolución: {total_volume:.4f}")
