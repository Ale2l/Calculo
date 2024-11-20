import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definir las funciones por tramos
def funcion(x):
    if np.isscalar(x):
        if 0 <= x <= 0.76:
            return -0.14 * x + 0.56
        elif 0.68 <= x <= 0.76:
            return -2.9 * (x + 0) + 2.66
        elif 0.66 <= x <= 0.68:
            return -12.06 * x + 8.91
        elif 0.66 <= x <= 0.88:
            return -0.48 * x + 1.21
        elif 0.77 <= x <= 0.88:
            return 9.21 * x**2 - 17.44 * x + 9.01
        elif 0.77 <= x <= 0.8:
            return 10.03 * x - 6.62
        elif 0.8 <= x <= 1.05:
            return 1.35 * x**2 - 3.4 * x + 3.25
        elif 1 <= x <= 1.13:
            return -26.75 * x**2 + 59.63 * x - 31.49
        elif 1.13 <= x <= 1.61:
            return -2.44 * x**3 + 12.54 * x**2 - 21.74 * x + 13.81
        elif 1.61 <= x <= 1.62:
            return 14.28 * x - 21.88
        elif 1.62 <= x <= 1.67:
            return 2.25 * x - 2.36
        elif 1.67 <= x <= 1.93:
            return 1.37 * x**2 - 6.01 * x + 7.63
        elif 1.93 <= x <= 2.01:
            return -108.02 * x**2 + 430.48 * x - 427.39
        elif 2.01 <= x <= 2.21:
            return 6.54 * x**2 - 29.64 * x + 34.62
        elif 2.21 <= x <= 2.44:
            return -0.75 * x + 2.71
        elif 2.43 <= x <= 2.51:
            return -57.04 * x**2 + 284.14 * x - 352.77
        elif 2.49 <= x <= 2.73:
            return 4.11 * x**2 - 22.66 * x + 32.06
        elif 2.68 <= x <= 2.73:
            return -3.73 * x + 11.01
        elif 2.68 <= x <= 2.76:
            return 2.17 * x - 4.8
        elif 2.76 <= x <= 3.14:
            return 2.14 * x**2 - 13.94 * x + 23.36
        elif 3.14 <= x <= 3.34:
            return -0.64 * x + 2.7
        elif 3.33 <= x <= 3.39:
            return 1.73 * x - 5.21
        elif 3.39 <= x <= 3.55:
            return 5.26 * x**2 - 37.38 * x + 66.93
        elif 3.52 <= x <= 3.55:
            return -4.77 * x + 17.44
        elif 3.52 <= x <= 3.54:
            return 6 * x - 20.48
        elif 3.54 <= x <= 3.73:
            return -1.07 * x + 4.57
        elif 3.73 <= x <= 3.95:
            return -0.79 * x + 3.53
        elif 3.95 <= x <= 4.3:
            return -0.57 * x + 2.66
        elif 4.29 <= x <= 4.33:
            return 1.93 * x - 8.06
        elif 4.32 <= x <= 4.47:
            return 1.26 * x**2 - 11.65 * x + 27.1
        elif 4.42 <= x <= 4.47:
            return -2.72 * x + 12.36
        elif 4.42 <= x <= 4.44:
            return 6 * x - 26.18
        elif 4.44 <= x <= 4.65:
            return 3.81 * x**2 - 35.6 * x + 83.41
        elif 4.65 <= x <= 5.15:
            return -0.53 * x + 2.73
        else:
            return np.nan  # Fuera de los límites
    else:
        return np.array([funcion(xi) for xi in x])  # Para arreglos

# Crear listas para almacenar x e y por tramos
x_vals = []
y_vals = []

# Definir los intervalos de las funciones
intervalos = [
    (0, 0.76), (0.68, 0.76), (0.66, 0.68), (0.66, 0.88), (0.77, 0.88), 
    (0.77, 0.8), (0.8, 1.05), (1, 1.13), (1.13, 1.61), (1.61, 1.62),
    (1.62, 1.67), (1.67, 1.93), (1.93, 2.01), (2.01, 2.21), (2.21, 2.44),
    (2.43, 2.51), (2.49, 2.73), (2.68, 2.73), (2.68, 2.76), (2.76, 3.14),
    (3.14, 3.34), (3.33, 3.39), (3.39, 3.55), (3.52, 3.55), (3.52, 3.54),
    (3.54, 3.73), (3.73, 3.95), (3.95, 4.3), (4.29, 4.33), (4.32, 4.47),
    (4.42, 4.47), (4.42, 4.44), (4.44, 4.65), (4.65, 5.15)
]

# Generar los valores de x e y para cada intervalo
for intervalo in intervalos:
    x_tramo = np.linspace(intervalo[0], intervalo[1], 100)
    y_tramo = funcion(x_tramo)
    x_vals.append(x_tramo)
    y_vals.append(y_tramo)

# Concatenar todos los tramos
x_total = np.concatenate(x_vals)
y_total = np.concatenate(y_vals)

# Crear la figura y el eje 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la función original
ax.plot(x_total, y_total, np.zeros_like(x_total), 'b-')

# Crear la malla de revolución sobre el eje X
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, y_grid = np.meshgrid(theta, y_total)

# Rotación sobre el eje X
x_grid = np.tile(x_total, (100, 1)).T  # Repetir x_total
z_grid = y_grid * np.sin(theta_grid)
y_grid = y_grid * np.cos(theta_grid)

# Graficar la superficie de revolución
ax.plot_surface(x_grid, y_grid, z_grid, color='b', alpha=0.5)

# Ajustar los ejes para mejorar la visualización
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Sólido de Revolución - Árbol")

# Mostrar la figura
plt.show()