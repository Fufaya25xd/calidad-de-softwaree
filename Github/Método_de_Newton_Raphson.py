import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
from sympy import symbols, diff, lambdify

print("Bienvenido al metodo de newton raphson\n")
def newton_raphson(funcion, x0, tol=1e-6, max_iter=100):
    x = symbols('x')
    f = lambdify(x, funcion, 'numpy')
    f_diff = lambdify(x, diff(funcion, x), 'numpy')
    datos = []
    xn = x0
    for i in range(max_iter):
        fxn = f(xn)
        dfxn = f_diff(xn)
        datos.append([i, xn, fxn, dfxn, fxn / dfxn])
        if abs(fxn) < tol:
            break
        xn_nuevo = xn - fxn / dfxn
        if abs(xn_nuevo - xn) < tol:
            break
        xn = xn_nuevo
    if abs(f(xn)) < tol:
        print(f"La raíz aproximada es: {xn}")
    else:
        print("El método no converge después de", max_iter, "iteraciones.")
    return xn, datos

def graficar_funcion(funcion, a, b, raiz):
    x = symbols('x')
    f = lambdify(x, funcion, 'numpy')
    x_vals = np.linspace(a, b, 100)
    y_vals = [f(x_i) for x_i in x_vals]
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals)
    plt.axhline(0, color='black')
    plt.axvline(raiz, color='red', linestyle='--', label='Raíz')
    plt.plot(raiz, f(raiz), 'ro')
    plt.title(f"Gráfica de la función: {funcion}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    plt.show()

funcion = input("Ingrese la función (use x como variable): ")
x0 = float(input("Ingrese el valor inicial x0: "))
raiz, datos = newton_raphson(funcion, x0)

print("\nMétodo de Newton-Raphson:")
headers = ["Iteración", "xn", "f(xn)", "f'(xn)", "f(xn)/f'(xn)"]
print(tabulate(datos, headers=headers, floatfmt=(".0f", ".6f", ".6f", ".6f", ".6f")))

a = float(input("Ingrese el límite inferior del intervalo para graficar: "))
b = float(input("Ingrese el límite superior del intervalo para graficar: "))
graficar_funcion(funcion, a, b, raiz)

