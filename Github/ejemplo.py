import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def f(x, funcion):
    return eval(funcion)

def biseccion(funcion, a, b, tol=1e-6, max_iter=100):
    if f(a, funcion) * f(b, funcion) >= 0:
        print("El intervalo no es válido. La función debe cambiar de signo en el intervalo.")
        return None
    datos = []
    xr_anterior = None
    for i in range(max_iter):
        c = (a + b) / 2
        f_a = f(a, funcion)
        f_c = f(c, funcion)
        f_a_f_c = f_a * f_c
        if xr_anterior is not None:
            aproximacion = abs((c - xr_anterior) / c)
        else:
            aproximacion = None
        datos.append([a, b, c, f_a, f_c, f_a_f_c, aproximacion])
        if abs(f_c) < tol:
            break
        elif f_a * f_c < 0:
            b = c
        else:
            a = c
        xr_anterior = c
    if abs(f(c, funcion)) < tol:
        print(f"La raíz aproximada es: {c}")
    else:
        print("El método no converge después de", max_iter, "iteraciones.")
    return c, datos

def graficar_funcion(funcion, a, b):
    x = np.linspace(a, b, 100)
    y = [f(x_i, funcion) for x_i in x]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y)
    plt.axhline(0, color='black')
    plt.title(f"Gráfica de la función: {funcion}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

funcion = input("Ingrese la función (use x como variable): ")
a = float(input("Ingrese el límite inferior del intervalo: "))
b = float(input("Ingrese el límite superior del intervalo: "))
try:
    raiz, datos = biseccion(funcion, a, b)
except ZeroDivisionError:
    print("INTERVALO INVALIDO")

print("\nMétodo de Bisección:")
headers = ["a", "b", "Xr", "f(Xa)", "f(Xr)", "f(a)*f(r)", "Aproximación"]
print(tabulate(datos, headers=headers, floatfmt=(".6f", ".6f", ".6f", ".6f", ".6f", ".6f", ".6e")))

graficar_funcion(funcion, a, b)
