Método de la Secante
from math import exp, sin, cos
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np
def f(x, funcion):
 return eval(funcion)
def secante(funcion, x0, x1, tol=1e-6, max_iter=100):
 datos = []
 for i in range(max_iter):
 fx0 = f(x0, funcion)
 fx1 = f(x1, funcion)
 if fx1 - fx0 == 0:
 print("Error: La función no cambia de signo en el intervalo
proporcionado.")
 return None, None
 x2 = x1 - fx1 * (x0 - x1) / (fx0 - fx1)
 if i > 0:
 error_relativo = abs((x2 - x1) / x2)
 else:
 error_relativo = None
 datos.append([x1, x0, fx1, fx0, x2, error_relativo])
 if abs(f(x2, funcion)) < tol:
 break
 x0, x1 = x1, x2
 if abs(f(x2, funcion)) < tol:
 print(f"La raíz aproximada es: {x2}")
 else:
 print("El método no converge después de", max_iter,
"iteraciones.")
 return x2, datos
def graficar_funcion(funcion, a, b, raiz):
 x_vals = np.linspace(a, b, 100)
 y_vals = [f(x_i, funcion) for x_i in x_vals]
 plt.figure(figsize=(8, 6))
 plt.plot(x_vals, y_vals)
 plt.axhline(0, color='black')
 plt.axvline(raiz, color='red', linestyle='--', label='Raíz')
 plt.plot(raiz, f(raiz, funcion), 'ro')
 plt.title(f"Gráfica de la función: {funcion}")
 plt.xlabel("x")
 plt.ylabel("y")
 plt.grid(True)
 plt.legend()
 plt.show()
funcion = input("Ingrese la función (use x como variable): ")
x0 = float(input("Ingrese el valor inicial x0: "))
x1 = float(input("Ingrese el valor inicial x1: "))
raiz, datos = secante(funcion, x0, x1)
if raiz is not None:
 print("\nMétodo de la Secante:")
 headers = ["x1", "x0", "f(x1)", "f(x0)", "x2", "Error Relativo"]
 print(tabulate(datos, headers=headers, floatfmt=(".6f", ".6f", ".6f",
".6f", ".6f", ".6e")))
 a = min(x0, x1)
 b = max(x0, x1)
 graficar_funcion(funcion, a, b, raiz)