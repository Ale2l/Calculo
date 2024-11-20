import numpy as np
from scipy.integrate import quad

# Definir las funciones por tramos
def g(x):
    if 0 <= x <= 0.76:
        return -0.14 * x + 0.56
    else:
        return np.nan

def p(x):
    if 0.68 <= x <= 0.76:
        return -2.9 * (x + 0) + 2.66
    else:
        return np.nan

def h(x):
    if 0.66 <= x <= 0.68:
        return -12.06 * x + 8.91
    else:
        return np.nan

def q(x):
    if 0.66 <= x <= 0.88:
        return -0.48 * x + 1.21
    else:
        return np.nan

def r(x):
    if 0.77 <= x <= 0.88:
        return 9.21 * x**2 - 17.44 * x + 9.01
    else:
        return np.nan

def s(x):
    if 0.77 <= x <= 0.8:
        return 10.03 * x - 6.62
    else:
        return np.nan

def t(x):
    if 0.8 <= x <= 1.05:
        return 1.35 * x**2 - 3.4 * x + 3.25
    else:
        return np.nan

def g_1(x):
    if 1 <= x <= 1.13:
        return -26.75 * x**2 + 59.63 * x - 31.49
    else:
        return np.nan

def h_1(x):
    if 1.13 <= x <= 1.61:
        return -2.44 * x**3 + 12.54 * x**2 - 21.74 * x + 13.81
    else:
        return np.nan

def p_1(x):
    if 1.61 <= x <= 1.62:
        return 14.28 * x - 21.88
    else:
        return np.nan

def q_1(x):
    if 1.62 <= x <= 1.67:
        return 2.25 * x - 2.36
    else:
        return np.nan

def r_1(x):
    if 1.67 <= x <= 1.93:
        return 1.37 * x**2 - 6.01 * x + 7.63
    else:
        return np.nan

def s_1(x):
    if 1.93 <= x <= 2.01:
        return -108.02 * x**2 + 430.48 * x - 427.39
    else:
        return np.nan

def t_1(x):
    if 2.01 <= x <= 2.21:
        return 6.54 * x**2 - 29.64 * x + 34.62
    else:
        return np.nan

def f_2(x):
    if 2.21 <= x <= 2.44:
        return -0.75 * x + 2.71
    else:
        return np.nan

def g_2(x):
    if 2.43 <= x <= 2.51:
        return -57.04 * (x - 0.01)**2 + 284.14 * (x - 0.01) - 352.77
    else:
        return np.nan

def h_2(x):
    if 2.49 <= x <= 2.73:
        return 4.11 * x**2 - 22.66 * x + 32.06
    else:
        return np.nan

def p_2(x):
    if 2.68 <= x <= 2.73:
        return -3.73 * x + 11.01
    else:
        return np.nan

def q_2(x):
    if 2.68 <= x <= 2.76:
        return 2.17 * x - 4.8
    else:
        return np.nan

def s_2(x):
    if 2.76 <= x <= 3.14:
        return 2.14 * x**2 - 13.94 * x + 23.36
    else:
        return np.nan

def r_2(x):
    if 3.14 <= x <= 3.34:
        return -0.64 * x + 2.7
    else:
        return np.nan

def t_4(x):
    if 3.33 <= x <= 3.39:
        return 1.73 * x - 5.21
    else:
        return np.nan

def f_3(x):
    if 3.39 <= x <= 3.55:
        return 5.26 * x**2 - 37.38 * x + 66.93
    else:
        return np.nan

def h_3(x):
    if 3.52 <= x <= 3.55:
        return -4.77 * x + 17.44
    else:
        return np.nan

def p_3(x):
    if 3.52 <= x <= 3.54:
        return 6 * x - 20.48
    else:
        return np.nan

def q_3(x):
    if 3.54 <= x <= 3.73:
        return -1.07 * x + 4.57
    else:
        return np.nan

def r_3(x):
    if 3.73 <= x <= 3.95:
        return -0.79 * x + 3.53
    else:
        return np.nan

def s_3(x):
    if 3.95 <= x <= 4.3:
        return -0.57 * x + 2.66
    else:
        return np.nan

def t_3(x):
    if 4.29 <= x <= 4.33:
        return 1.93 * x - 8.06
    else:
        return np.nan

def f_4(x):
    if 4.32 <= x <= 4.47:
        return 1.26 * x**2 - 11.65 * x + 27.1
    else:
        return np.nan

def g_4(x):
    if 4.42 <= x <= 4.47:
        return -2.72 * (x + 0) + 12.36
    else:
        return np.nan

def h_4(x):
    if 4.42 <= x <= 4.44:
        return 6 * x - 26.18
    else:
        return np.nan

def p_4(x):
    if 4.44 <= x <= 4.65:
        return 3.81 * (x + 0)**2 - 35.6 * (x + 0) + 83.41
    else:
        return np.nan

def f_5(x):
    if 4.65 <= x <= 5.15:
        return -0.53 * (x + 0.02) + 2.73
    else:
        return np.nan

# Función para calcular el área bajo la curva
def area_under_curve(func, a, b):
    area, _ = quad(func, a, b)
    return area

# Lista de funciones con su intervalo
functions = [
    (g, 0, 0.76),
    (p, 0.68, 0.76),
    (h, 0.66, 0.68),
    (q, 0.66, 0.88),
    (r, 0.77, 0.88),
    (s, 0.77, 0.8),
    (t, 0.8, 1.05),
    (g_1, 1, 1.13),
    (h_1, 1.13, 1.61),
    (p_1, 1.61, 1.62),
    (q_1, 1.62, 1.67),
    (r_1, 1.67, 1.93),
    (s_1, 1.93, 2.01),
    (t_1, 2.01, 2.21),
    (f_2, 2.21, 2.44),
    (g_2, 2.43, 2.51),
    (h_2, 2.49, 2.73),
    (p_2, 2.68, 2.73),
    (q_2, 2.68, 2.76),
    (s_2, 2.76, 3.14),
    (r_2, 3.14, 3.34),
    (t_4, 3.33, 3.39),
    (f_3, 3.39, 3.55),
    (h_3, 3.52, 3.55),
    (p_3, 3.52, 3.54),
    (q_3, 3.54, 3.73),
    (r_3, 3.73, 3.95),
    (s_3, 3.95, 4.3),
    (t_3, 4.29, 4.33),
    (f_4, 4.32, 4.47),
    (g_4, 4.42, 4.47),
    (h_4, 4.42, 4.44),
    (p_4, 4.44, 4.65),
    (f_5, 4.65, 5.15)
]

# Calcular área de cada función en su intervalo
areas = []
for func, a, b in functions:
    area = area_under_curve(func, a, b)
    areas.append((func.__name__, a, b, area))

# Imprimir el área de cada función
for func_name, a, b, area in areas:
    print(f'Área bajo {func_name} en el intervalo [{a}, {b}]: {area}')

# Calcular el área total
total_area = sum(area for _, _, _, area in areas)
print(f'Área total bajo la curva: {total_area}')
