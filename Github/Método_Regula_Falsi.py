import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

print("Bienvenido al metodo regula falsi\n")
def f(x, funcion):
    return eval(funcion)

def regula_falsi(funcion, a, b, tol=1e-6, max_iter=100):
    if f(a, funcion) * f(b, funcion) >= 0:
        print("El intervalo no es válido. La función debe cambiar de signo en el intervalo.")
        return None
    datos = []
    for i in range(max_iter):
        c = (a * f(b, funcion) - b * f(a, funcion)) / (f(b, funcion) - f(a, funcion))
        datos.append([i, a, b, c, f(a, funcion), f(b, funcion), f(c, funcion), f(a, funcion) * f(c, funcion)])
        if abs(f(c, funcion)) < tol:
            break
        elif f(a, funcion) * f(c, funcion) < 0:
            b = c
        else:
            a = c
    if f(a, funcion) * f(c, funcion) < tol:
        print(f"La raíz aproximada es: {c}")
    else:
        print("El método no converge después de", max_iter, "iteraciones.")
    return c, datos

def graficar_funcion(funcion, a, b, raiz):
    x = np.linspace(a, b, 100)
    y = [f(x_i, funcion) for x_i in x]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
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
a = float(input("Ingrese el límite inferior del intervalo: "))
b = float(input("Ingrese el límite superior del intervalo: "))
try:
    raiz, datos = regula_falsi(funcion, a, b)
except ZeroDivisionError:
    print("INTERVALO INVALIDO")

print("\nMétodo de Regula Falsi:")
headers = ["Iteración", "a", "b", "xr", "f(a)", "f(b)", "f(xr)", "f(a)*f(xr)"]
print(tabulate(datos, headers=headers, floatfmt=(".0f", ".6f", ".6f", ".6f", ".6f", ".6f", ".6f", ".6f")))

graficar_funcion(funcion, a, b, raiz)
